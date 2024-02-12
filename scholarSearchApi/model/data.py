from sqlalchemy import Column, Integer, String, Float
from .. import db

class Data(db.Model):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    school_url = Column(String)
    admission_rate = Column(Float)
    average_sat = Column(Integer)
    address = Column(String)
    tuition_in_state = Column(Float)
    tuition_out_of_state = Column(Float)

    def __init__(self, name, city, state, zip_code, school_url=None, admission_rate=None, average_sat=None, address=None, tuition_in_state=None, tuition_out_of_state=None):
        self.name = name
        self.city = city
        self.state = state
        self.zip = zip_code
        self.school_url = school_url
        self.admission_rate = admission_rate
        self.average_sat = average_sat
        self.address = address
        self.tuition_in_state = tuition_in_state
        self.tuition_out_of_state = tuition_out_of_state
    
    def __repr__(self):
        return f"id='{self.id}', name='{self.name}', city='{self.city}', state='{self.state}', zip='{self.zip}', school_url='{self.school_url}', admission_rate='{self.admission_rate}', average_sat='{self.average_sat}', address='{self.address}', tuition_in_state='{self.tuition_in_state}', tuition_out_of_state='{self.tuition_out_of_state}'"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "school_url": self.school_url,
            "admission_rate": self.admission_rate,
            "average_sat": self.average_sat,
            "address": self.address,
            "tuition_in_state": self.tuition_in_state,
            "tuition_out_of_state": self.tuition_out_of_state
        }

def init_data():
    college1 = Data(
        name="University of Example", 
        city="Example City", 
        state="Example State", 
        zip_code="12345", 
        school_url="https://www.example.edu", 
        admission_rate=0.75, 
        average_sat=1200, 
        address="123 Example St", 
        tuition_in_state=15000.00, 
        tuition_out_of_state=30000.00
    )
    college2 = Data(
        name="Example College", 
        city="Another City", 
        state="Another State", 
        zip_code="54321", 
        school_url="https://www.examplecollege.edu", 
        admission_rate=0.80, 
        average_sat=1300, 
        address="456 College Ave", 
        tuition_in_state=20000.00, 
        tuition_out_of_state=35000.00
    )
    
    
    
    db.session.add(college1)
    db.session.add(college2)
    
    db.session.commit()
