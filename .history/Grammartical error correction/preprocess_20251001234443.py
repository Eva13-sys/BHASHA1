import pandas as pd
import os

train_file = 'train.csv'
dev_file = 'dev.csv'

os.makedirs('data', exist_ok=True)

train_df= pd.read_csv(train_file)
dev_df= pd.read_csv(dev_file)

train_df["input"]