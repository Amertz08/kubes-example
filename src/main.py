import fastapi

import schemas

# TODO: how to get this via envar/kube secret
SQLALCHEMY_DATABASE_URL = "postgresql+pg8000://postgres:password@postgres:5432/postgres"
app = fastapi.FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/healthcheck")
async def healthcheck():
    return {"Healthy": True}


@app.post("/users", status_code=201, response_model=schemas.User)
async def create_user():
    return {"id": 1, "username": "hi", "email": "hello@example.com"}
