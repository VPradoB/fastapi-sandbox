from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    '''
    api home page
    '''
    return {'hello': 'world'}