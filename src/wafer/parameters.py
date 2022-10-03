import torch 
import torch.nn as nn

from torch import optim
from torch.optim.lr_scheduler import ReduceLROnPlateau

from wafer.config import gpu_setting
from wafer.wafer_dataset.dataset import Dataset
from wafer.core.resnet import resnet34, resnet50, resnet101 

def ResNetParameters(model):
    device = gpu_setting.device
    model = model.lower()
    if model == 'resnet34':
        model = resnet34().to(device)
    if model == 'resnet50':
        model = resnet50().to(device)
    if model == 'resnet101':
        model = resnet101().to(device)
        
    loss_func = nn.CrossEntropyLoss(reduction='sum')
    opt = optim.Adam(model.parameters(), lr=0.001)
    lr_scheduler = ReduceLROnPlateau(opt, mode='min', factor=0.1, patience=10)
    
    # definc the training parameters
    params_train = {
        'num_epochs':20,
        'optimizer':opt,
        'loss_func':loss_func,
        'train_dl':Dataset.train_dl, 
        'val_dl':Dataset.val_dl,
        'sanity_check':False,
        'lr_scheduler':lr_scheduler,
        'path2weights':f'./src/wafer/trained_model/weights.pt',
    }
    return model, params_train
