from flask import Flask
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from models import Variables
from sql_db_instance import db


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




@app.route('/filter')
def filter():
    print('this is callfilter')
    income_var = (db.session.query(Variables).filter(Variables.age >= 58))
    testvariable = [variable.name for variable in income_var]

    return {'testvar': testvariable}

