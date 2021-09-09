from pydantic import BaseModel, Field

## Models
class UserList(BaseModel):
    id        : str
    username  : str
    password  : str
    first_name: str
    last_name : str
    gender    : str
    create_at : str
    status    : str

class UserEntry(BaseModel):
    username  : str = Field(..., example="username")
    password  : str = Field(..., example="password")
    first_name: str = Field(..., example="first_name")
    last_name : str = Field(..., example="last_name")
    gender    : str = Field(..., example="M or F")
    
class UserUpdate(BaseModel):
    id        : str = Field(..., example="Enter your id")
    first_name: str = Field(..., example="first_name")
    last_name : str = Field(..., example="last_name")
    gender    : str = Field(..., example="M or F")
    status    : str = Field(..., example="1")
class UserDelete(BaseModel):
    id: str = Field(..., example="Enter your id")