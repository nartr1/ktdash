import uvicorn
from fastapi import FastAPI, APIRouter
from models.settings import Settings
from routes.authentication import authentication_router
from routes.killteams import killteams_router
from routes.rosters import rosters_router
from routes.session import sessions_router
from routes.user import user_router
from models.settings import SETTINGS

app = FastAPI()
base_router = APIRouter()

app.include_router(base_router)
app.include_router(authentication_router)
app.include_router(killteams_router)
app.include_router(rosters_router)
app.include_router(sessions_router)
app.include_router(user_router)

@base_router.get("/")  # When someone goes to / on the server, execute the following function
def home():
    return "Hello, World!"  # Return this message back to the browser

if (
    __name__ == "__main__"
):  # If the script that was run is this script (we have not been imported)
    uvicorn.run(
        "run:app",
        host=SETTINGS.host,
        port=SETTINGS.port,
        reload=SETTINGS.hot_reload,
    )  # Start the server
