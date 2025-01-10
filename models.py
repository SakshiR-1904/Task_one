from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class Config(Base):
    __tablename__ = "config"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)  # Unique key
    value = Column(JSON)  # Storing JSON data
    is_deleted = Column(Boolean, default=False)  # Soft delete flag
    config_group_id = Column(Integer, ForeignKey("config_group.id"), nullable=True)  # Foreign key
    config_desc = Column(String, nullable=True)  # Description

    # Relationship (if there's a ConfigGroup model)
    config_group = relationship("ConfigGroup", back_populates="configs", lazy="joined")

