import torch

filepath = 'hackathon3/model.pth'
model = torch.load(filepath)
print(model)