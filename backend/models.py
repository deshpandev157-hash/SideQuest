from .database import db

# USER TABLE
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# CONTENT TABLE
class Content(db.Model):
    __tablename__ = "content"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    genre = db.Column(db.String(100))
    category = db.Column(db.String(50))
    year = db.Column(db.Integer)
    poster = db.Column(db.String(300))


# REVIEW TABLE
class Review(db.Model):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    content_id = db.Column(db.Integer, db.ForeignKey("content.id"))
class EpisodeRating(db.Model):
    __tablename__ = "episode_rating"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)
    show_id = db.Column(db.Integer)      # tvmaze or anime id
    season = db.Column(db.Integer)
    episode = db.Column(db.Integer)

    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
