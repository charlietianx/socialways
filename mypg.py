import torch
import torch.nn as nn
import numpy as np
# t = torch.FloatTensor(torch.rand(2, 10))
# print(t)

# arr = [[1,3,5], [0,6,8]]
# arr = list(map(lambda x: list(map(lambda y:y/10, x)), arr))
# print(arr)
# # print(arr[-1])
# arr = torch.tensor(arr)
# print(torch.mean(arr, 1))
# print(torch.mean(arr, 1).mean(0, keepdim = True))
# arr = np.random.uniform(-1, 1, 10)
# t = torch.FloatTensor(arr)
# print(arr)
# print(t)

m = nn.Sigmoid()
loss = nn.BCELoss()
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
print(input, "\n", target)
output = loss(m(input), target)
output.backward()