from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str="artifacts/train.csv"
    test_data_path:str="artifacts/test.csv"
    raw_data_path:str="artifacts/raw.csv"