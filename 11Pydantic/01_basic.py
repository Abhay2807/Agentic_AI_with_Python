# pydantic basics

from pydantic import BaseModel

# define our pydantic class

class player(BaseModel):
    # defining type annotations for pydantic class
    age : int
    name : str
    is_legend : bool

# Input data 

player_data = {
    'age' : 40,
    'name' : 'Rohit',
    'is_legend' : True
}

# Creating an object from pydantic class
# Send the unpack (**) dictionary to the base model for data validation
player1 = player(**player_data)
print(player1)

