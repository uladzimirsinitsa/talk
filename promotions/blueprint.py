
from flask import Blueprint, render_template

promotions = Blueprint('promotions', __name__, template_folder='templates')


@promotions.route('/')
def list_promotions():
    return render_template('main.html')


