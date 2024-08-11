from pydantic import  BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateTask(BaseModel):
    title: str
    lastname: str
    priority: int

class UpdateTask(BaseModel):
    title: str
    lastname: str
    priority: int
