# from fastapi import FastAPI, Depends , HTTPException
# from sqlalchemy.orm import Session
# from app import models, schemas, database
# from typing import List



# app = FastAPI()

# # Dependency
# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/configs", response_model=List[schemas.Config])
# def get_configs(db: Session = Depends(get_db)):
#     try:
#         configs = db.query(models.Config).all()
#         return configs
#     except Exception as e:
#         # Log the error or print the error message
#         raise HTTPException(status_code=500, detail=str(e))

# # Create routes for other configurations similarly

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from typing import List

app = FastAPI()

# Dependency to get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Config Endpoints
@app.get("/configs", response_model=List[schemas.Config])
def get_configs(db: Session = Depends(get_db)):
    try:
        return db.query(models.Config).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Custom Field Group Endpoints
@app.get("/custom_field_groups", response_model=List[schemas.CustomFieldGroup])
def get_custom_field_groups(db: Session = Depends(get_db)):
    try:
        return db.query(models.CustomFieldGroup).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Dynamic Item Form Field Endpoints
@app.get("/dynamic_item_form_fields", response_model=List[schemas.DynamicItemFormField])
def get_dynamic_item_form_fields(db: Session = Depends(get_db)):
    try:
        return db.query(models.DynamicItemFormField).all()
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# Expressions Endpoints
@app.get("/expressions", response_model=List[schemas.Expressions])
def get_expressions(db: Session = Depends(get_db)):
    try:
        return db.query(models.Expressions).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Filters Endpoints
@app.get("/filters", response_model=List[schemas.Filters])
def get_filters(db: Session = Depends(get_db)):
    try:
        return db.query(models.Filters).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Lookups Endpoints
@app.get("/lookups", response_model=List[schemas.Lookups])
def get_lookups(db: Session = Depends(get_db)):
    try:
        return db.query(models.Lookups).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Operators Endpoints
@app.get("/operators", response_model=List[schemas.Operators])
def get_operators(db: Session = Depends(get_db)):
    try:
        return db.query(models.Operators).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Source Field Separators Endpoints
@app.get("/source_field_separators", response_model=List[schemas.SourceFieldSeparators])
def get_source_field_separators(db: Session = Depends(get_db)):
    try:
        return db.query(models.SourceFieldSeparators).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
