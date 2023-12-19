# main file
from fastapi import FastAPI

# create an instance of fastapi

app = FastAPI()


# first method
@app.get("/api/v1/projects")
async def get_project():
    return {"name": "API Projet"}
