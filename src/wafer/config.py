import torch 

class DatasetConfig:
    train_dir = "./data/train/"
    valid_dir = "./data/valid/" 

    # Batch size 
    batch_size=32
    
    
# mps -> 조용식의 컴퓨터는 macbook pro, m1 이므로 // gpu, cpu로 변경해서 쓰세요 :)
class gpu_setting:
    device = torch.device('mps' if torch.cuda.is_available() else 'cpu')