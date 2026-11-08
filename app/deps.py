import secrets
import time
from collections import deque
from typing import Annotated
import httpx
from fastapi import Depends, Path, Request, Security
from fastapi.security import APIKeyHeader
from app.config import Settings, get_settings
from app.errors import DocumentNotFound, TooManyRequests, Unauthorized
from app.store import DocumentStore


def get_store(request: Request) -> DocumentStore:
    return request.app.state.store


def get_sessions(request: Request) -> dict[str, str]:
    return request.app.state.sessions


def get_http(request: Request) -> httpx.AsyncClient:
    return request.app.state.http


SettingsDep = Annotated[Settings, Depends(get_settings)]
StoreDep = Annotated[DocumentStore, Depends(get_store)]
SessionsDep = Annotated[dict[str, str], Depends(get_sessions)]
HttpDep = Annotated[httpx.AsyncClient, Depends(get_http)]


def get_doc(doc_id: Annotated[int, Path(ge=1)], store: StoreDep) -> dict:
    doc = store.get(doc_id)
    if doc is None:
        raise DocumentNotFound()
    return doc


DocDep = Annotated[dict, Depends(get_doc)]


api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def require_api_key(
    settings: SettingsDep,
    key: Annotated[str | None, Security(api_key_header)],
) -> None:
    ok = key is not None and secrets.compare_digest(
        key.encode(), settings.api_key.encode())
    if not ok:
        raise Unauthorized()


async def rate_limit(request: Request, settings: SettingsDep) -> None:
    ip = request.client.host if request.client else "unknown"
    bucket = request.app.state.rate_buckets.setdefault(ip, deque())
    now = time.monotonic()
    while bucket and now - bucket[0] > 60:
        bucket.popleft()
    if len(bucket) >= settings.rate_limit_per_minute:
        raise TooManyRequests(headers={"Retry-After": "60"})
    bucket.append(now)