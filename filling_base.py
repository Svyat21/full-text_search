import csv
from datetime import datetime
from app.models import Document
from app import db


def copying_to_base():
    with open('posts.csv', 'r', newline='', encoding='utf-8') as file:
        data = csv.DictReader(file)
        for row in data:
            post = Document(
                rubrics=row['rubrics'],
                text=row['text'],
                created_date=datetime.strptime(row['created_date'], "%Y-%m-%d %H:%M:%S")
            )
            db.session.add(post)
            db.session.commit()
