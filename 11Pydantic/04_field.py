# Pydantic
# Concept of field (very huge, as it automates many tasks for us easily)
from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id : int
    # Defining more validations using field
    name : str = Field(
        ..., #Required field
        min_length=3,
        max_length=15,
        description="Employee's name",
        examples="Abhay Singh")
    # optional, if comes then it will be str and by default it will be 'General_Dept
    department : Optional[str] = 'General_Dept'
    salary : float = Field(
        ...,
        ge=12000, # ge : greater than or equal to (>=)
        description="Employee's salary",
        examples=12500)

employee_data={
    'id' : 28,
    'name' : 'Kush Jatt',
    'department' : 'Data Engineering',
    'salary' : '112000'}

employee_obj = Employee(**employee_data)
print(employee_obj)




