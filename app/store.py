# from fastapi import HTTPException
# from app.schemas import CreateDocument
# DOCS = [
#     {
#         "id": 1, "title": "شرایط گارانتی محصولات",
#         "text": "تمامی محصولات شرکت دارای ۱۸ ماه گارانتی بی‌قید و شرط تعویض هستند.",
#         "category": "policy", "tags": ["گارانتی", "تعویض"],
#         "password": "Test123!@"
#     },
#     {
#         "id": 2, "title": "مهلت مرجوعی کالا",
#         "text": "مشتریان گرامی می‌توانند تا ۷ روز کاری پس از تحویل کالا، درخواست مرجوعی ثبت کنند.",
#         "category": "policy", "tags": ["مرجوعی", "بازگشت وجه"],
#         "password": "Secure456#"
#     },
#     {
#         "id": 3, "title": "ساعت کاری و تعطیلات رسمی",
#         "text": "ساعت کاری شرکت از شنبه تا چهارشنبه از ساعت ۹:۰۰ صبح الی ۱۷:۰۰ عصر می‌باشد.",
#         "category": "faq", "tags": ["ساعت کاری", "تعطیلات"],
#         "password": "Work789$"
#     },
#     {
#         "id": 4, "title": "آیین‌نامه مرخصی استحقاقی",
#         "text": "هر کارمند به ازای هر سال کارکرد کامل، ۲۶ روز مرخصی استحقاقی با حقوق دارد.",
#         "category": "policy", "tags": ["منابع انسانی", "مرخصی"],
#         "password": "Leave123!"
#     },
#     {
#         "id": 5, "title": "قوانین مرخصی استعلاجی",
#         "text": "در صورت بیماری، کارمند موظف است حداکثر تا ۴۸ ساعت اطلاع‌رسانی کند.",
#         "category": "policy", "tags": ["منابع انسانی", "بیماری", "مرخصی"],
#         "password": "Sick456@"
#     },
#     {
#         "id": 6, "title": "قوانین نحوه درخواست مساعده حقوق",
#         "text": "درخواست مساعده فقط تا سقف ۳۰ درصد از حقوق پایه‌ی ماهانه قابل ثبت است.",
#         "category": "faq", "tags": ["مالی", "مساعده", "حقوق"],
#         "password": "Money789#"
#     },
#     {
#         "id": 7, "title": "قوانین سیاست‌های استفاده از اینترنت شرکت",
#         "text": "دسترسی به اینترنت شرکت صرفاً برای امور کاری مجاز است.",
#         "category": "policy", "tags": ["فناوری اطلاعات", "امنیت", "اینترنت"],
#         "password": "Net123!@"
#     },
#     {
#         "id": 8, "title": "راهنمای نصب نرم‌افزارهای داخلی",
#         "text": "برای نصب نرم‌افزار اتوماسیون اداری، آخرین نسخه را از پرتال داخلی دانلود کنید.",
#         "category": "manual", "tags": ["فناوری اطلاعات", "نرم‌افزار", "راهنما"],
#         "password": "Soft456#"
#     },
#     {
#         "id": 9, "title": "فرآیند مصاحبه و استخدام",
#         "text": "فرآیند استخدام شامل سه مرحله است: بررسی رزومه، مصاحبه و استعلام سوابق.",
#         "category": "manual", "tags": ["منابع انسانی", "استخدام"],
#         "password": "Hire789$"
#     },
#     {
#         "id": 10, "title": "آیین‌نامه انضباطی کارکنان",
#         "text": "هرگونه تأخیر بیش از ۱۵ دقیقه در ورود، بدون اطلاع‌رسانی، غیبت ثبت می‌شود.",
#         "category": "policy", "tags": ["منابع انسانی", "انضباط"],
#         "password": "Rule123!"
#     },
#     {
#         "id": 11, "title": "نحوه ثبت درخواست مأموریت",
#         "text": "مأموریت‌های کاری باید از طریق فرم الکترونیکی و با تأیید مدیر ثبت شوند.",
#         "category": "faq", "tags": ["مالی", "مأموریت"],
#         "password": "Trip456@"
#     },
#     {
#         "id": 12, "title": "پوشش‌های بیمه‌ی تکمیلی درمان",
#         "text": "بیمه‌ی تکمیلی شامل هزینه‌های دندانپزشکی، عینک، ویزیت و دارو می‌شود.",
#         "category": "faq", "tags": ["منابع انسانی", "بیمه", "درمان"],
#         "password": "Health789#"
#     },
#     {
#         "id": 13, "title": "راهنمای استفاده از دستگاه‌های اداری",
#         "text": "برای استفاده از دستگاه کپی، کارت پرسنلی خود را روی حسگر قرار دهید.",
#         "category": "manual", "tags": ["پشتیبانی", "تجهیزات اداری"],
#         "password": "Copy123!@"
#     },
#     {
#         "id": 14, "title": "سیاست‌ها و شرایط دورکاری",
#         "text": "دورکاری فقط با موافقت کتبی مدیر و حداکثر ۲ روز در هفته مجاز است.",
#         "category": "policy", "tags": ["منابع انسانی", "دورکاری"],
#         "password": "Home456#"
#     },
#     {
#         "id": 15, "title": "فرآیند ارزیابی عملکرد سالانه",
#         "text": "ارزیابی عملکرد بر اساس KPI، نظم و بازخورد ۳۶۰ درجه صورت می‌گیرد.",
#         "category": "manual", "tags": ["منابع انسانی", "ارزیابی عملکرد"],
#         "password": "Rate789$"
#     },
#     {
#         "id": 16, "title": "دستورالعمل حفظ محرمانگی اطلاعات",
#         "text": "کلیه‌ی اسناد و اطلاعات مشتریان محرمانه تلقی می‌شوند.",
#         "category": "policy", "tags": ["امنیت", "محرمانگی", "حقوقی"],
#         "password": "Secret123!"
#     },
#     {
#         "id": 17, "title": "نحوه‌ی درخواست تجهیزات اداری",
#         "text": "برای درخواست لوازم التحریر، فرم درخواست کالا را پر کنید.",
#         "category": "faq", "tags": ["پشتیبانی", "تدارکات"],
#         "password": "Supply456@"
#     },
#     {
#         "id": 18, "title": "آیین‌نامه پرداخت پاداش و کارانه",
#         "text": "پاداش فصلی بر اساس سودآوری و نمره ارزیابی محاسبه می‌شود.",
#         "category": "policy", "tags": ["مالی", "پاداش", "حقوق"],
#         "password": "Bonus789#"
#     },
#     {
#         "id": 19, "title": "راهنمای ثبت‌نام در سامانه‌ی رفاهی",
#         "text": "با کد ملی و شماره موبایل ثبت‌نام کنید. رمز اولیه پیامک می‌شود.",
#         "category": "manual", "tags": ["فناوری اطلاعات", "سامانه رفاهی"],
#         "password": "Welfare123!@"
#     },
#     {
#         "id": 20, "title": "قوانین تردد و پارکینگ خودرو",
#         "text": "استفاده از پارکینگ فقط برای خودروهای ثبت‌شده مجاز است.",
#         "category": "faq", "tags": ["حراست", "پارکینگ", "تردد"],
#         "password": "Parking456#"
#     }
# ]
# def find_doc_by_id(doc_id: int):
#     for doc in DOCS:
#         if doc["id"] == doc_id:
#             return doc
#     raise HTTPException(status_code=404,detail="Not Found")
# def create_new_id():
#       new_id=max((doc["id"] for doc in DOCS),default=0 )+1
#       return new_id
#
# def add(body:CreateDocument):
#     new_id=create_new_id()
#     DOCS.append({
#         "id":new_id,
#         **body.model_dump()
#     })
# def remove(id:int):
#     doc=find_doc_by_id(id)
#     DOCS.remove(doc)
import pathlib
# import pathlib
# class DocumentsStore:
#     def __init__(self, upload_dir: pathlib.Path):
#         self.upload_dir = upload_dir
#         self.docs: list[dict] = [
#             {
#                 "id": 1, "title": "شرایط گارانتی محصولات",
#                 "text": "تمامی محصولات شرکت دارای ۱۸ ماه گارانتی بی‌قید و شرط تعویض هستند.",
#                 "category": "policy", "tags": ["گارانتی", "تعویض"],
#                 "password": "Test123!@"
#             },
#             # ... بقیه‌ی اسناد (۲ تا ۲۰)
#         ]
#
#     def get(self, doc_id: int) -> dict | None:
#         return next((d for d in self.docs if d["id"] == doc_id), None)
#
#     def next_id(self) -> int:
#         return max((d["id"] for d in self.docs), default=0) + 1
#
#     def add(self, doc: dict) -> dict:
#         self.docs.append(doc)
#         return doc
#
#     def remove(self, doc: dict) -> None:
#         self.docs.remove(doc)
#
#     def file_path(self, doc_id: int) -> pathlib.Path:
#         return self.upload_dir / f"{doc_id}.txt"
import pathlib


class DocumentStore:
    def __init__(self, upload_dir: pathlib.Path):
        self.upload_dir = upload_dir
        self.docs: list[dict] = [
            {"id": 1, "title": "شرایط گارانتی", "text": "گارانتی ۱۸ ماه است."},
            {"id": 2, "title": "مهلت مرجوعی", "text": "مرجوعی تا ۷ روز ممکن است."},
            {"id": 3, "title": "ساعت کاری", "text": "شنبه تا چهارشنبه ۹ تا ۱۷."},
        ]

    def get(self, doc_id: int) -> dict | None:
        return next((d for d in self.docs if d["id"] == doc_id), None)

    def next_id(self) -> int:
        return max((d["id"] for d in self.docs), default=0) + 1

    def add(self, doc: dict) -> dict:
        self.docs.append(doc)
        return doc

    def remove(self, doc: dict) -> None:
        self.docs.remove(doc)

    def file_path(self, doc_id: int) -> pathlib.Path:
        return self.upload_dir / f"{doc_id}.txt"