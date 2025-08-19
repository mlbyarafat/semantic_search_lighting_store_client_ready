import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset relative to this file
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'products_demo.csv'))

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# Ensure required columns exist
for col in ['product_name', 'description']:
    if col not in df.columns:
        raise ValueError(f"Dataset must contain '{col}' column")


# Prepare a combined text field for better search
df['search_text'] = (df['product_name'].fillna('') + ' ' + df['description'].fillna('') + ' ' + df.get('material','').fillna('') + ' ' + df.get('finish','').fillna(''))

vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = vectorizer.fit_transform(df['search_text'])

def semantic_search(query, top_k=5):
    if not query or str(query).strip()=="": 
        return []
    query_vec = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = cosine_similarities.argsort()[-top_k:][::-1]
    results = df.iloc[top_indices][['product_id','product_name','description','material','finish','category']].to_dict(orient='records')
    # Filter out empty matches (cosine 0)
    filtered = [r for i,r in zip(top_indices, results) if cosine_similarities[i] > 0]
    return filtered
