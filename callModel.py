import pickle
import numpy as np

class Predict():
    def __init__(self):
        self.value = []
        
    def import_model(self):
        self.filename = 'knn_predict_redwine_quality.pkl'
        try:
            with open(self.filename, 'rb') as self.file:
                self.model = pickle.load(self.file)
            return True
        except ImportError:
            return False
        
    def predictQuality(self):
        self.dataset = np.array([self.value])
        try:
            self.predictvalue = self.model.predict(self.dataset)
            return np.array2string(self.predictvalue).lstrip('[').rstrip(']')
        except:
            return False