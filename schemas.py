from pydantic import BaseModel
from typing import Optional, Any

class ConfigBase(BaseModel):
    id: int
    key: str
    value: Any  # Supports JSON
    is_deleted: bool
    config_group_id: Optional[int] = None
    config_desc: Optional[str] = None

    class Config:
        orm_mode = True
