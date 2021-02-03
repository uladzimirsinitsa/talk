
from app import db
from datetime import datetime
import re


def slugify(s):
    """title ==> Slug"""
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Promotion(db.Model):
    """Promotions model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    slug = db.Column(db.String(75), unique=True)
    description = db.Column(db.String(160), unique=True)
    img = db.Column(db.String(100))
    img_alt = db.Column(db.String(100))
    body = db.Column(db.Text)
    link_casino = db.Column(db.String(300))
    created = db.Column(db.DateTime, default=datetime.now())


    def __init__(self, *args, **kwargs):
        super(Promotion, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        """Slug title"""
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Promotion id: {}, title: {}>'.format(self.id, self.title)

