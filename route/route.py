from controller import controller
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


# routers
home_router = Blueprint('home_router', __name__)
about_router = Blueprint('about_router', __name__)


@home_router.route('/')
@home_router.route('/home')
def home(): return controller.home_control()



@about_router.route('/about')
def about(): return controller.about_control()





