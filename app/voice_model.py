import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class VoiceModelService:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.is_trained = False

    def train(self, X, y):
        self.model.fit(X, y)
        self.is_trained = True

    def predict(self, audio_features):
        if not self.is_trained:
            raise Exception("Model is not trained yet.")
        return self.model.predict(np.array(audio_features).reshape(1, -1))

    def save_model(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self.model, f)

    def load_model(self, file_path):
        with open(file_path, 'rb') as f:
            self.model = pickle.load(f)
            self.is_trained = True