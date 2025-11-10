import os
import tempfile
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI

load_dotenv()

app = FastAPI(title="Wispr Flow Clone", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_client: Optional[OpenAI] = None


def get_openai_client() -> OpenAI:
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured")
        _client = OpenAI(api_key=api_key)
    return _client


@app.get("/health")
async def healthcheck() -> dict:
    return {"status": "ok"}


@app.post("/api/transcribe-chunk")
async def transcribe_chunk(
    audio: UploadFile = File(...),
    language: Optional[str] = Form(None),
    chunk_id: Optional[str] = Form(None),
) -> JSONResponse:
    try:
        client = get_openai_client()
    except RuntimeError as exc:  # pragma: no cover - fail fast for missing env vars
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    contents = await audio.read()
    if not contents:
        raise HTTPException(status_code=400, detail="Received empty audio chunk")

    suffix = os.path.splitext(audio.filename or "chunk.webm")[-1] or ".webm"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(contents)
        tmp_path = tmp_file.name

    try:
        with open(tmp_path, "rb") as fh:
            transcription = client.audio.transcriptions.create(
                model=os.getenv("WHISPER_MODEL", "whisper-1"),
                file=fh,
                language=language or None,
                response_format="json",
                temperature=0.0,
            )
    except Exception as exc:  # pragma: no cover - surface upstream failure
        raise HTTPException(status_code=502, detail=f"Transcription failed: {exc}") from exc
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass

    payload = {"text": transcription.text.strip(), "chunkId": chunk_id}
    return JSONResponse(content=payload)


@app.get("/api/config")
async def get_config() -> dict:
    """Expose minimal config so the UI can adapt."""
    return {"languageOptions": ["auto", "en", "zh"]}


FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
if FRONTEND_DIR.exists():
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
