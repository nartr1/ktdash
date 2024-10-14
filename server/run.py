from collections import defaultdict

import uvicorn
from fastapi import APIRouter, FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from models.settings import SETTINGS
from routes.authentication import authentication_router
from routes.killteams import killteams_router
from routes.rosters import rosters_router
from routes.user import user_router

app = FastAPI()
base_router = APIRouter()

app.include_router(base_router)
app.include_router(authentication_router)
app.include_router(killteams_router)
app.include_router(rosters_router)
app.include_router(user_router)


@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request, exc):
    reformatted_message = defaultdict(list)
    for pydantic_error in exc.errors():
        loc, msg = pydantic_error["loc"], pydantic_error["msg"]
        filtered_loc = list(loc[1:] if loc[0] in ("body", "query", "path") else loc)
        field_string = ".".join(
            [str(x) for x in filtered_loc]
        )  # nested fields with dot-notation
        reformatted_message[field_string].append(msg)

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {"detail": "Invalid request", "errors": reformatted_message}
        ),
    )


@base_router.get(
    "/"
)  # When someone goes to / on the server, execute the following function
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
