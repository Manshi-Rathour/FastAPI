from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated



class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Priya'])]
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient is married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

def insert(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print('inserted')


patient_info = {'name': 'puja', 'age': 30, 'email': 'puja@email.com', 'weight': 55.5, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '9273129369'}}

patient1 = Patient(**patient_info)

insert(patient1)