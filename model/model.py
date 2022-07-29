from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import HistGradientBoostingRegressor


class Model:
    def __init__(self, model_path, str=None):
        self._model = None
        self._model_path = model_path
        self.load()


    def train(self, X:np.ndarray, y:np.ndarray):
        # self._model = RandomForestRegressor()
        self._model = HistGradientBoostingRegressor()
        self._model.fit(X,y)
        return self

    def predict(self, X:np.ndarray) -> np.ndarray:
        return self._model.predict(X)

    def load(self):
        try:
            self._model = joblib.load(self._model_path)
        except:
            self._model = None
        return self

    def save(self):
        if self._model is not None:
            joblib.dump(self._model, self._model_path)
        else:
            raise TypeError("haven't trained the model yet")


model_path = Path(__file__).parent / "model.joblib"
model = Model(model_path)

def get_model():
    return model

if __name__ == '__main__':
    dataset = pd.read_csv('../data/data__0011_20220703.csv')
    X = dataset.iloc[:,1:]
    y = dataset.iloc[:,0]
    model.train(X, y)
    model.save()