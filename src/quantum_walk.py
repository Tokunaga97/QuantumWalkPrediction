# -*- coding: utf-8 -*-

import numpy as np
from unitary_matrixes import K3GraphUnitaryMatrix, C4GraphUnitaryMatrix, ButterflyGraphUnitaryMatrix, K4GraphUnitaryMatrix, \
                            K2_3GraphUnitaryMatrix, S3GraphUnitaryMatrix, FranklinGraphUnitaryMatrix, PetersenGraphUnitaryMatrix
from initial_states import K3GraphInitialState, C4GraphInitialState, ButterflyGraphInitialState, K4GraphInitialState,\
                            K2_3GraphInitialState, S3GraphInitialState, FranklinGraphInitialState, PetersenGraphInitialState
                    
graph_info = {
              "K3":(K3GraphUnitaryMatrix(), K3GraphInitialState()), "C4": (C4GraphUnitaryMatrix(), C4GraphInitialState()),\
              "Butterfly": (ButterflyGraphUnitaryMatrix(), ButterflyGraphInitialState()), "K4": (K4GraphUnitaryMatrix(), K4GraphInitialState()),\
              "K2_3": (K2_3GraphUnitaryMatrix(), K2_3GraphInitialState()), "S3": (S3GraphUnitaryMatrix(), S3GraphInitialState()),\
              "Franklin": (FranklinGraphUnitaryMatrix(), FranklinGraphInitialState()), "Petersen": (PetersenGraphUnitaryMatrix(), PetersenGraphInitialState())    
              }


def QuantumWalk(graph_name, limit_time, graph_info=graph_info):
    
    M = [] #全ての時刻における量子ウォーカーの存在確率
    m_list = [] ##時刻tにおける量子ウォーカーの存在確率
    #ユニタリ行列と初期状態を取得         
    U, psy = graph_info[graph_name]
    #各エッジの初期状態における量子ウォーカーの存在確率を計算
    for p in psy:
        measure = abs(p) ** 2
        m_list.append(measure)
    M.append(m_list)
    #指定時刻まで量子ウォークを展開    
    for _ in range(limit_time-1):
        m_list = []
    
        psy = np.dot(psy, U)
        #存在確率を計算
        for p in psy:
            measure = abs(p) ** 2
            m_list.append(measure)
        M.append(m_list)
    M = np.array(M)
    
    return M
