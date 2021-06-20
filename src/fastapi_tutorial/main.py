# import uvicorn
from fastapi import FastAPI

app = FastAPI()

# somehow it does not work...
# => I forgot changing current directory path
@app.get("/")
async def root():
    return {"message": "Hello World"}


'''
    input: http://127.0.0.1:8000/items/foo
    output: "item_id":"foo"
'''
# @app.get('/items/{item_id}')
# async def read_item(item_id):
#     return {'item_id': item_id}


'''
    input: http://127.0.0.1:8000/items/192
    output: "item_id": 192
'''
@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}
