from fastapi import FastAPI
import requests


app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Livreen API V1.0"}

@app.get('/recent_books')
async def root():
    request = requests.get('https://tyfee.github.io/livreen-api/json/recents.json')
    all = request.json()
    return all

@app.get('/books')
async def root():
    request = requests.get('https://tyfee.github.io/livreen-api/json/v1.json')
    all = request.json()
    return all

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


