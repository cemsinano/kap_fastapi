from fastapi import FastAPI, status

from pymongo import MongoClient
from bson import json_util
import json

client = MongoClient(
    "mongodb+srv://cemsinan:cemsinanUserPassword@cluster0.ombz1.mongodb.net/mikroskop?retryWrites=true&w=majority")

db = client['mikroskop']
collection = db['bist_companies']



app = FastAPI()


@app.get("/stock/{tick}")
def read_financial(tick: str):
    # comp = BISTCompany(ticker = tick)
    # pr = comp.get_financial_reports()
    pr = collection.find({'ticker': tick})

    json.loads(json.dumps(pr[0], default=json_util.default, ensure_ascii=False))

    # return json.loads(json_util.dumps(pr[0]))





@app.get('/')
def welcome():
    '''
    The root route which returns a JSON response.

    The JSON response is delivered as:

    '''
    return {'message': 'Welcome!'}

"""
@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    '''
    Simple route for the GitHub Actions to healthcheck on.

    More info is available at:
    https://github.com/akhileshns/heroku-deploy#health-check

    It basically sends a GET request to the route & hopes to get a "200"
    response code. Failing to return a 200 response code just enables
    the GitHub Actions to rollback to the last version the project was
    found in a "working condition". It acts as a last line of defense in
    case something goes south.

    Additionally, it also returns a JSON response in the form of:

    {
      'healtcheck': 'Everything OK!'
    }
    '''
    return {'healthcheck': 'Everything OK!'}
"""
