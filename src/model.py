# -*- coding: utf-8 -*-

from torch import nn

class MeasurePredictNet(nn.Module):
    def __init__(self, inputDim, hiddenDim, outputDim):
        super(MeasurePredictNet, self).__init__()
        self.rnn = nn.LSTM(input_size = inputDim,
                            hidden_size = hiddenDim,
                            batch_first = True)
        self.layer1 = nn.Linear(hiddenDim, 250)
        self.layer2 = nn.Linear(250, 200)
        self.layer3 = nn.Linear(200, 100)
        self.layer4 = nn.Linear(100, 50)
        self.layer5 = nn.Linear(50, 25)
        self.layer6 = nn.Linear(25, 15)
        self.layer7 = nn.Linear(15, 10)
        self.layer8 = nn.Linear(10, 5)
        self.layer9 = nn.Linear(5, 3)
        self.relu = nn.ReLU()
        self.tanh = nn.Tanh()
        self.output_layer = nn.Linear(3, outputDim)

    
    def forward(self, inputs, hidden0=None):
        output, (hidden, cell) = self.rnn(inputs, hidden0)
        output = self.layer1(output)
        output = self.layer2(output)
        output = self.layer3(output)
        output = self.layer4(output)
        output = self.layer5(output)
        output = self.layer6(output)
        output = self.layer7(output)
        output = self.layer8(output)
        output = self.layer9(output)
        output = self.output_layer(output)
        output = output[:, -1, :]
        return output

