import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import logger
from src.exception import CustomException
from src.entity import DataIngestionConfig

class DataIngestion:

    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logger.info("Entered the data injestion Method")

        try:
            df=pd.read_csv("data/raw/creditcard.csv")
            logger.info("Dataset Loaded successffully")

            os.makedirs("artifacts", exist_ok=True)

            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )
            logger.info("Raw Data Saved")

            train_data, test_data=train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            logger.info("data splitted for train and test")

            train_data.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            logger.info("train data saved")

            test_data.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logger.info("test data saved")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)