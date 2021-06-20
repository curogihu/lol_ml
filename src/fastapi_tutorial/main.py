# import uvicorn
from fastapi import FastAPI

app = FastAPI()

# somehow it does not work...
# => I forgot changing current directory path
@app.get("/")
async def root():
    return {"message": "Hello World"}
