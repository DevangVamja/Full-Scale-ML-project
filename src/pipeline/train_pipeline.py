import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion

from src.components.data_transformation import DataTransformation

from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        self.di=DataIngestion()
        self.dt=DataTransformation()
        self.mt=ModelTrainer()

    def initiate_train_pipeline(self):
        try:
            self.train_data, self.test_data = self.di.initiate_data_ingestion()
            self.train_arr, self.test_arr, self.obj_path = self.dt.initiate_data_transformation(self.train_data, self.test_data)
            return self.mt.initiate_model_trainer(self.train_arr, self.test_arr)

        except Exception as e:
            CustomException(e, sys)

