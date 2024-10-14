from sqlmodel import select
from db.schema import User as UserDB
from models.user import TokenData
from api.user.session import TokenManager
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from typing import Annotated
import jwt

from db.engine import SessionDep
from models.settings import SETTINGS

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


class User:
    def __init__(self):
        pass

    @staticmethod
    def create_user(userid, password, session):
        # Create a new user in the database
        user = UserDB(userid=userid, passhash=TokenManager.get_password_hash(password))

        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def get_user(userid, session):
        # Return the user with the given ID
        query = select(UserDB).where(UserDB.userid == userid)
        user_row = session.exec(query).all()
        if user_row is None or len(user_row) == 0:
            return None
        return user_row[0]

    @staticmethod
    def authenticate_user(userid: str, password: str, session):
        user = User.get_user(userid, session)
        if not user:
            return False
        if not TokenManager.verify_password(password, user.passhash):
            return False
        return user


def get_current_user(
    session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, SETTINGS.secret_key, algorithms=[SETTINGS.algorithm]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(userid=username)
    except InvalidTokenError as exc:
        raise credentials_exception from exc
    user = User.get_user(token_data.userid, session)
    if user is None:
        raise credentials_exception
    return user, session
