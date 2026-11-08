from typing import Annotated, Literal

from fastapi import APIRouter, Cookie, Form, Header, Response

router = APIRouter(tags=["misc"])


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/whoami")
def whoami(
    user_agent: Annotated[str | None, Header()] = None,
    x_request_id: Annotated[str | None, Header()] = None,
):
    return {"user_agent": user_agent, "x_request_id": x_request_id}


@router.post("/prefs")
def set_prefs(lang: Annotated[Literal["fa", "en"], Form()],
              response: Response):
    response.set_cookie("lang", lang, httponly=True, samesite="lax",
                        max_age=60 * 60 * 24 * 30)
    return {"saved": lang}


@router.get("/prefs")
def get_prefs(lang: Annotated[str | None, Cookie()] = None):
    return {"lang": lang or "fa"}