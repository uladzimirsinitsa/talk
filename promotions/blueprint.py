from flask import Blueprint
from flask import render_template
import models
from models import Promotion


promotions = Blueprint('promotions', __name__)


@promotions.route('/')
def main():
    """Home page"""
    data = Promotion.query.all()
    return render_template('main.html', data=data)





