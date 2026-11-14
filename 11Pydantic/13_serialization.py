# Serialization 

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str
    zip_code : str

class User(BaseModel):
    id : int
    name : str
    email : str
    is_active : bool = True
    created_at : datetime
    address : Address
    tags : List[str] = []
    
    model_config = ConfigDict(
        json_encoders={datetime : lambda v : v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=1,
    name="Kush",
    email="kushomaxe@gmail.com",
    is_active=False,
    created_at=datetime(2026,5,31,13,45,28),
    address=Address(
        street="Green",
        city="Mumbai",
        zip_code="p928"
    ),
    tags=["pro","dada"]
)

python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)

json_str = user.model_dump_json()
print("="*30)
print(json_str)

print(user.address.street)
