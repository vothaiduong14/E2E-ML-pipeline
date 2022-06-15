from datetime import date
from xmlrpc.client import boolean
from pydantic import BaseModel

class Record(BaseModel):
    id: int
    gender: str
    age: int
    driving_license: int
    region_code: int
    previously_insured: bool
    vehicle_age: str
    vehicle_damage:str
    annual_premium: int
    policy_sales_channel: int
    vintage: int
    response: int



