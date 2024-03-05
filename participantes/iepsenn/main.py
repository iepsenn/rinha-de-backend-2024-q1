from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def get_root():
    return {"Welcome to my solution to solve Rinha de Backend challenge!!!!!"}
