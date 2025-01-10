# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# from sqlalchemy.orm import relationship
# from app.database import Base

# class Config(Base):
#     __tablename__ = 'config'
#     __table_args__ = {"schema": "config"} 
#     id = Column(Integer, primary_key=True, index=True)
#     key = Column(String, index=True)
#     value = Column(String)
#     is_deleted = Column(Boolean, default=False)
#     config_group_id = Column(Integer, ForeignKey('custom_field_group.id'))
#     config_desc = Column(String)

#     # Relationship with CustomFieldGroup (Optional, for querying related data)
#     config_group = relationship("CustomFieldGroup", back_populates="configs")


# class CustomFieldGroup(Base):
#     __tablename__ = 'custom_field_group'
#     id = Column(Integer, primary_key=True, index=True)
#     custom_field_group_code = Column(String, index=True)
#     custom_field_group_desc = Column(String)
#     loopup_id = Column(Integer)

#     # Reverse relationship with Config
#     configs = relationship("Config", back_populates="config_group")

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey , TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql import func 

# Config Table
class Config(Base):
    __tablename__ = 'config'
    __table_args__ = {"schema": "config"} 

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, index=True)
    value = Column(String)
    is_deleted = Column(Boolean, default=False)
    config_group_id = Column(Integer, ForeignKey("config.custom_field_group.id"))
    config_desc = Column(String)

    # Relationship with CustomFieldGroup
    config_group = relationship("CustomFieldGroup", back_populates="configs")

    # config_group_id = Column(Integer, ForeignKey("config.custom_field_group.id"))



# Custom Field Group Table
class CustomFieldGroup(Base):
    __tablename__ = 'custom_field_group'
    __table_args__ = {"schema": "config"} 
    
    id = Column(Integer, primary_key=True, index=True)
    custom_field_group_code = Column(String, index=True)
    custom_field_group_desc = Column(String)
    lookup_id = Column(Integer)

    # Reverse relationship with Config
    configs = relationship("Config", back_populates="config_group")


# Dynamic Item Form Field Table
class DynamicItemFormField(Base):
    __tablename__ = "dynamic_item_form_field"
    __table_args__ = {"schema": "config"}

    id = Column(Integer, primary_key=True, index=True)
    form_field_name = Column(String, index=True)  # Rename this column
    form_field_label = Column(String)  # Consider renaming `form_field_label`
    template_id = Column(Integer, index=True)
    group_id = Column(Integer, index=True)
    control_type = Column(String, nullable=True)



# Expressions Table
class Expressions(Base):
    __tablename__ = 'expression'
    __table_args__ = {"schema": "config"} 

    id = Column(Integer, primary_key=True, index=True)
    operator_id = Column(Integer, index=True)
    

# Filters Table
class Filters(Base):
    __tablename__ = 'filter'
    __table_args__ = {"schema": "config"} 

    id = Column(Integer, primary_key=True, index=True)
    expression_id = Column(Integer, index=True)
    


# Lookups Table
class Lookups(Base):
    __tablename__ = 'lookup'
    __table_args__ = {"schema": "config"} 

    id = Column(Integer, primary_key=True, index=True)
    lookup_name = Column(String, index=True)
    parent_lookup_id = Column(Integer, index=True)
    is_deleted = Column(Boolean)
    created_on = Column(TIMESTAMP, server_default=func.now(), index=True)
    updated_on = Column(TIMESTAMP, server_default=func.now(), index=True)
    lookup_desc = Column(String, index=True)



# Operators Table
class Operators(Base):
    __tablename__ = 'operator'
    __table_args__ = {"schema": "config"} 

    id = Column(Integer, primary_key=True, index=True)
    operator_name = Column(String, index=True)
    is_sql_operator = Column(Boolean)


# Source Field Separators Table
class SourceFieldSeparators(Base):
    __tablename__ = 'source_field_separator'
    __table_args__ = {"schema": "config"} 

    id = Column(Integer, primary_key=True, index=True)
    source_field_id = Column(Integer, index=True)
    sub_field_separator = Column(String, nullable=True)
    sub_field_number = Column(Integer, index=True)
    multi_value_separator = Column(String, nullable=True)


