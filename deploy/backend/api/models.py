'''
This module define columns of our table within postgres
New table will be created when the application starts
This doesn't change the already exiting database.
'''


# sourcery skip: avoid-builtin-shadow
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    driving_license = Column(Integer, nullable=False)
    region_code = Column(Integer, nullable=False)
    previously_insured = Column(Boolean, nullable=False)
    vehicle_age = Column(String, nullable=False)
    vehicle_damage = Column(String, nullable=False)
    annual_premium = Column(Integer, nullable=False)
    policy_sales_channel = Column(Integer, nullable=False)
    vintage = Column(Integer, nullable=False)
    response = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)



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

