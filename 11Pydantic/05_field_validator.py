# Field Validator
# Validates one field at a time


from pydantic import BaseModel, field_validator

class User(BaseModel):
    username : str

    @field_validator('username')
    def username_length(cls, value):
        if len(value)<4:
            raise ValueError("Length of the username cannot be less than 4")
        return value
    
user_data = {
    "username" : "abhay"
}

user1=User(**user_data)
print(user1.username)



