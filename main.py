from src.components.data_ingestion import DataIngestion
from src.logger import logger

if __name__=="__main__":
    logger.info("Application started")

    data_ingestion=DataIngestion()

    train_path, test_path=data_ingestion.initiate_data_ingestion()

    logger.info("Data injestion completed")

    print("train_data", train_path)
    print("test_data", test_path)