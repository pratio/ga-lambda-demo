import requests
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title='Lambda Github CI/CD Pratyay Modi')
handler = Mangum(app=app)


@app.get("/",  tags=["Endpoint Test"])
def main():
    return {"message": "FastAPI Lambda on github actions"}


@app.get("/comments")
def comments():
    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}
    
@app.get("/posts")
def posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}


@app.get("/posts/{index}")
def comments(index: int):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{index}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}
    

@app.get("/comments/{index}")
def comments(index: int):
    response = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={index}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

