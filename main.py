# IMPORTS
from flask import Flask,render_template
from route import route
from constants import constants
from flask_session import Session

# CREATE APP
app = Flask(__name__,static_url_path='',static_folder='public',template_folder='views')

# SESSION CONFIG
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(route.home_router)
app.register_blueprint(route.contact_router)
app.register_blueprint(route.about_router)


# SERVER CONFIG
def main():      
   app.run(debug=constants.IS_DEBUG,host=constants.IP,port=constants.PORT)



if __name__ == '__main__':
    main()