# pydantic

from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True # defined default value also
    # It will be used when no value is provided for field : in_stock

product1 = Product(id=1, name="pen", price=10.98, in_stock= False)
product2 = Product(id=2, name='rubber', price=1.2) #No value provided for the field : in_stock, so it will take its default value

print(product1)
print(product2)







