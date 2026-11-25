import numpy as np

np.random.seed(0)
x1 = np.random.rand(100)     # 花费
x2 = np.random.rand(100)     # 点击
y = 3 * x1 + 5 * x2 + 2 + np.random.randn(100) * 0.1

w1, w2, b = 0.0, 0.0, 0.0
lr = 0.1

for step in range(2000):
    y_hat = w1*x1 + w2*x2 + b      # TODO
    err = y_hat - y        # TODO
    loss = np.mean(err*err)       # TODO
    dw1 = 2 * np.mean(err*x1)        # TODO 自己推
    dw2 = 2 * np.mean(err*x2)        # TODO 自己推
    db = np.mean(err)         # TODO
    w1 = w1 - lr*dw1         # TODO 更新
    w2 = w2 - lr*dw2
    b = b - lr*db
    if step % 200 == 0:
        print(step, round(loss, 4), round(w1, 3), round(w2, 3), round(b, 3))