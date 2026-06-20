from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address


address_dict = {'city': 'patna', 'state': 'bihar', 'pin': '801113'}

address1 = Address(**address_dict)

patient_dict = {'name': 'manshi', 'age': 22, 'gender': 'F', 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)