from fastapi import FastAPI

from db_model.db_model import Hero, get_heros_db, get_session

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    if name=="Marius":
        return {"message": f"Hello my love"}
    return {"message": f"Hello {name}"}

@app.get("/heros")
async def get_heros(name: str):
    return get_heros_db(get_session())

@app.post("/heros")
async def post_hero(hero: Hero):
    return post_hero(hero,get_session())

