from fastapi import FastAPI, status

from pymongo import MongoClient
from bson import json_util
import json
from pykap import get_general_info
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGODB_URL = os.environ.get("MONGODB_URL")

client = MongoClient(MONGODB_URL)

db = client['mikroskop']
collection = db['bist_companies']


app = FastAPI(title='KAP API', description='KAP(Public Disclosure Platform) Documentation API for Capital Markets Board of Turkey and Borsa Istanbul Public Disclosures')



@app.get('/')
def welcome():
    '''
    The root route which returns a JSON response.

    The JSON response is delivered as:

    '''
    return {'message': 'Welcome please go to /docs for more info!'}



@app.get("/stock/{tick}")
def read_financial(tick: str):
    # comp = BISTCompany(ticker = tick)
    # pr = comp.get_financial_reports()
    pr = collection.find({'ticker': tick})

    return json.loads(json_util.dumps(pr[0]))

@app.get("/general/{tick}")
def read_general(tick: str):
    gi = get_general_info(tick=tick)
    return gi




