from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Calculator"}

@app.get("/add")
async def add(a: float, b: float):
    return {"operation": "addition", "result": a + b}

@app.get("/subtract")
async def subtract(a: float, b: float):
    return {"operation": "subtraction", "result": a - b}

@app.get("/multiply")
async def multiply(a: float, b: float):
    return {"operation": "multiplication", "result": a * b}

@app.get("/divide")
async def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"operation": "division", "result": a / b}