from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.get("/health")
def health_check():
    return {"status": "Running"}

@app.get("/check")
def check():
    return {"status": "Checking"}


