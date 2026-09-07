import numpy as np
x = np.linspace(0, 10, 100)
y_true = 2*x + 5
w = np.random.randn()
b = np.random.randn()
for _ in range(100):
    pred = w*x + b
    loss = ((pred-y_true)**2).mean()
    dw = (2*(pred-y_true)*x).mean()
    db = (2*(pred-y_true)).mean()
    w -= 0.01*dw
    b -= 0.01*db
print(f"w={w:.3f} b={b:.3f} loss={loss:.6f}")
