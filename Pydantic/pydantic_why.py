from pydantic import AnyUrl ,BaseModel ,EmailStr , Field

from typing import Dict, List, Optional



class Patient(BaseModel):
    name: str =Field(max_length= 50)
    age: int = Field(gt=0 , le=120)
    email : EmailStr
    linkedin_url: AnyUrl
    weight : float = Field(gt=0)
    married : bool
    allergies : Optional[List[str]]=Field(max_length = 5)
    contact_details : Dict[str , str]
    
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.linkedin_url)
    print(patient.allergies)
    print("updated")
    
    
patient_info = {
    'name': 'mayur',
    'age' : 22,
    'email': 'abc@gmail.com',
    'linkedin_url': 'https://100xdevs.com/',
    'weight' : 70.0,
    'married': True,
    # 'allergies': ['Pollen' , 'Dust'],
    'contact_details' :{
        
        'phone' : '123144341790'
    }    
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
