from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

# Serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html") as f:
        return f.read()

# JSON Endpoint
@app.post("/predict")
async def predict(request: Request):
    body = await request.json()
    return {"status": "success", "received": body}
