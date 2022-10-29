from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello_world():
    return ("api is working")



@app.post('/search')
async def searchitem(keyword:str):
    return "url1"
