from flask import Flask
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from sql_db_instance import db
from arrayAPI import one_query, Variables

def create_app():
    print("this is createapp")
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///applicants.sqlite"
    db = SQLAlchemy(app)

    return app



def setup_database(app):

     with app.app_context():

        db.create_all()
        engine = db.get_engine()
        df = pd.read_csv('smallset.csv')
        print('this is setupdatabase')
        df.to_sql('APPLICANTS', con=engine, index_label='id', if_exists='replace')
        one_query()

        return