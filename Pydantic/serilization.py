from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()
temp1 = patient1.model_dump_json()
temp2  = patient1.model_dump(include=['name'])
temp3  = patient1.model_dump(exclude=['name'])
temp4 = patient1.model_dump(exclude_unset=True)


print(temp)
print(type(temp))
print(temp1)
print(type(temp1))
print(temp2)
print(temp3)
print(temp4)

#output:

#{'name': 'nitish', 'gender': 'Male', 'age': 35, 'address': {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}}
#<class 'dict'>

# json
# {"name":"nitish","gender":"Male","age":35,"address":{"city":"gurgaon","state":"haryana","pin":"122001"}}
# <class 'str'>