# PYDANTIC
# COMPUTED PROPERTY

from pydantic import BaseModel, computed_field, Field

class RoomBooking(BaseModel):
    user_id : int
    room_no : int
    nights : int = Field(...,ge=1)
    price_per_night : float

    # To calculate total bill for staying
    @computed_field
    @property
    # It will make it accessible as a attribute (total_bill), not as a method
    def total_bill(self) -> float:
        return (self.nights * self.price_per_night)
    
data = {
    "user_id" : 1, 
    "room_no" : 28,
    "nights" :  7,
    "price_per_night" : 4000
}

booking1 = RoomBooking(**data)
print(booking1.total_bill)
print(booking1.model_dump()) #list down all attributes and their values
# The total_bill is now also an attribute



    