# import numpy as np
# import matplotlib.pyplot as plt
#
# fig,axe = plt.subplots(10, 5, sharex=True, sharey=True, figsize=(6,6))
# # fig.tight_layout(h_pad=1)
# for i in range(10):
#     for j in range(5):
#         obsv1 = np.random.rand(12,2)
#         pred1 = np.random.rand(8,2)
#         pred_hat1 = np.random.rand(8, 2)
#
#         x, y = zip(*obsv1)
#         x1, y1 = zip(*pred1)
#         x2, y2 = zip(*pred_hat1)
#         current_axis = axe[i, j]
#         current_axis.scatter(x, y, c='black', s=0.2)
#         current_axis.scatter(x1, y1, c='green', s=0.2)
#         current_axis.scatter(x2, y2, c='red', s=0.2)
#
# for j in range(5):
#     axe[9, j].set(xlabel='code=' + str(j))
# # plt.savefig('traj.png')
# plt.show()
# import math
#
#
#
# # obsv2 = np.random.rand(3,2)
# # pred2 = np.random.rand(5,2)
# # pred_hat2= np.random.rand(12, 2)
# #
# # obsv3 = np.random.rand(3,2)
# # pred3 = np.random.rand(5,2)
# # pred_hat3 = np.random.rand(12, 2)
# # x, y = zip(*obsv)
# # x1, y1 = zip(*pred)
# # plt.scatter(x, y, c='red')
# # plt.scatter(x1, y1, c='blue')
# # plt.title('code=[0.3, 0.5, 0.5]')
#
# # plt.savefig("traj1.png")
# import torch
#
# # str = "3.44"
# # str.replace('.', '_')
# # print(str)
# # r = torch.rand(2, 32)
# # print(r)
# # r = torch.FloatTensor(torch.rand(2, 32))
# # print(r)
# # arr = [[[ 0.3688,  0.4412,  0.0378, -0.0762],
# #          [ 0.4067,  0.3646,  0.0379, -0.0766],
# #          [ 0.4449,  0.2877,  0.0382, -0.0769],
# #          [ 0.4834,  0.2105,  0.0385, -0.0772],
# #          [ 0.5222,  0.1330,  0.0388, -0.0775],
# #          [ 0.5613,  0.0551,  0.0391, -0.0779],
# #          [ 0.6007, -0.0232,  0.0394, -0.0783],
# #          [ 0.6404, -0.1018,  0.0397, -0.0786],
# #          [ 0.6804, -0.1809,  0.0400, -0.0791],
# #          [ 0.7206, -0.2604,  0.0402, -0.0795],
# #          [ 0.7610, -0.3404,  0.0404, -0.0800],
# #          [ 0.8016, -0.4209,  0.0405, -0.0804]]]
# # # arr = np.asarray(arr)
# # t = torch.FloatTensor(arr)
# # t1 = t[0][:][0:3]
# # print(t)
# # print(t1)
# # m = arr[0][:]
# # print(m)
# # print(arr[0][:][:, [0,2]])

# code1 = 0.0
# while code1 < 1.0:
#     print(code1)
#     code1 += 0.1
#
# for i in range(0, 10, 1):
#     print(i/10)

l = [0, 0]
l[0] = 1
l[1] = 2
print('_'.join(list(map(lambda x: str(x), l))))
l[1] = 2
l[0] = 1
print('_'.join(list(map(lambda x: str(x), l))))
