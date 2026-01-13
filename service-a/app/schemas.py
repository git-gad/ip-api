from pydantic import BaseModel,IPvAnyAddress

class IP(BaseModel):
    ip: IPvAnyAddress