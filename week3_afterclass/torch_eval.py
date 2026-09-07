import torch
from torch import nn
model = nn.Sequential(nn.Linear(4,8), nn.ReLU(), nn.Linear(8,1))
model.eval()
with torch.no_grad():
    out = model(torch.randn(2,4))
print("eval shape:", out.shape)
