# advanced validators
from pydantic import BaseModel, model_validator, field_validator
from datetime import datetime
# Running field validations before
class Product(BaseModel):
    price: float

    @field_validator('price', mode='before')
    def price_parse(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v

class TimeRange(BaseModel):
    startdate: datetime
    enddate: datetime

    @model_validator(mode='after')
    def validate_date(self):
        if self.startdate >= self.enddate:
            raise ValueError("end date must be greater than start date")
        return self

product1 = Product(price="10$")
print(product1.price)

range1 = TimeRange(
    startdate='2026-10-01',
    enddate='2026-10-10'
)
print(range1.enddate)


