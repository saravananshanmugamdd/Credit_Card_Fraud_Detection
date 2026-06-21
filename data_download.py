import kagglehub
import shutil
import pandas as pd
import os

path=kagglehub.dataset_download("mlg-ulb/creditcardfraud")

os.makedirs("data/raw", exist_ok=True)

shutil.copy(
    os.path.join(path, "creditcard.csv"),
    "data/raw/creditcard.csv"

)


print("Dataset downloaded successfully!")