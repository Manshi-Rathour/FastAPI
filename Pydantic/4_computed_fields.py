from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float  # kg
    height: float # mts
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi


def insert(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print('BMI: ', patient.bmi)
    print('inserted')


patient_info = {'name': 'puja', 'age': 70, 'email': 'puja@hdfc.com', 'weight': 55.5, 'height': 1.72, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '9273129369', 'emergency': '9273129369'}}

patient1 = Patient(**patient_info)

insert(patient1)