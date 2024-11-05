from pydantic import BaseModel
from datetime import date
class Event(BaseModel):
    name: str
    location: str
    date: date 
    description: str
    
    
