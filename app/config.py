from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Application settings"""
    
    # API Configuration
    api_key: str = "default-api-key"
    environment: str = "development"
    debug: bool = True
    
    # Model Configuration
    model_path: str = "./models/voice_detection_model.pt"
    confidence_threshold: float = 0.5
    
    # Audio Processing
    sample_rate: int = 16000
    max_audio_size: int = 10485760  # 10MB
    supported_languages: List[str] = ["tamil", "english", "hindi", "malayalam", "telugu"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()