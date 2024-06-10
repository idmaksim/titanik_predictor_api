from services.model import ModelService


def model_service():
    return ModelService('src/model/model.pkl')
