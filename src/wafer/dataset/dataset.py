import os
import numpy as np
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

from wafer.config import DatasetConfig


class Dataset:
    train_folder_dataset = dset.ImageFolder(root=DatasetConfig.train_dir)
    train_transformation = transforms.Compose([
                        transforms.ToTensor(),
                        transforms.Resize(224),
                        # transforms.Normalize([train_meanR, train_meanG, train_meanB],[train_stdR, train_stdG, train_stdB]),
                        transforms.RandomHorizontalFlip()])
    
    valid_folder_dataset = dset.ImageFolder(root=DatasetConfig.valid_dir)
    valid_transformation = transforms.Compose([
                        transforms.ToTensor(),
                        transforms.Resize(224),
                        # transforms.Normalize([train_meanR, train_meanG, train_meanB],[train_stdR, train_stdG, train_stdB]),
                        ])
    
    # apply transformation 
    train_folder_dataset.transform = train_transformation
    valid_folder_dataset.transform = valid_transformation
    
    # Create DataLoader 
    train_dl = DataLoader(train_folder_dataset, batch_size=DatasetConfig.batch_size, shuffle=True)
    val_dl = DataLoader(valid_folder_dataset, batch_size=DatasetConfig.batch_size, shuffle=True)
    
    
def get_mean_std(data_dir):
    transform = transforms.Compose([
        transforms.ToTensor()
    ])

    dataset = dset.ImageFolder(os.path.join(f'./{data_dir}'), transform)
    meanRGB = [np.mean(x.numpy(), axis=(1,2)) for x,_ in dataset]
    stdRGB = [np.std(x.numpy(), axis=(1,2)) for x,_ in dataset]

    meanR = np.mean([m[0] for m in meanRGB])
    meanG = np.mean([m[1] for m in meanRGB])
    meanB = np.mean([m[2] for m in meanRGB])

    stdR = np.mean([s[0] for s in stdRGB])
    stdG = np.mean([s[1] for s in stdRGB])
    stdB = np.mean([s[2] for s in stdRGB])
    print("평균",meanR, meanG, meanB)
    print("표준편차",stdR, stdG, stdB)
