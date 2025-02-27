import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.transformation_config=DataTransformationConfig()
    
    def make_data_transformation_pipeline(self,num_cols,cat_cols):
        try:
            logging.info("Creating Data Transformation Pipeline")
            
            num_pipeline=Pipeline([
                ('imputer',SimpleImputer(strategy='median')),
                ('std_scaler',StandardScaler())
            ])

            cat_cols_pipeline=Pipeline([
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder',OneHotEncoder()),
                ('std_scaler',StandardScaler(with_mean=False)),
            ])

            preprocessor=ColumnTransformer([
                ('num_pipe',num_pipeline,num_cols),
                ('cat_pipe',cat_cols_pipeline,cat_cols)
            ])
            logging.info("Data Transformation Pipeline Created")
            return preprocessor

        except Exception as e:
            logging.error("Data Transformation Failed")
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_data_path,test_data_path):
        logging.info("Initiating Data Transformation")
        try:
            # Reading the data
            self.train_data=pd.read_csv(train_data_path)
            self.test_data=pd.read_csv(test_data_path)
            logging.info("Data Loaded")

            self.target_col='math_score'

            # getting the numerical and categorical columns
            num_cols=self.train_data.select_dtypes(include=[np.number]).columns
            cat_cols=self.train_data.select_dtypes(include=[object]).columns
        
            if self.target_col in num_cols:
                num_cols=num_cols.drop(self.target_col)
            else:
                cat_cols=cat_cols.drop(self.target_col)
            logging.info("Columns Split into Numerical and Categorical")
            logging.info(f"Numerical Columns: {num_cols}")
            logging.info(f"Categorical Columns: {cat_cols}")
            # Creating the data transformation pipeline
            self.preprocessor= self.make_data_transformation_pipeline(num_cols,cat_cols)
            logging.info("Preprocessor Created")

            
            self.input_features_train=self.train_data.drop(self.target_col,axis=1)
            self.input_features_test=self.test_data.drop(self.target_col,axis=1)
            self.target_train=self.train_data[self.target_col]
            self.target_test=self.test_data[self.target_col]
            logging.info("Data Split into Input Features and Target")

            self.input_features_train=self.preprocessor.fit_transform(self.input_features_train)
            self.input_features_test=self.preprocessor.transform(self.input_features_test)
            self.train_array=np.c_[self.input_features_train,self.target_train]
            self.test_array=np.c_[self.input_features_test,self.target_test]
            logging.info("Preprocessor fit on data")

            save_object(
                obj=self.preprocessor,
                file_path=self.transformation_config.preprocessor_obj_file_path
                )
            logging.info("Preprocessor Saved")

            return self.train_array,self.test_array,self.transformation_config.preprocessor_obj_file_path


        except Exception as e:
            raise CustomException(e,sys)