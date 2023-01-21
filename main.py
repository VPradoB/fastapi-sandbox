from typing import Optional
from fastapi import FastAPI, Body, Query, Path
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

@app.get("/person/details")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: Optional[int] = Query(None, le=100, ge=1)
):
    return {name: age}

@app.get("/person/{person_id}/details")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person id",
        description="The person id. Is required and must be greater than 0"
        )
):
    return{person_id: "It exists!"}