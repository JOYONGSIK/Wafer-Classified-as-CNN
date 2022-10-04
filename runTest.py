import os 
import torch
import numpy as np
import matplotlib.pyplot as plt 

# from src.wafer.utils.showgrid import show
from src.wafer.train import train_val
from src.wafer.parameters import ResNetParameters
from src.wafer.config import gpu_setting

device =gpu_setting.device

model, params_train = ResNetParameters('Resnet34')
model, loss_hist, metric_hist = train_val(model, params_train)