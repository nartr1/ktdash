from datetime import timedelta
from typing import Annotated

from api.user.session import TokenManager
from api.user.user import User
from db.engine import SessionDep
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.settings import SETTINGS
from models.user import Token

authentication_router = APIRouter(prefix="/api/auth")


@authentication_router.post("/token")
def login_for_access_token(
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = User.authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=SETTINGS.access_token_expire_minutes)
    access_token = TokenManager.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@authentication_router.post("/register")
def register(
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    # Check if the user already exists
    user = User.get_user(form_data.username, session)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )
    User.create_user(form_data.username, form_data.password, session)

    access_token_expires = timedelta(minutes=SETTINGS.access_token_expire_minutes)
    access_token = TokenManager.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
