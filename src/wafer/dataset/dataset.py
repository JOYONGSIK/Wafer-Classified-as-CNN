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