# init SQLAlchemy so we can use it later in our models

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)



    PASSWORD ="oursql-123"
    PUBLIC_IP_ADDRESS ="34.173.1.85"
    DBNAME ="oursql"
    PROJECT_ID ="oursql"
    INSTANCE_NAME ="darkhan-oursql"

    # configuration

    app.config['SECRET_KEY'] = 'somesecretstuff'
    app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"


    # app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

    db.init_app(app)

    # blueprint for auth routes in our app
    from authorization import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app

if __name__ == "main":
    app = create_app
    app.run(debug=True)