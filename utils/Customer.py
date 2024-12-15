from dataclasses import dataclass
from enum import Enum

class Type(Enum):
    IMPORTANT = 0
    PREVENT = 1

class Category(Enum):
    STUDENT = 0
    TEACHER = 1

@dataclass
class Customer:
    name: str
    email: str
    books:list
    category: Category
    type: Type