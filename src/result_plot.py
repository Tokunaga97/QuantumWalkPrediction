# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from quantum_walk import QuantumWalk

limit_time = 100 #時刻の上限
edge_num = 1 #エッジ指定
graph_name = "Petersen" #グラフ名

M = QuantumWalk(graph_name, limit_time+1)
time = np.array([i for i in range(limit_time+1)])
measure = M[:, edge_num]
plt.plot(time, measure)