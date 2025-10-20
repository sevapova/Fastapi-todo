from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.users import router as users_router
from app.routers.tasks import router as tasks_router

app = FastAPI(
    title="Todo API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(tasks_router)
