from fastapi import FastAPI, Query
from enum import Enum
from typing import Union, List
from pydantic import BaseModel  # For request body (POST, PUT, PATCH, DELETE

app = FastAPI()

# Enum class
class LanguageEnum(str, Enum):
    python = "python"
    java = "java"
    javascript = "javascript"


################################################## GET OPERATIONS
# 'Home screen'
@app.get("/")
def home_screen():
    return {"message": "Hello World"}


# Takes item_id in path and returns as JSON
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Returns users /me
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "user me selected", "another": "field"}


# Same path as above but takes integer only runs if above operation does not
@app.get("/users/{user_id}")
async def read_item(user_id: int):
    return {"user_id": user_id}


# Constricts /language/ to only accept values in Enum
@app.get("/language/{language_name}")
async def read_language_name(language_name: LanguageEnum):
    if language_name is LanguageEnum.python:
        return {"language_name": language_name, "message": "that got coded quickly"}

    if language_name is LanguageEnum.java:
        return {"language_name": language_name, "message": "that is some strict typing"}

    if language_name is LanguageEnum.javascript:
        return {"language_name": language_name, "message": "you got any libraries? React maybe?"}


# Allows a file path to be passed to read_file function
@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path": file_path}


# Takes two integer parameters and returns the sum through a query
# Example - addtwoints/?int1=10&int2=15 (if no query defaults to zero)
@app.get("/addtwoints/")
async def query_parameters(int1: int=0, int2: int=0):
    return {"Total" : (int1 + int2)}


# Example of multiple parameters and their defaults
@app.get("/parametertypes/")
async def query_parameters(int1: int=9, isTrue: bool=False, name: str = 'Hi'):
    # works on query 'addtwoints/?int1=10&int2=15' = 25
    # defaults are 0 and 0 for these query parameters
    return {"All parameters" : str(int1) + ' ' + str(isTrue) + ' ' + str(name)}


# Multiple path parameters and queries
# q is an OPTIONAL query
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": "This was a query"})
    else:
        item.update({"q": "This was not a query"})
    return item


# Multiple path parameters and queries
# q is a REQUIRED query (no default value)
# Example requiredquery/10/items/banana?q=a
@app.get("/requiredquery/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Union[str, None]):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": "This was a query"})
    else:
        item.update({"q": "This was not a query"})
    return item


# Constrain query ( => 2 and <= 10 and starts with 'B')
@app.get("/limitedquery/")
async def foo(q:Union[str, None] =  Query(default="B_default_query_can_break_size_rule", min_length=2, max_length=10, regex="^B")):
    results = {"item": "this is an item"}
    if q:
        results.update({"query is": q})
    return results


# Query list
@app.get("/querylist/")
async def go(q: Union[List[str], None] = Query(default=None)):
    queryList = {}
    for i, each in enumerate(q):
        queryList[f"Query {i}"] = each
    return queryList


################################################## SEND (AS REQUEST BODY) OPERATIONS
# Base model class
class Item (BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


# create_item expects an item structured like Item class
# test functionality of POST in /docs
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        item_dict.update({"Price inc tax": item.price + item.tax})
    return item_dict


# operation that includes REQUEST BODY and PATH and QUERY parameters
@app.post("/trifector/item_id")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result



