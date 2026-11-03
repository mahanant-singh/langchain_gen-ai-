from pydantic import BaseModel,EmailStr
from typing import Optional
class Student(BaseModel):
    name:str='mahanant singh'
    age:Optional[int]=None
    email:EmailStr
new_student={'age':'23','emal':'abv2gmail.com'}
student=Student(**new_student)
print(student)