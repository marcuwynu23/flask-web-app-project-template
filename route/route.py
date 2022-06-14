from controller import controller
from flask import Blueprint

#register blueprints
home_router = Blueprint('home_router', __name__)
contact_router = Blueprint('contact_router', __name__)
about_router = Blueprint('about_router', __name__)


# routers
@home_router.route('/',methods=['GET'])
@home_router.route('/home',methods=['GET'])
def home():
	return controller.home_control()

@contact_router.route('/contact',methods=['GET'])
def contact():
	return controller.contact_control()


@about_router.route('/about',methods=['GET'])
def about():
	return controller.about_control()





