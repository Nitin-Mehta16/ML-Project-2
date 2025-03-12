#USED FOR IMPORTING DATA.

import os 
import sys 
from src.exception import CustomExecption
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

#input for where we have save the data(train,test,raw) or from where we have access data  --> for this we have to make seperate class 

@dataclass         #A decorator in Python is a function that modifies the behavior of another function or method without changing its actual code. It allows you to add extra functionality (such as logging, authentication, or timing execution) in a clean and reusable way.
class DataIngestionConfig:
    artifact_dir: str = os.path.join(ROOT_DIR, "artifact")  
    train_data_path: str=os.path.join(artifact_dir, 'train.csv')
    test_data_path: str=os.path.join(artifact_dir, 'test.csv')
    raw_data_path: str=os.path.join(artifact_dir, 'data.csv')


# main class for data ingestion
class DataIngestion: 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initialize_data_ingestion(self):
        logging.info("Data Ingestion initialized")
        try:
            df =  pd.read_csv(r"C:\Users\nitin\DS&ML\31. Ml Project\notebook\data\stud.csv")
            logging.info("read the dataset as dataframe")

            logging.info("making/check the directory for saving the data")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  #The function os.path.dirname(path) returns the directory (folder) part of a given file path, removing the file name #This ensures the "artifact" directory exists without creating a file named "train.csv" as a directory.
            
            logging.info("saving raw data" )
            df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)   
            
            logging.info("splitting data into train and test")
            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            logging.info("saving train and test data to train_data_path and test_data_path") 
            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)

            logging.info("Data Ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e  :
            raise CustomExecption(e,sys)   



if __name__ == "__main__":
    data_ingestion = DataIngestion()
    train_data , test_data = data_ingestion.initialize_data_ingestion()
    data_transformation = DataTransformation() # it will initiate "" self.transformation_config = DataTransformationConfig() ""
    data_transformation.initiate_data_transformtion(train_data,test_data)

    
