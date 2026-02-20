from .models import EpisodeRating
from .external_api import search_tvmaze, search_anime
from flask import Blueprint, request, jsonify
from .models import User, Content, Review
from .external_api import search_tvmaze, search_anime
from .database import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# ---------------- REGISTER ----------------
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'])

    user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})


# ---------------- LOGIN ----------------
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data['email']).first()

    if user and check_password_hash(user.password, data['password']):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid email or password"}), 401


# ---------------- GET ALL CONTENT ----------------
@auth_bp.route('/all_content', methods=['GET'])
def all_content():
    contents = Content.query.all()

    result = []
    for c in contents:
        result.append({
            "id": c.id,
            "title": c.title,
            "description": c.description,
            "genre": c.genre,
            "category": c.category,
            "year": c.year,
            "poster": c.poster
        })

    return jsonify(result)


# ---------------- GET SINGLE CONTENT ----------------
@auth_bp.route('/content/<int:id>', methods=['GET'])
def get_content(id):
    c = Content.query.get(id)

    if not c:
        return jsonify({"error": "Not found"}), 404

    # calculate average rating
    reviews = Review.query.filter_by(content_id=id).all()

    if len(reviews) == 0:
        avg_rating = "No ratings yet"
    else:
        total = sum(r.rating for r in reviews)
        avg_rating = round(total / len(reviews), 1)

    return jsonify({
        "id": c.id,
        "title": c.title,
        "description": c.description,
        "genre": c.genre,
        "category": c.category,
        "year": c.year,
        "poster": c.poster,
        "avg_rating": avg_rating
    })
    if not c:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "id": c.id,
        "title": c.title,
        "description": c.description,
        "genre": c.genre,
        "category": c.category,
        "year": c.year,
        "poster": c.poster
    })


# ---------------- ADD REVIEW ----------------
@auth_bp.route('/add_review', methods=['POST'])
def add_review():
    data = request.get_json()

    review = Review(
        user_id=1,  # temporary user
        content_id=data['content_id'],
        rating=data['rating'],
        comment=data['comment']
    )

    db.session.add(review)
    db.session.commit()

    return jsonify({"message": "Review added"})


# ---------------- GET REVIEWS ----------------
@auth_bp.route('/reviews/<int:content_id>', methods=['GET'])
def get_reviews(content_id):

    reviews = Review.query.filter_by(content_id=content_id).all()

    result = []
    for r in reviews:
        user = User.query.get(r.user_id)
        result.append({
            "username": user.username if user else "User",
            "rating": r.rating,
            "comment": r.comment
        })

    return jsonify(result)
# ---------------- SEARCH CONTENT ----------------
@auth_bp.route('/search/<string:query>', methods=['GET'])
def search(query):

    results = Content.query.filter(Content.title.ilike(f"%{query}%")).all()

    output = []
    for c in results:
        output.append({
            "id": c.id,
            "title": c.title,
            "poster": c.poster,
            "year": c.year,
            "category": c.category
        })

    return jsonify(output)
# LIVE SEARCH (internet)
@auth_bp.route('/live_search/<string:query>', methods=['GET'])
def live_search(query):

    tv_results = search_tvmaze(query)
    anime_results = search_anime(query)

    return jsonify(tv_results + anime_results)
# RATE EPISODE
@auth_bp.route('/rate_episode', methods=['POST'])
def rate_episode():

    data = request.get_json()

    rating = EpisodeRating(
        user_id=1,
        show_id=data['show_id'],
        season=data['season'],
        episode=data['episode'],
        rating=data['rating'],
        comment=data['comment']
    )

    db.session.add(rating)
    db.session.commit()

    return jsonify({"message":"Episode rated!"})
