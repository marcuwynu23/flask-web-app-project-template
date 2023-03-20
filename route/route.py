from controller import controller
from flask import Blueprint
from flask_login import login_required

#register blueprints
home_router = Blueprint('home', __name__)
contact_router = Blueprint('contact', __name__)
about_router = Blueprint('about', __name__)


# routers
@home_router.route('/',methods=['GET'])
@home_router.route('/home',methods=['GET'])
@login_required
def home():
	return controller.home_control()

@contact_router.route('/contact',methods=['GET'])
@login_required
def contact():
	return controller.contact_control()


@about_router.route('/about',methods=['GET'])
@login_required
def about():
	return controller.about_control()




