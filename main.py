from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://livreen-tyfee.vercel.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {"message": "Livreen API V1.0"}

@app.get('/recent_books')
async def root():
     with open('json/recents.json') as fp:
      data = json.load(fp)
      return data

@app.get('/books')
async def root():
    with open('json/v1.json') as fp:
      data = json.load(fp)
      return data

@app.get('/book')
async def root(id:str):
    request = requests.get('https://tyfee.github.io/livreen-api/json/' + id + '.json')
    all = request.json()
    return all

@app.get('/line')
async def root(id:str, line: str):
    request = requests.get('https://tyfee.github.io/livreen-api/json/' + id + '.json')
    all = request.json()
    return all[line]


