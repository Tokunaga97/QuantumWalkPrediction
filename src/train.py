# -*- coding: utf-8 -*-

import torch
from quantum_walk import QuantumWalk
from model import MeasurePredictNet
from dataset import MeasureDataset
from torch.utils.data import DataLoader
from statistics import mean
from torch import nn, optim
from tqdm import tqdm

limit_time = 1000 #時刻の上限
edge_num = 1 #エッジ指定
graph_name = "Petersen" #グラフ名


measures = QuantumWalk(graph_name, limit_time+1)
measures = measures[:, edge_num]
ds = MeasureDataset(measures, size=11)
loader = DataLoader(ds, batch_size=100, shuffle=True, num_workers=0)

def train_measure(net, loss_f, input, target):
    opt.zero_grad()
    output = net(input.view(-1, 10, 1))
    loss = loss_f(output.view(-1), target.view(-1))
    loss.backward()
    return loss.item()

def predict_measure(net, start=measures[int(len(measures)*0.8)-10:int(len(measures)*0.8)], length=int(len(measures)*0.2)+1):
    net.eval()
    a = int(len(measures)*0.8)-10
    result1 = []
    result2 = []
    result1.append(start)
    index = start
    for i in tqdm(range(length)):
        input_tensor = torch.tensor(index, dtype=torch.float32)#.cuda()
        outputs = net(input_tensor.view(-1, 10, 1))
        index = outputs.item()
        result1 = measures[a+1:a+11]
        result2 += [index]
        a += 1
        index = result1
    return result2


net = MeasurePredictNet(1, 400, 1)#.cuda()
opt = optim.Adam(net.parameters())
loss_f = nn.MSELoss()

losses_fp = []
print('\n')
for epoch in tqdm(range(1, 1001)):
    net.train()
    losses = []
    for data in loader:
        print(data.size())
        x = data[:, :-1]#.cuda()
        y = data[:, -1].contiguous()
        y2 = []
        for i in y:
            y2.append([i])
        y = torch.tensor(y2, dtype=torch.float32)#.cuda()
        loss = train_measure(net, loss_f, x, y)#.long())
        opt.step()
        losses.append(loss)
    losses_fp.append(mean(losses))
    print("["+str(epoch)+"]"+str(mean(losses)))
    pred = predict_measure(net)
    
save_name = r"prediction_result_"+graph_name+"_"+"edge_"+str(edge_num)+".pt"

torch.save(pred, r"./prediction_result/"+save_name)
