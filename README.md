# 💡 Lighting Store — Semantic Search Demo

This project is a **semantic product search web app** for Saas Instrument Oy.  
It demonstrates how customers can search products using **natural queries** (e.g., *"wooden lamp"*, *"brass chandelier"*).

---

## 🚀 Features
- **Semantic Search** using TF‑IDF similarity for accurate product matching.
- **Modern Responsive UI** (desktop, tablet, mobile friendly).
- **Interactive Search Experience**:
  - Quick suggestion chips
  - Animated loading skeletons
  - Live feedback messages
- **Attractive, polished design** with dark/light theme support.
- **Client-ready demo data** (replace with real product CSV from Kaggle).

---

## 📂 Project Structure
```
01_semantic_search_lighting_store_client_ready/
│── app/
│   ├── data/               # CSV dataset goes here
│   ├── model/              # Precomputed TF-IDF model (optional)
│   ├── server.py           # Flask backend
│── static/
│   ├── style.css           # Styling (if separated)
│── templates/
│   ├── index.html          # UI (Responsive front-end)
│── run.py                  # Entry point to run app
│── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the project
```bash
git clone <your-repo-link>
cd 01_semantic_search_lighting_store_client_ready
```

### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate     # Windows PowerShell
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
python run.py
```
The app will be available at: **http://127.0.0.1:5000/**

---

## 📊 Data
- Place your **products dataset CSV** inside `app/data/` folder.
- Ensure it has columns like: `product_name, description, material, finish, image_url (optional)`.

---

## 🎨 UI Preview
- Sticky glassmorphic header
- Responsive product grid cards
- Suggestion chips for quick queries
- Smooth animations and loading skeletons

---

## 🤝 Client Notes
- Demo is **fully functional** with sample data.
- Replace dataset with real client product data for production use.
- Brand colors, logo, and product images can be customized as required.

---

## 📜 License
This project is provided as a **demo client deliverable**.  
You may customize and extend for real production deployments.

---
✨ Prepared with care, by the grace of Allah.
