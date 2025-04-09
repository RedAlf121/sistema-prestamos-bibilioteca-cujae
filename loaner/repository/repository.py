from pydantic import BaseModel

class Repository:
    def __init__(self,database):
        self.database=database
    def set_database(self,database):
        self.database=database
    
    def insert(model:BaseModel):
        pass
    def update(model:BaseModel):
        pass
    def delete(model:BaseModel):
        pass
    def find(model:BaseModel,id:str):
        pass
    def find_all(model:BaseModel):
        pass