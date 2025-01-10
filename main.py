from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router  # Ensure correct import

app = FastAPI()

# CORS Configuration
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register router
app.include_router(router)

# Debug: Print all registered routes
@app.on_event("startup")
async def startup_event():
    print("Registered Routes:")
    for route in app.routes:
        print(route.path, route.methods)
