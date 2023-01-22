from typing import Optional
from fastapi import FastAPI, Body, Query, Path
from Models.Person import Person
from Models.Location import Location
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
def show_person_details(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person name",
        description="Person name. Must have a length between 1 and 50 characters.",
        example="Victor"
        ),
    age: Optional[int] = Query(
        None,
        lt=140,
        gt=0,
        title="Person age",
        description="Person age. Must be greather than 0 and less than 140"),
        example=27
):
    return {name: age}

@app.get("/person/{person_id}/details")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person id",
        description="The person id. Is required and must be greater than 0",
        example=1
        )
):
    return{person_id: "It exists!"}

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person Id",
        description="The person id to update",
        gt=0,
        example=1
    ),
    person: Person = Body(...),
):
    return person