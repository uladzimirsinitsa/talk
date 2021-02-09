
from app import db
import uuid
from datetime import datetime
from flask_security import UserMixin, RoleMixin


from utils import simple_slug_generator


class Promotion(db.Model):
    """Promotions model Data Post"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True, nullable=False)
    slug = db.Column(db.String(75), unique=True)
    description = db.Column(db.String(160), unique=True, nullable=False)
    img = db.Column(db.String(100), nullable=False)
    img_alt = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    link_casino = db.Column(db.String(300), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    over = db.Column(db.String(3))

    def __init__(self, *args, **kwargs):
        super(Promotion, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = simple_slug_generator(self.title)


    def __repr__(self):
        return '<Promotion id: {}, title: {}>'.format(self.id, self.title)


# Flask Security
roles_user = db.Table('role_users',
                      db.Column('user_id', db.Integer(),
                                db.ForeignKey('user.id')),
                      db.Column('role_id', db.Integer(),
                                db.ForeignKey('role.id'))
                      )


class User(db.Model, UserMixin):
    """Model for Authorization"""
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_user,
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    """Role Model for Site Administration"""
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
