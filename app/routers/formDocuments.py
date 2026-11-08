# import pathlib
# from typing import Annotated
# from app.schemas import Category
# from app.store import create_new_id,DOCS
# from pydantic import AfterValidator, validators
# import re
# from fastapi import Form,UploadFile,APIRouter,HTTPException
# router=APIRouter(prefix='/ecoupload',tags=['ecoupload'])
# def check_Password(password:str):
#     password=password.strip()
#     if not password:
#         raise validators('Password cannot be empty')
#     if not password.isascii():
#         raise ValueError("Password must English")
#     if not password.strip():
#         raise ValueError("Password cannot be empty")
#     if len(password) < 8:
#         raise ValueError("Password should not be longer than 8 characters")
#     if not re.search(r"[a-z]", password):
#         raise ValueError("password must contain Lowercase letters")
#     if not re.search(r"[A-Z]", password):
#         raise ValueError("password must contain Uppercase letters ")
#     if not re.search(r"[^a-zA-Z0-9]", password):
#         raise ValueError("password must contain carcter letters ")
#     return password
#
#
#
# @router.patch('')
# def upload_eco_form(
#         title:Annotated[str,Form()],
#         text:Annotated[str,Form()],
#         category:Annotated[Category,Form()],
#         tags:Annotated[list[str],Form()],
#         password:Annotated[str,Form(),AfterValidator(check_Password)]
#
# ):
#     return {"title":title,"text":text,"category":category,"tags":tags,password:password}
# @router.post('/upload_file')
# def upload_file(file:UploadFile):
#     MAX_BYTES=1_000_000
#     raw = file.file.read(MAX_BYTES + 1)
#     file_contex=file.file.read(MAX_BYTES+1)
#     if not (file.filename or "").lower().endswith(".txt"):
#         raise HTTPException(400, "فقط فایل .txt مجاز است")
#     if not file_contex.strip():
#         raise HTTPException("File cannot be empty")
#     if len(file_contex) > MAX_BYTES:
#         raise HTTPException("File too large")
#     try:
#         text = raw.decode("utf-8-sig")
#     except UnicodeDecodeError:
#         raise HTTPException(400, "فایل باید UTF-8 باشد")
#
# UPLOAD_DIR = pathlib.Path(__file__).resolve().parent.parent / "uploads"
# UPLOAD_DIR.mkdir(exist_ok=True)
# @router.post('/upload_file_form')
# def upload_file_form(
#         title:Annotated[str,Form()],
#         category:Annotated[Category,Form()],
#         tags:Annotated[list[str],Form()],
#         password:Annotated[str,Form(),AfterValidator(check_Password)],
#         file:UploadFile
#
# ):
#     MAX_BYTES = 1_000_000
#     raw = file.file.read(MAX_BYTES + 1)
#     file_contex = file.file.read(MAX_BYTES + 1)
#     if not (file.filename or "").lower().endswith(".txt"):
#         raise HTTPException(400, "فقط فایل .txt مجاز است")
#     if not file_contex.strip():
#         raise HTTPException("File cannot be empty")
#     if len(file_contex) > MAX_BYTES:
#         raise HTTPException("File too large")
#     try:
#         text = raw.decode("utf-8-sig")
#     except UnicodeDecodeError:
#         raise HTTPException(400, "فایل باید UTF-8 باشد")
#     new_id=create_new_id()
#     (UPLOAD_DIR / f"{new_id}.txt").write_text(text, encoding="utf-8")
#     doc = {"id": new_id, "title": title.strip(), "text": text,
#            "category": category, "tags":tags,"password":password}
#     DOCS.append(doc)
#     return doc