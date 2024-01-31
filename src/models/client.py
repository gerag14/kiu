from sqlalchemy import Column, String

from db import BaseModel


class Client(BaseModel):
    username = Column(String)
