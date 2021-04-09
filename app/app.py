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
        print('this is setupdatabase')
        df.to_sql('APPLICANTS', con=engine, index_label='id', if_exists='replace')
        

        return

@app.route('/filter')
def filter():
    testvariable = 28
    return {'testvar': testvariable}