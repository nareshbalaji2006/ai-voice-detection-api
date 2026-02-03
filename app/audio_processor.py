import base64
import io
import librosa
import numpy as np
from typing import Tuple
import logging

logger = logging.getLogger(__name__)

class AudioProcessor:
    """Audio processing utility for voice detection"""
    
    @staticmethod
    def decode_base64_audio(audio_base64: str) -> bytes:
        """Decode base64 encoded audio to bytes"""
        try:
            audio_bytes = base64.b64decode(audio_base64)
            return audio_bytes
        except Exception as e:
            logger.error(f"Error decoding base64 audio: {str(e)}")
            raise ValueError("Invalid base64 audio format")
    
    @staticmethod
    def load_audio(audio_bytes: bytes, sr: int = 16000) -> Tuple[np.ndarray, int]:
        """Load audio from bytes and resample to target sample rate"""
        try:
            audio_io = io.BytesIO(audio_bytes)
            y, sr = librosa.load(audio_io, sr=sr)
            return y, sr
        except Exception as e:
            logger.error(f"Error loading audio: {str(e)}")
            raise ValueError("Invalid audio format")
    
    @staticmethod
    def extract_features(audio: np.ndarray, sr: int) -> np.ndarray:
        """Extract audio features for model input"""
        try:
            # MFCC features
            mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
            mfcc_mean = np.mean(mfcc, axis=1)
            
            # Zero Crossing Rate
            zcr = librosa.feature.zero_crossing_rate(audio)[0]
            zcr_mean = np.mean(zcr)
            
            # Spectral Centroid
            spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sr)[0]
            spec_cent_mean = np.mean(spec_cent)
            
            # Combine all features
            features = np.concatenate([mfcc_mean, [zcr_mean, spec_cent_mean]])
            return features
        except Exception as e:
            logger.error(f"Error extracting features: {str(e)}")
            raise ValueError("Error processing audio features")
    
    @staticmethod
    def validate_audio_length(audio: np.ndarray, sr: int, min_duration: float = 0.5, max_duration: float = 60.0) -> bool:
        """Validate audio length is within acceptable range"""
        duration = len(audio) / sr
        return min_duration <= duration <= max_duration