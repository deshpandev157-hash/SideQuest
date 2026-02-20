from app import app
from database import db
from models import Content

sample_content = [
    ("Attack on Titan","Humans fight giant Titans to survive.","Action","anime",2013,"https://upload.wikimedia.org/wikipedia/en/7/7a/Attack_on_Titan_season_1.jpg"),
    ("Breaking Bad","A chemistry teacher becomes a drug kingpin.","Crime","tv",2008,"https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png"),
    ("Interstellar","Astronauts travel through a wormhole in space.","Sci-Fi","movie",2014,"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"),
    ("Demon Slayer","A boy becomes a demon slayer to save his sister.","Fantasy","anime",2019,"https://upload.wikimedia.org/wikipedia/en/4/4a/Demon_Slayer_Kimetsu_no_Yaiba_volume_1_cover.jpg"),
    ("Game of Thrones","Noble families fight for control of the Iron Throne.","Fantasy","tv",2011,"https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg")
]

with app.app_context():
    for title,desc,genre,cat,year,poster in sample_content:

        # prevent duplicates
        exists = Content.query.filter_by(title=title).first()
        if exists:
            continue

        content = Content(
            title=title,
            description=desc,
            genre=genre,
            category=cat,
            year=year,
            poster=poster
        )

        db.session.add(content)

    db.session.commit()

print("Clean library added!")
