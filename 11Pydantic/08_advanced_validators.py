# Advanced validators

from pydantic import BaseModel,field_validator

class Person(BaseModel):
    first_name : str
    last_name : str

    @field_validator('first_name','last_name')
    # Validations on multiple fields
    def name_is_capitalized(cls, v):
        if not v.istitle():
            raise ValueError("Name must be capitalized")
        return v

class User(BaseModel):
    email : str

    @field_validator('email')
    def normalize_mail(cls, v):
        return v.lower().strip()

person1 = Person(first_name='Abhay',last_name='Singh')
print(person1.first_name)

user1 = User(email='Kushomaxe@gmail.com ')
print(user1.email)