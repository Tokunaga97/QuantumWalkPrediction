# -*- coding: utf-8 -*-

import numpy as np
import math

#完全グラフK3(閉路グラフC3)
def K3GraphInitialState(e_n=6):
    #初期状態では頂点v_1に測度をのせる
    psy = [0 for i in range(e_n)]
    psy[2] = 1 / math.sqrt(2)
    psy[3] = 1j * 1 / math.sqrt(2)
    psy = np.array(psy)
    return psy


#閉路グラフC4
def C4GraphInitialState(e_n=8):
    #初期状態では頂点v_1に測度をのせる
    psy = [0 for i in range(e_n)]
    psy[3] = 1 / math.sqrt(2)
    psy[4] = 1j * 1 / math.sqrt(2)
    psy = np.array(psy)
    return psy


#バタフライグラフ
def ButterflyGraphInitialState(e_n=12):
    #初期状態では頂点v_1に測度をのせる
    psy = [0 for i in range(e_n)]
    psy[2] = 1 / math.sqrt(4)
    psy[3] = 1j * 1 / math.sqrt(4)
    psy[8] = 1 / math.sqrt(4)
    psy[9] = 1j * 1 / math.sqrt(4)
    psy = np.array(psy)
    return psy


#完全グラフK4
def K4GraphInitialState(e_n=12):
    #初期状態では頂点v_1に測度をのせる
    psy = [0 for i in range(e_n)]
    psy[3] = 1 / math.sqrt(3)
    psy[4] = 1j * 1 / math.sqrt(3)
    psy[10] = 1 / math.sqrt(3)
    psy = np.array(psy)
    return psy


#完全二部グラフK2_3
def K2_3GraphInitialState(e_n=12):
    #初期状態では頂点v_1に測度をのせる
    psy = [0 for i in range(e_n)]
    psy[3] = 1 / math.sqrt(2)
    psy[8] = 1j * 1 / math.sqrt(2)
    psy = np.array(psy)
    return psy


#スターS3
def S3GraphInitialState(e_n=6):
    #初期状態では頂点v_1に測度をのせる
    psy = [0 for i in range(e_n)]
    psy[3] = 1 / math.sqrt(3)
    psy[4] = 1j * 1 / math.sqrt(3)
    psy[5] = 1 / math.sqrt(3)
    psy = np.array(psy)
    return psy



#フランクリングラフ
def FranklinGraphInitialState(e_n=36):
    #初期状態では頂点v_1に測度をのせる
    psy = [0 for i in range(e_n)]
    psy[11] = 1 / math.sqrt(3)
    psy[12] = 1j * 1 / math.sqrt(3)
    psy[29] = 1 / math.sqrt(3)
    psy = np.array(psy)
    return psy


#ぺーターセングラフ
def PetersenGraphInitialState(e_n=30):
    #初期状態では頂点v_1に測度をのせる
    psy = [0 for i in range(e_n)]
    psy[4] = 1 / math.sqrt(3)
    psy[5] = 1j * 1 / math.sqrt(3)
    psy[15] = 1 / math.sqrt(3)
    psy = np.array(psy)
    return psy