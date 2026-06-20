from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError(
                'Patient older than 60 must have an emergency contact'
            )
        return self


def insert(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print('inserted')


patient_info = {'name': 'puja', 'age': 70, 'email': 'puja@hdfc.com', 'weight': 55.5, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '9273129369', 'emergency': '9273129369'}}

patient1 = Patient(**patient_info)

insert(patient1)