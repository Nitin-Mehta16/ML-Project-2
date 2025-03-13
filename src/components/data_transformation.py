#USED FOR PERFORMING EDA ON DATA ND SPLITING OF DATA INTO TRAIN, TEST AND VALIDATION.
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
import os 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

@dataclass
class DataTransformationConfig:
    artifact_dir: str=os.path.join(ROOT_DIR, "artifact")
    preprocessor_obj_file_path : str = os.path.join(artifact_dir, 'preprocessor.pkl')

#main class
class DataTransformation:
    def __init__(self):
        logging.info("Data Transformation initialized")
        self.transformation_config = DataTransformationConfig()
    
    def get_data_transformer(self):
        '''
        This function is used to get the data transformation object.
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            logging.info(f"Creating categorical columns {numerical_columns}")

            categorical_columns = [
            "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course",
            ]
            logging.info(f"Creating categorical columns  --> {categorical_columns}")


            logging.info("Creating numerical pipeline")
            num_pipeline = Pipeline(
                steps=[
                    ("impute", SimpleImputer(strategy="median")),
                    ("standardization", StandardScaler(with_mean=False)),
                ]
            )

            logging.info("Creating categorical pipeline")
            cat_pipeline= Pipeline(
                steps=[
                    ("impute", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoding", OneHotEncoder()),
                    ("standardization", StandardScaler(with_mean=False)),
                ]
            )

            logging.info("Combining/Executing numerical and categorical pipeline using ColoumnTransformer")
            full_pipeline = ColumnTransformer(
                [
                    ("num_pipeline" , num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns),
                ]
            )
            return full_pipeline

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformtion(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Read train and test data")

            
             
            logging.info("intizialiting target_column_name and numerical_columns")
            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]
            
            logging.info("seperating input_feature and target_feature from TRAIN data ")            
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            logging.info("seperating input_feature and target_feature from TEST data ")
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            logging.info("Getting full_pipeline")
            Pipeline=self.get_data_transformer()  # return full_pipeline

            logging.info("Applying Pipeline on training dataframe and testing dataframe.")
            transformed_input_feature_train_df = Pipeline.fit_transform(input_feature_train_df)
            transformed_input_feature_test_df = Pipeline.transform(input_feature_test_df)
            logging.info("Data Transformation completed")
            
            logging.info("Combining dependent and independent features for training data")
            #np.c_[] is a NumPy column-wise concatenation operation. It combines multiple arrays column-wise.
            train_data = np.c_[transformed_input_feature_train_df, target_feature_train_df]

            logging.info("Combining dependent and independent features for testing data")
            test_data = np.c_[transformed_input_feature_test_df, target_feature_test_df]

            save_object( # saving full_pipeline as preprocessor.pkl file
                file_path=self.transformation_config.preprocessor_obj_file_path,
                obj=Pipeline    # return full_pipeline
            )

            return train_data, test_data , self.transformation_config.preprocessor_obj_file_path

        except Exception as e:
            raise CustomException(e,sys)
        
            
