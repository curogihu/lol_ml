from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI()


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep learning ftw'}

    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    return {'model_name': model_name, 'message': 'Have some residuals'}




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