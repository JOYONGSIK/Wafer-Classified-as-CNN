import numpy as np
import matplotlib.pyplot as plt 

from torchvision import utils
from wafer.wafer_dataset.dataset import Dataset

# display sample images
def show(img, y=None, color=True):
    npimg = img.numpy()
    npimg_tr = np.transpose(npimg, (1,2,0))

    if y is not None:
        plt.title('labels :' + str(y))
        
    plt.imshow(npimg_tr)
    plt.savefig('./data/static/show_grid.jpg', dpi=300)
        
grid_size = 4 
rnd_inds = np.random.randint(0, len(Dataset.train_folder_dataset), grid_size)
print(f'image indices: {rnd_inds}')

x_grid = [Dataset.train_folder_dataset[i][0] for i in rnd_inds]
y_grid = [Dataset.train_folder_dataset[i][1] for i in rnd_inds]

x_grid = utils.make_grid(x_grid, nrow=grid_size, padding=2)

show(x_grid, y_grid)