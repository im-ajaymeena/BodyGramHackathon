from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route (endpoint) for the "Hello, World!" message
@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}