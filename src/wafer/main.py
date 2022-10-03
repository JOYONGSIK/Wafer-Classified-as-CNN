import os 
import torch
import numpy as np
import matplotlib.pyplot as plt 

from wafer.core.resnet import resnet34, resnet50, resnet101 
from wafer.wafer_dataset.dataset import Dataset
from wafer.train import train_val
from wafer.parameters import ResNetParameters
from wafer.config import gpu_setting

# print(f"mps 사용 가능 여부: {torch.backends.mps.is_available()}")
# print(f"mps 지원 환경 여부: {torch.backends.mps.is_built()}")

device =gpu_setting.device

model, params_train = ResNetParameters('Resnet34')
model, loss_hist, metric_hist = train_val(model, params_train)