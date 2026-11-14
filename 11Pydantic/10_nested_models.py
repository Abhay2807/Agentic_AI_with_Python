# Nested Model in pydantic
from pydantic import BaseModel

class Address(BaseModel):
    city : str
    pincode : str
    state : str

class User(BaseModel):
    name : str
    address : Address #nested Model use

# One way to use
address_user1 = Address(
    city = "Chandigarh",
    pincode="P170901",
    state="Punjab"
)

user1 = User(
    name="Abhay Singh",
    address = address_user1
)

print(user1)

# Second way to use
user2_data = {
    "name" : "Kush",
    "address" : {
        "city" :"Bilaspur", "pincode" :"HP174028", "state":"Himachal Pradesh"
    }
}

user2=User(**user2_data)
print(user2)
print(user2.name)
print(user2.address.state)
print(user2.model_dump())
print(user2.model_dump_json())



    