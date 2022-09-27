import os
import shutil
import splitfolders
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

for num in all_df['failureNum'].unique():
    createFolder(f'./data/failureNum/{num}')
    
for idx in range(len(all_df)):
    fail_num = all_df.iloc[idx]['failureNum']
    image_file = all_df.iloc[idx]['image_id']
    shutil.move(f'./data/image_data/{image_file}', f'./data/failureNum/{fail_num}/{image_file}')
    
splitfolders.ratio('./data/failureNum/', './data/', ratio=(0.7, 0.3))
os.remove('./data/image_data')