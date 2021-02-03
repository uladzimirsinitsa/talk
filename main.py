
from app import app
from app import db
from promotions.blueprint import promotions


import view

app.register_blueprint(promotions, url_prefix='')


if __name__ == '__main__':
    app.run()
