from fastapi import FastAPI
from router import sentence, label
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/annotator")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
                   allow_headers=["*"])

app.include_router(sentence.router)
app.include_router(label.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
