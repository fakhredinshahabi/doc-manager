import secrets
from typing import Annotated

from fastapi import APIRouter, Cookie, Form, Response

from app.deps import SessionsDep, SettingsDep

router = APIRouter(prefix="/session", tags=["session"])


@router.post("/login")
def login(response: Response, sessions: SessionsDep, settings: SettingsDep,
          username: Annotated[str, Form(min_length=1, max_length=50)]):
    token = secrets.token_urlsafe(32)
    sessions[token] = username
    response.set_cookie("session_id", token, httponly=True, samesite="lax",
                        max_age=settings.session_max_age)
    return {"message": f"خوش آمدی {username}"}


@router.get("/me")
def me(sessions: SessionsDep,
       session_id: Annotated[str | None, Cookie()] = None):
    username = sessions.get(session_id) if session_id else None
    return {"logged_in": username is not None, "username": username}


@router.post("/logout")
def logout(response: Response, sessions: SessionsDep,
           session_id: Annotated[str | None, Cookie()] = None):
    sessions.pop(session_id, None)
    response.delete_cookie("session_id")
    return {"logged_out": True}