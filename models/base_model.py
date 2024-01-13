#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid4())
            if not any(key in kwargs for key in ["created_at", "updated_at"]):
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        
    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"
    
    def save(self):
        self.updated_at = self.updated_at.now()
        
    def to_dict(self):
        dics = self.__dict__
        dics["__class__"] = self.__class__.__name__
        dics["created_at"] = self.created_at.isoformat()
        dics["updated_at"] = self.updated_at.isoformat()
        
        
        return dics
       

