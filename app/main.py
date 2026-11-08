import logging
import time
import uuid
from contextlib import asynccontextmanager
import httpx
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.config import BASE_DIR, get_settings
from app.deps import rate_limit
from app.errors import register_error_handlers
from app.routers import documents, misc, session
from app.store import DocumentStore

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s")
access_log = logging.getLogger("app.access")

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    upload_dir = BASE_DIR / settings.upload_dir
    upload_dir.mkdir(exist_ok=True)
    app.state.store = DocumentStore(upload_dir)
    app.state.sessions = {}
    app.state.rate_buckets = {}  # 🆕
    app.state.http = httpx.AsyncClient(timeout=10)
    yield
    await app.state.http.aclose()

app = FastAPI(title=settings.app_name, version="0.6.0", lifespan=lifespan,
              dependencies=[Depends(rate_limit)])  # 🆕

register_error_handlers(app)  # 🆕

@app.middleware("http")  # 🆕
async def request_context(request: Request, call_next):
    request_id = request.headers.get("x-request-id") or uuid.uuid4().hex[:12]
    request.state.request_id = request_id
    start = time.perf_counter()
    try:
        response = await call_next(request)
    except Exception:
        access_log.exception("%s %s crashed id=%s",
                             request.method, request.url.path, request_id)
        raise
    ms = (time.perf_counter() - start) * 1000
    response.headers["X-Request-ID"] = request_id
    access_log.info("%s %s -> %s (%.0f ms) id=%s", request.method,
                    request.url.path, response.status_code, ms, request_id)
    return response

app.add_middleware(  # 🆕
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Request-ID"],
)

app.include_router(misc.router)
app.include_router(documents.router)
app.include_router(session.router)