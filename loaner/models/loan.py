from typing import Optional
from pydantic import BaseModel

class Loan(BaseModel):
    id: Optional[str]