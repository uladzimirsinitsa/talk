from flask import Blueprint
from flask import render_template
from models import Promotion

from flask_security import login_required

promotions = Blueprint('promotions', __name__)


@promotions.route('/')
def main():
    """Home page"""
    data = Promotion.query.all()
    return render_template('main.html', data=data)


@promotions.route('/<slug>')
def promo_detail(slug):
    """Detail page"""
    promotion = Promotion.query.filter(Promotion.slug==slug).first()
    return render_template('promo_detail.html', promotion=promotion)





