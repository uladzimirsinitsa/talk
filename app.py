
from flask import Flask, render_template
from flask_admin import Admin
from config import Configuration
from promotions.blueprint import promotions
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config.from_object(Configuration)


db = SQLAlchemy(app)

app.register_blueprint(promotions, url_prefix='/promotions')

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here



@app.route('/')
def main():
    return render_template('main.html')


app.run()


if __name__ == '__main__':
    app.run()
