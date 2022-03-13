from flask import Flask,render_template
from route import route
from constants import constants

app = Flask(
   __name__,
   static_url_path='',
   static_folder='static',
   template_folder='templates'
)

app.register_blueprint(route.home_router)
app.register_blueprint(route.about_router)

def main():      
   app.run(debug=constants.IS_DEBUG,host=constants.IP,port=constants.PORT)

if __name__ == '__main__':
    main()