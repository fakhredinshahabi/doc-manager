from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, Query, UploadFile
from fastapi.responses import FileResponse
from app.deps import DocDep, SettingsDep, StoreDep, require_api_key
from app.schemas import Category, DocumentCreate, DocumentOut, DocumentUpdate

router = APIRouter(prefix="/documents", tags=["documents"])

protected = [Depends(require_api_key)]


@router.get("/count")
def count_documents(store: StoreDep):
    return {"count": len(store.docs)}


@router.get("", response_model=list[DocumentOut])
def list_documents(
    store: StoreDep,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=50)] = 10,
    search: Annotated[str | None, Query(max_length=100)] = None,
    in_text: bool = False,
):
    items = store.docs
    if search:
        items = [d for d in items
                 if search in d["title"] or (in_text and search in d["text"])]
    return items[skip : skip + limit]


@router.post("", status_code=201, response_model=DocumentOut,
             dependencies=protected)
def create_document(body: DocumentCreate, store: StoreDep):
    return store.add({"id": store.next_id(), **body.model_dump()})


@router.post("/upload", status_code=201, response_model=DocumentOut,
             dependencies=protected)
def upload_document(
    title: Annotated[str, Form(min_length=3, max_length=100)],
    file: UploadFile,
    store: StoreDep,
    settings: SettingsDep,
    category: Annotated[Category, Form()] = Category.faq,
):
    if not (file.filename or "").lower().endswith(".txt"):
        raise HTTPException(400, "فقط فایل .txt مجاز است")
    limit = settings.max_upload_bytes
    raw = file.file.read(limit + 1)
    if len(raw) > limit:
        raise HTTPException(413, "فایل از سقف مجاز بزرگ‌تر است")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise HTTPException(400, "فایل باید UTF-8 باشد")
    if not text.strip():
        raise HTTPException(400, "فایل بدون محتوا است")
    new_id = store.next_id()
    store.file_path(new_id).write_text(text, encoding="utf-8")
    return store.add({"id": new_id, "title": title.strip(), "text": text,
                      "category": category, "tags": []})


@router.get("/{doc_id}", response_model=DocumentOut)
def get_document(doc: DocDep):
    return doc


@router.patch("/{doc_id}", response_model=DocumentOut,
              dependencies=protected)
def update_document(doc: DocDep, body: DocumentUpdate):
    doc.update(body.model_dump(exclude_unset=True))
    return doc


@router.delete("/{doc_id}", status_code=204, dependencies=protected)
def delete_document(doc: DocDep, store: StoreDep):
    store.remove(doc)


@router.get("/{doc_id}/download")
def download_document(doc: DocDep, store: StoreDep):
    path = store.file_path(doc["id"])
    if not path.exists():
        raise HTTPException(404, "فایلی برای این سند نیست")
    return FileResponse(path, media_type="text/plain",
                        filename=f"document-{doc['id']}.txt")
