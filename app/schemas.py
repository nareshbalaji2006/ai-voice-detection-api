from pydantic import BaseModel


class VoiceDetectionRequest(BaseModel):
    audio_file: str
    language: str
    model: str


class VoiceDetectionResponse(BaseModel):
    transcription: str
    confidence: float
    duration: float


class HealthResponse(BaseModel):
    status: str
    message: str
