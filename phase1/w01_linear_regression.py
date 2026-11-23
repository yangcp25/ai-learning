import numpy as np

np.random.seed(0)
x = np.random.rand(100)                  # 100 个花费，0~1 之间
y = 3 * x + 2 + np.random.randn(100) * 0.1   # 真实规律 + 一点噪声

w, b = 0.0, 0.0
lr = 0.1

for step in range(1000):
    y_hat = w*x+b       # TODO 预测 y
    err = y_hat - y          # TODO 误差
    loss = np.mean(err*err)         # TODO 平均平方误差：err 平方后求平均
    dw = 2 * np.mean(err * x)           # TODO
    db = 2 * np.mean(err)           # TODO
    w = w - lr * dw            # TODO 更新
    b = b - lr * db             # TODO 更新
    if step % 100 == 0:
        print(step, round(loss, 4), round(w, 3), round(b, 3))