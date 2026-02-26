# -*- coding: utf-8 -*-

import numpy as np
import torch
from quantum_walk import QuantumWalk
import matplotlib.pyplot as plt

limit_time = 1000
graph_name = "Petersen"
edge_num = 1
save_name = r"prediction_result_"+graph_name+"_"+"edge_"+str(edge_num)+".pt"

measures = QuantumWalk(graph_name, limit_time+1)
measures = measures[:, edge_num]

pred = torch.tensor(torch.load(r"./prediction_result/"+save_name))
pred[pred < 0] = 0
pred = pred.numpy()
left = np.array([i for i in range(int(len(measures)*0.8), len(measures))])
height1 = np.array(measures[int(len(measures)*0.8):])
height2 = pred
error = sum(abs(height1 - height2)) / len(height1)
print(error)
plt.plot(left, height1, label='actual', linestyle="solid")
plt.plot(left, height2, label='predictive', linestyle="dashed")
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=10)

