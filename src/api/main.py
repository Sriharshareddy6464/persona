from fastapi import FastAPI

from src.api.upload import router

from src.api.query import (
    router as query_router
)


app=FastAPI()

app.include_router(
    router
)

app.include_router(
    query_router
)


@app.get("/")

def root():

    return {

        "message":
        "Persona API running"

    }