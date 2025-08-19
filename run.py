import os
from flask import Flask
from app.routes import main

# Ensure working directory is project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", "templates")
print("Template folder:", template_dir)
print("Current working directory:", os.getcwd())

app = Flask(__name__, template_folder=template_dir, static_folder=os.path.join("app","static"))
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
