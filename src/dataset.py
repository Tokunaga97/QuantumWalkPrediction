# -*- coding: utf-8 -*-

import torch
from torch.utils.data import Dataset

class MeasureDataset(Dataset):
    def __init__(self, measures, size=10):
        data = torch.tensor(measures[:int(len(measures)*0.8)], dtype=torch.float32).split(size)
        if len(data[-1]) < size:
            data = data[:-1]
        self.data = data
        self.data_size = len(self.data)
    def __len__(self):
        return self.data_size
    def __getitem__(self, idx):
        return self.data[idx]