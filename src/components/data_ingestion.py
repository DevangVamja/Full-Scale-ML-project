import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
sys.path.append(os.path.abspath('.'))

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Initiating Data Ingestion")
        try:
            # code to import the data
            self.raw_data=pd.read_csv(os.path.join('notebook', 'data', 'stud.csv'))
            logging.info("Got data as df")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            logging.info("Moving to Data Splitting")
            
            self.train_data, self.test_data = train_test_split(self.raw_data, test_size=0.3, random_state=93)
            logging.info("Data Splitting Done")

            self.raw_data.to_csv(self.ingestion_config.raw_data_path, index=False)
            self.train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            self.test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Raw Data, Train Data, and Test Data Saved")
            
            logging.info("Data Ingestion Completed")

            return self.ingestion_config.train_data_path,self.ingestion_config.test_data_path

        except Exception as e:
            logging.error("Data Ingestion Failed")
            raise CustomException(e,sys)
        

if __name__=="__main__":
    di=DataIngestion()
    train_data, test_data = di.initiate_data_ingestion()

    # Initialize the DataTransformation class to transform the ingested data
    dt=DataTransformation()
    train_arr, test_arr, obj_path = dt.initiate_data_transformation(train_data, test_data)

    mt = ModelTrainer()
    print(mt.initiate_model_trainer(train_arr, test_arr))