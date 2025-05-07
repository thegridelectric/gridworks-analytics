from pydantic import BaseModel

class HourlyElectricity(BaseModel):
    hour_start_ms: str
    electricity: float
    
    def to_dict(self):
        return {
            "hour_start_ms": self.hour_start_ms,
            "electricity": self.electricity
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)