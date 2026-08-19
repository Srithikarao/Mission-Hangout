import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    print(
        f"[BACKEND] "
        f"{request.method} "
        f"{request.url.path} "
        f"-> {response.status_code} "
        f"({process_time:.3f}s)"
    )

    return response










from fastapi import FastAPI

from backend.routers.food import router as food_router
from backend.routers.chill import router as chill_router
from backend.routers.events import router as events_router
from backend.routers.family import router as family_router
from backend.routers.friends import router as friends_router

app = FastAPI(
    title="Warangal Hangout API",
    version="1.0.0"
)

app.include_router(food_router)
app.include_router(chill_router)
app.include_router(events_router) 
app.include_router(family_router)
app.include_router(friends_router)


@app.get("/")
def home():

    return {
        "message":"Welcome to Warangal Hangout Recommendation API"
    } 
