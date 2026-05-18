from fastapi import FastAPI
from src.api.upload import router

app=FastAPI()

app.include_router(router)


@app.get("/")

def root():

    return {

        "message":"Persona API running"

    }