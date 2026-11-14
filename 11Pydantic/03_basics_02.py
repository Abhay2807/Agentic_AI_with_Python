# pydantic
# advanced field data types in pydantic

from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id : int
    items : List[str] # List from typing used along with str from pydantic
    # it will be list containing values of type str
    quantities : Dict[str, int]
    # it will be dict (key-value pairs) , having keys of type str and values of type int

class BlogPost(BaseModel):
    title : str
    content : str
    image_url : Optional[str] = None
    # optional, if comes then it will be str and by default it will be casted as None

cart_data = {
    'user_id' : 28,
    'items' : ['pen','bat','ball'],
    'quantities' : {
        'pen' : 10, 
        'bat' : 3,
        'ball' : 5
    }
}

blog_data = {
    'title' : 'A_Day_in_my_life',
    'content' : 'Today was highly productive and disciplined day'
}

cart_obj = Cart(**cart_data)
print(cart_obj)

blog_obj = BlogPost(**blog_data)
print(blog_obj)


