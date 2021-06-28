from fastapi import FastAPI
from typing import Optional


app = FastAPI()
fake_items_db = [
    {'item_name': 'Foo'},
    {'item_name': 'Bar'},
    {'item_name': 'Baz'},
]

'''
    input: http://127.0.0.1:8000/items/?skip=0&limit=2
    output: [
                {
                    "item_name": "Foo"
                },
                {
                    "item_name": "Bar"
                }
            ]


'''
@app.get('/items/')
async def read_item(skip:int=0, limit:int=10):
    return fake_items_db[skip:skip+limit]


# @app.get('/items/{item_id}')
# async def read_item(item_id:str, q:Optional[str]=None):
#     if q:
#         return {'item_id': item_id, 'q': q}

#     return {'item_id': item_id}

@app.get('/items/{item_id}')
async def read_item(item_id:str, q:Optional[str]=None, short:bool=False):
    item = {'item_id': item_id}

    if q:
        item.update({'q': q})

    if not short:
        item.update(
            {'description': 'This is an amazing item that has a long description'}
        )

    return item

    return {'item_id': item_id}