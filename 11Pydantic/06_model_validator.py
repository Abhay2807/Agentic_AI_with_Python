# Model Validator
# Can we used to validate multiple fields together

from pydantic import model_validator,BaseModel


class User(BaseModel):
    pwd : str
    confirm_pwd : str

    @model_validator(mode='after')
    def pwd_validator(cls, values):
        if values.pwd != values.confirm_pwd :
            raise ValueError("Password is not matching pls check")
        return values
    
user_data={
    "pwd" : "abhay",
    "confirm_pwd" : "abhay"
}

user1=User(**user_data)
print(user1)