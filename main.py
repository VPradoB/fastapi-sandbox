from fastapi import FastAPI, Body
from Models.Person import Person
app = FastAPI()


@app.get("/")
def home():
    '''
    api home page
    '''
    return {'hello': 'world'}

@app.post("/person")
def create_person(person: Person = Body(...)):
    return person
