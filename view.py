
from app import app
from flask import render_template


@app.route('/')
def promotions():
    return render_template('main.html')
