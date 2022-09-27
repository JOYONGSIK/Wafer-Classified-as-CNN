import torch
import numpy as np

class EarlyStopping:
    def __init__(self, patience=10, verbose=True, delta=0, path="./"):
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.loss_min = np.Inf
        self.delta = delta
        self.path = path

    def __call__(self, loss, model):
        score = -loss

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(loss, model)

        elif score < self.best_score + self.delta:
            self.counter += 1
            print(f"EarlyStopping counter: {self.counter} out of {self.patience}")
            if self.counter >= self.patience:
                self.early_stop = True
                
        else:
            self.best_score = score
            self.save_checkpoint(loss, model)
            self.counter = 0

    def save_checkpoint(self, loss, model):
        if self.verbose:
            print(
                f"Validation loss decreased ({self.loss_min:.6f} --> {loss:.6f}).  Saving model ..."
            )
        torch.save(model.state_dict(), self.path)
        self.loss_min = loss 
