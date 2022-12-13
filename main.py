from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class LanguageEnum(str, Enum):
    python = "python"
    java = "java"
    javascript = "javascript"


@app.get("/")
def home_screen():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "user me selected", "another": "field"}


@app.get("/users/{user_id}")
async def read_item(user_id: int):
    return {"user_id": user_id}


@app.get("/language/{language_name}")
async def read_language_name(language_name: LanguageEnum):
    if language_name is LanguageEnum.python:
        return {"language_name": language_name, "message": "that got coded quickly"}

    if language_name is LanguageEnum.java:
        return {"language_name": language_name, "message": "that is some strict typing"}

    if language_name is LanguageEnum.javascript:
        return {"language_name": language_name, "message": "you got any libraries? React maybe?"}


@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path": file_path}