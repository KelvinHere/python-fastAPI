# python-fastAPI
Having a look at fastAPI


##
See main.py for operations examples


## Operations
I have implemented different operations to get used to FastAPI.  The input type of these operations can be constrained by defining a type for example. 

<pre># Will take any value
@app.get("/users/{user_id}")
    async def read_item(user_id):</pre>

<pre># Expects an integer to be supplied
@app.get("/users/{user_id}")
    async def read_item(user_id: int):</pre>

<pre># Constrained to values in Enum
@app.get("/specific/{enumHere}")
    async def read_item(specificValue :enumHere):</pre>

## Start Uvicorn server
```uvicorn main:app --reload```
--reload: make the server restart after code changes.  Development use only.

## Useful paths

```/docs``` Lets you see all path operation decorators and schemas etc.
```/redocs``` Generates documentation from the OpenAPI definitions