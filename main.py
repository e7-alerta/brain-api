from fastapi import FastAPI

from web.routes.address.address import address_routes

app = FastAPI()
app.include_router(address_routes)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
