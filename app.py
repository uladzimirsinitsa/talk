
from flask import Flask, url_for, redirect, request
from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user
from config import Configuration

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from flask_script import Manager

from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)
from models import Promotion, User, Role


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    """Закрывает админк от общего доступа"""
    pass


class HomeAdminView(AdminMixin, ModelView):
    """Скрывает админку"""
    pass


class PromotionAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'description', 'img', 'img_alt', 'body', 'link_casino', 'over']


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

admin = Admin(app)
admin.add_view(PromotionAdminView(Promotion, db.session))


# Flask Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
