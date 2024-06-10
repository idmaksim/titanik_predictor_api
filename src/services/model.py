from pandas import DataFrame
from joblib import load
from schemas.users import UserInfo



class ModelService:
    def __init__(self, model_path: str) -> None:
        self.model = load(model_path)

    async def predict(self, user_info: UserInfo):
        df = await self.to_dataframe(user_info)
        pred = self.model.predict(df)
        return bool(pred)


    async def to_dataframe(self, user_info: UserInfo) -> DataFrame:
        return DataFrame(
            {
                'Pclass': [user_info.p_class], 
                'Sex': [user_info.sex], 
                'Age': [user_info.age], 
                'SibSp': [user_info.sibsp], 
                'Parch': [user_info.parch]
            }
        )