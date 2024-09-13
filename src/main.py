import typing

import fastapi

import schemas
import repositories

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
async def create_user(
    user_in: schemas.UserBase,
    user_repository: typing.Annotated[
        repositories.UserRepository, fastapi.Depends(repositories.UserRepository)
    ] = repositories.UserRepository(SQLALCHEMY_DATABASE_URL),
) -> schemas.User:
    user = user_repository.add(user_in.username, user_in.email)
    return user


@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(
    user_id: int,
    user_repository: typing.Annotated[
        repositories.UserRepository, fastapi.Depends(repositories.UserRepository)
    ] = repositories.UserRepository(SQLALCHEMY_DATABASE_URL),
):
    user = user_repository.get(user_id)
    if user is None:
        raise fastapi.HTTPException(status_code=404)
    return user
