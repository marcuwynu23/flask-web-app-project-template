# IMPORTS
from flask import Flask,render_template
from flask_login import LoginManager
from route import route
from route import activity_route
from route.auth import auth,login_manager
from route.api import api
from flask_session import Session

# CREATE APP
app = Flask(__name__,static_url_path='',static_folder='public',template_folder='views')

# SESSION CONFIG
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#login manager
login_manager.init_app(app)


#auth route
app.register_blueprint(auth)
#basic route example
app.register_blueprint(route.home_router)
app.register_blueprint(route.contact_router)
app.register_blueprint(route.about_router)

#crud route example
app.register_blueprint(activity_route.activity,url_prefix='/activity')
#api
app.register_blueprint(api,url_prefix='/api')

# SERVER CONFIG
def main():      
   app.run(debug=True)

if __name__ == '__main__':
    main()