# from enum import Enum
# from pydantic import BaseModel, Field, field_validator
# import re
#
# class Category(str,Enum):
#     policy="policy"
#     faq="faq"
#     manually= "manual"
# class CreateDocument(BaseModel):
#     title: str = Field()
#     text:str=Field()
#     category:Category|None=None
#     tags:list[str]=Field()
#     password:str=Field()
#     @field_validator("password")
#     @classmethod
#     def check_password(cls,password):
#         if not  password.isascii():
#             raise ValueError("Password must English")
#         if not password.strip():
#             raise ValueError("Password cannot be empty")
#         if len(password) < 8:
#             raise ValueError("Password should not be longer than 8 characters")
#         if not re.search(r"[a-z]",password) :
#             raise ValueError("password must contain Lowercase letters")
#         if not re.search(r"[A-Z]", password):
#             raise ValueError("password must contain Uppercase letters ")
#         if not re.search(r"[^a-zA-Z0-9]", password):
#             raise ValueError("password must contain carcter letters ")
#         return password
#
#
#
#
# class CreateDocumentOut(BaseModel):
#     id: int
#     title: str
#     text: str
#     category: Category
#     tags: list[str] | None = None
#
# class UpdateDocument(BaseModel):
#     title: str | None = Field(default=None)
#     text: str|None = Field(default=None)
#     category: Category|None = Field(default=None)
#     tags: list[str]|None = Field(default=None)
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class Category(str, Enum):
    policy = "policy"
    faq = "faq"
    manual = "manual"


class DocumentCreate(BaseModel):
    title: str = Field(max_length=100)
    text: str = Field(min_length=1)
    category: Category = Category.faq
    tags: list[str] = []

    @field_validator("title")
    @classmethod
    def clean_title(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 3:
            raise ValueError("عنوان باید حداقل ۳ حرف معنادار باشد")
        return v


class DocumentUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    text: str | None = Field(default=None, min_length=1)
    category: Category | None = None


class DocumentOut(BaseModel):
    id: int
    title: str
    text: str
    category: Category = Category.faq
    tags: list[str] = []