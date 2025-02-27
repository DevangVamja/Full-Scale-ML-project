import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class CustomData:
    def __init__(self, data):
        #gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,math_score,reading_score,writing_score
        self.gender = str(data['gender'])
        self.race_ethnicity = str(data['race_ethnicity'])
        self.parental_level_of_education = str(data['parental_level_of_education'])
        self.lunch = str(data['lunch'])
        self.test_preparation_course = str(data['test_preparation_course'])
        self.reading_score = int(data['reading_score'])
        self.writing_score = int(data['writing_score'])

    def to_df(self):
        try:
            return pd.DataFrame([vars(self)])
        except Exception as e:
            CustomException(e, sys)
    
class Prediction:
    def __init__(self, data):
        logging.info("loading data")
        self.data = data
        self.preprocessor_path = os.path.join("artifacts", "proprocessor.pkl")
        self.model_path = os.path.join("artifacts", "model.pkl")
        logging.info("data loaded")

    def preprocess(self):
        try:
            logging.info("preprocessing data")
            preprocessor = load_object(self.preprocessor_path)
            return preprocessor.transform(self.data)
        except Exception as e:
            CustomException(e, sys)
    
    def predicts(self):
        try:
            logging.info("predicting data")
            model = load_object(self.model_path)
            return model.predict(self.preprocess())
        except Exception as e:
            CustomException(e, sys)
            

    
