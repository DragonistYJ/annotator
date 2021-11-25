from fastapi import FastAPI
from router import sentence

app = FastAPI(root_path="/annotator")

app.include_router(sentence.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
