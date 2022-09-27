import os
import shutil
import numpy as np
import pandas as pd

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error')
        
train_df = pd.read_csv('./data/train_df.csv')
test_df = pd.read_csv('./data/test_df.csv')
all_df = pd.concat([train_df, test_df])

print(all_df.head())
# for num in all_df['failureNum'].unique():
#     createFolder(f'./data/{num}')
    
# for idx in range(len(all_df)):
#     fail_num = all_df.iloc[idx]['failureNum']
#     image_file = all_df.iloc[idx]['image_id']
#     shutil.move(f'./image_data/{image_file}', f'./data/{fail_num}/{image_file}')
    