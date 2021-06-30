import torch
state_dict = torch.load('./net/epoch.pth', map_location="cpu")
torch.save(state_dict, './net/new_epoch.pth', _use_new_zipfile_serialization=False)
#使新版pytorch能够使用模型
