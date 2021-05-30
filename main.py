# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, NameEmail
#from pykap import BISTCompany, get_general_info

from pymongo import MongoClient
from bson import json_util
import json

client = MongoClient(
    "mongodb+srv://cemsinan:cemsinanUserPassword@cluster0.ombz1.mongodb.net/mikroskop?retryWrites=true&w=majority")

db = client['mikroskop']
collection = db['bist_companies']

app = FastAPI()


class Subscriber(BaseModel):
    full_name: str
    email: NameEmail


@app.post("/s")
async def newUser(sub: Subscriber):
    name = sub.full_name
    email = sub.email

    # you could also return sub.json() or sub.dict()
    return {
        "full_name": name,
        "email": email
    }


#@app.get("/subs/{sub_id}")
#async def read_item(sub_id: int, q: Optional[str] = None):
#    return {"sub_id": sub_id, "q": q}

@app.get("/")
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@app.get("/stock/{tick}")
async def read_financial(tick: str):
    # comp = BISTCompany(ticker = tick)
    # pr = comp.get_financial_reports()
    pr = collection.find({'ticker': tick})
    print(pr[0])

    return json.loads(json_util.dumps(pr[0]))


#@app.get("/general/{tick}")
#def read_general(tick: str):
#    gi = get_general_info(tick=tick)
#    return gi
