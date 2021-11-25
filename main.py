from json.encoder import JSONEncoder
from fastapi import FastAPI
from router import sentence, label, document
from fastapi.middleware.cors import CORSMiddleware
import json
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
                   allow_headers=["*"])

app.include_router(sentence.router)
app.include_router(label.router)
app.include_router(document.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
