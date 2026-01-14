from pydantic import BaseModel

class CoordinatesData(BaseModel):
    ip: str
    coordinates: str