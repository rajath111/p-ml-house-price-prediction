import pickle

class ModelLoader:

    @staticmethod
    def load():
        with open('model/modelfile', 'rb') as f:
            return pickle.load(f)