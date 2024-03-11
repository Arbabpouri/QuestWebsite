from pydantic import BaseModel
from typing import Union, Optional


class Response(BaseModel):
    status: int
    message: Union[str, None] = None
    result: Optional[dict] = {}
