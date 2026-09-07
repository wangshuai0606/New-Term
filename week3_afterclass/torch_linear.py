import torch
from torch import nn
x = torch.linspace(-1,1,101).reshape(-1,1)
y = 3*x - 1
model = nn.Linear(1,1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)
for _ in range(200):
    opt.zero_grad()
    loss = loss_fn(model(x), y)
    loss.backward()
    opt.step()
print(f"w={model.weight.item():.4f} b={model.bias.item():.4f}")
