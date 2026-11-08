import logging
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

log = logging.getLogger("app.errors")

HTTP_CODES = {400: "bad_request", 401: "unauthorized", 403: "forbidden",
              404: "not_found", 413: "payload_too_large",
              429: "too_many_requests"}


class AppError(Exception):
    status_code = 500
    code = "internal_error"
    message = "خطای داخلی سرور"

    def __init__(self, message: str | None = None,
                 headers: dict | None = None):
        super().__init__(message or self.message)
        if message:
            self.message = message
        self.headers = headers


class DocumentNotFound(AppError):
    status_code = 404
    code = "document_not_found"
    message = "سند پیدا نشد"


class Unauthorized(AppError):
    status_code = 401
    code = "unauthorized"
    message = "کلید API نامعتبر است یا ارسال نشده است"


class TooManyRequests(AppError):
    status_code = 429
    code = "too_many_requests"
    message = "تعداد درخواست‌ها زیاد است؛ کمی بعد دوباره تلاش کن"


def error_body(request: Request, code: str, message: str, details=None):
    err = {"code": code, "message": message,
           "request_id": getattr(request.state, "request_id", None)}
    if details is not None:
        err["details"] = details
    return {"error": err}


def register_error_handlers(app: FastAPI):
    @app.exception_handler(AppError)
    async def handle_app_error(request: Request, exc: AppError):
        return JSONResponse(
            status_code=exc.status_code, headers=exc.headers,
            content=error_body(request, exc.code, exc.message))

    @app.exception_handler(RequestValidationError)
    async def handle_validation(request: Request,
                                exc: RequestValidationError):
        return JSONResponse(status_code=422, content=error_body(
            request, "validation_error", "ورودی نامعتبر است",
            jsonable_encoder(exc.errors())))

    @app.exception_handler(StarletteHTTPException)
    async def handle_http(request: Request, exc: StarletteHTTPException):
        code = HTTP_CODES.get(exc.status_code, "http_error")
        return JSONResponse(
            status_code=exc.status_code, headers=exc.headers,
            content=error_body(request, code, str(exc.detail)))

    @app.exception_handler(Exception)
    async def handle_unexpected(request: Request, exc: Exception):
        log.exception("unhandled error on %s", request.url.path)
        return JSONResponse(status_code=500, content=error_body(
            request, "internal_error", "خطای داخلی سرور"))