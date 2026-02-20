from flask import Flask, render_template
from flask_cors import CORS
from .database import db
from routes import auth_bp

import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "sidequest.db")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# REGISTER API ROUTES
app.register_blueprint(auth_bp, url_prefix='/api/auth')


# ---------- WEBSITE PAGES ----------

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Login Page
@app.route('/login')
def login():
    return render_template("login.html")

# Register Page
@app.route('/register')
def register():
    return render_template("register.html")

# Content Details Page  ⭐ IMPORTANT
@app.route('/content/<int:id>')
def content_page(id):
    return render_template("content.html")

@app.route('/show/<string:type>/<int:id>')
def show_page(type, id):
    return render_template("show.html")

# create database tables automatically (for Render too)
with app.app_context():
    db.create_all()

# DO NOT run app.run() on cloud
if __name__ == "__main__":
    app.run(debug=True)
