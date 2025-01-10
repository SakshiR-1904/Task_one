from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema for Config
class ConfigBase(BaseModel):
    key: str
    value: str
    is_deleted: Optional[bool] = False    
    config_desc: Optional[str] = None
    config_group_id: Optional[int] = None

# Schema for creating Config
class ConfigCreate(ConfigBase):
    pass

# Schema for returning Config data (with ID)
class Config(ConfigBase):
    id: int

    class Config:
        orm_mode = True


# Base schema for CustomFieldGroup
class CustomFieldGroupBase(BaseModel):
    custom_field_group_code: str
    custom_field_group_desc: Optional[str] = None
    lookup_id: Optional[int] = None

# Schema for creating CustomFieldGroup
class CustomFieldGroupCreate(CustomFieldGroupBase):
    pass

# Schema for returning CustomFieldGroup data (with ID)
class CustomFieldGroup(CustomFieldGroupBase):
    id: int

    class Config:
        orm_mode = True


# Base schema for DynamicItemFormField
class DynamicItemFormFieldBase(BaseModel):
    form_field_name: str  # Renamed from field_name
    form_field_label: Optional[str] = None  # Changed from form_field_label
    template_id: Optional[int] = None
    group_id: Optional[int] = None
    control_type: Optional[str] = None

# Schema for creating DynamicItemFormField
class DynamicItemFormFieldCreate(DynamicItemFormFieldBase):
    pass

# Schema for returning DynamicItemFormField data (with ID)
class DynamicItemFormField(DynamicItemFormFieldBase):
    id: int

    class Config:
        orm_mode = True


# Base schema for Expressions
class ExpressionsBase(BaseModel):
    operator_id: Optional[int] = None

# Schema for creating Expressions
class ExpressionsCreate(ExpressionsBase):
    pass

# Schema for returning Expressions data (with ID)
class Expressions(ExpressionsBase):
    id: int

    class Config:
        orm_mode = True


# Base schema for Filters
class FiltersBase(BaseModel):
    expression_id: Optional[int] = None
    

# Schema for creating Filters
class FiltersCreate(FiltersBase):
    pass

# Schema for returning Filters data (with ID)
class Filters(FiltersBase):
    id: int

    class Config:
        orm_mode = True


# Base schema for Lookups
class LookupsBase(BaseModel):
    lookup_name:  Optional[str] = None
    parent_lookup_id: Optional[int] = None
    is_deleted: Optional[bool] = False
    lookup_desc: Optional[str] = None
    created_on: Optional[datetime] = None
    updated_on: Optional[datetime] = None


# Schema for creating Lookups
class LookupsCreate(LookupsBase):
    pass

# Schema for returning Lookups data (with ID)
class Lookups(LookupsBase):
    id: int

    class Config:
        orm_mode = True


# Base schema for Operators
class OperatorsBase(BaseModel):
    operator_name: str
    is_sql_operator: Optional[bool] = None

# Schema for creating Operators
class OperatorsCreate(OperatorsBase):
    pass

# Schema for returning Operators data (with ID)
class Operators(OperatorsBase):
    id: int

    class Config:
        orm_mode = True


# Base schema for SourceFieldSeparators
class SourceFieldSeparatorsBase(BaseModel):
    source_field_id: Optional[int] = None
    sub_field_separator: Optional[str] = None
    sub_field_number: Optional[int] = None
    multi_value_separator : Optional[str] = None

# Schema for creating SourceFieldSeparators
class SourceFieldSeparatorsCreate(SourceFieldSeparatorsBase):
    pass

# Schema for returning SourceFieldSeparators data (with ID)
class SourceFieldSeparators(SourceFieldSeparatorsBase):
    id: int

    class Config:
        orm_mode = True
