from flask import Flask
import pandas as pd
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///applicants.sqlite"
db = SQLAlchemy(app)



def setup_database(app):

     with app.app_context():

        db.create_all()
        engine = db.get_engine()
        df = pd.read_csv('smallset.csv')
        
        df.to_sql('APPLICANTS', con=engine, index_label='id', if_exists='replace')
        
        print('this is setupdatabase')
        return


def call_filter(app):

    @app.route('/filter')
    def filter():
        print('this is callfilter')
        testvariable = 28
        return {'testvar': testvariable}