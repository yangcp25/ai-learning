"""第 1 周 NumPy 练习场:每个概念都用 "NumPy 一行" 和 "Go 风格双层循环" 各算一遍,结果必须一样。

运行: cd /Users/ycp/work/code/own/ai-learning && uv run python phase1/w01_numpy_playground.py
看懂一段后,改里面的数字再跑,看结果怎么变。
"""
import numpy as np

# 3 个广告 x 4 天的花费表
cost = np.array([[100, 200, 150, 300],   # 广告A
                 [ 80,  90, 100, 120],   # 广告B
                 [ 50,  60,  70,  80]])  # 广告C
n_ads, n_days = cost.shape               # 3, 4
print("cost.shape =", cost.shape, " -> cost[i][j]: i 选广告(0~2), j 选天(0~3)\n")


# ---------- 1. axis:写哪一维,哪一维就被加没 ----------
print("=== 1. axis ===")

# axis=1:把 j(天)加没,每个广告剩一个数
by_ad = np.zeros(n_ads)
for i in range(n_ads):          # 保留 i
    for j in range(n_days):     # 加掉 j
        by_ad[i] += cost[i][j]
print("循环,加掉天  :", by_ad, " shape", by_ad.shape)
print("cost.sum(axis=1):", cost.sum(axis=1), " shape", cost.sum(axis=1).shape)

# axis=0:把 i(广告)加没,每天剩一个数
by_day = np.zeros(n_days)
for j in range(n_days):         # 保留 j
    for i in range(n_ads):      # 加掉 i
        by_day[j] += cost[i][j]
print("循环,加掉广告:", by_day, " shape", by_day.shape)
print("cost.sum(axis=0):", cost.sum(axis=0), " shape", cost.sum(axis=0).shape)
print("规律:(3,4) 用 axis=1 -> (3,);用 axis=0 -> (4,)。被写的那一维从 shape 里消失\n")


# ---------- 2. 广播:短的那个自动复制成表那么大 ----------
print("=== 2. 广播 ===")
day_factor = np.array([1, 1, 1.5, 1.5])  # 周末乘 1.5,shape (4,)

manual = np.zeros((n_ads, n_days))
for i in range(n_ads):
    for j in range(n_days):
        manual[i][j] = cost[i][j] * day_factor[j]   # 每一行都用同一组 day_factor
print("循环结果:\n", manual)
print("cost * day_factor:\n", cost * day_factor)
print("NumPy 等于先把 day_factor 复制成 3 行:\n", np.tile(day_factor, (3, 1)), "\n")


# ---------- 3. * 和 @:要明细还是要总数 ----------
print("=== 3. * 和 @ ===")
qty = np.array([[2, 1],    # 订单1:甲 2 个,乙 1 个
                [0, 3],    # 订单2
                [1, 1]])   # 订单3
price = np.array([10, 5])  # 甲 10 元,乙 5 元

detail = np.zeros((3, 2))
total = np.zeros(3)
for i in range(3):
    for k in range(2):
        detail[i][k] = qty[i][k] * price[k]   # * 只做这一步
        total[i] += qty[i][k] * price[k]      # @ 多做一步:加起来
print("qty * price(每样花多少,明细):\n", qty * price)
print("循环明细:\n", detail)
print("qty @ price(每单一共多少):", qty @ price)
print("循环总数:", total)
print("(qty*price).sum(axis=1):", (qty * price).sum(axis=1), " <- @ = 先 * 再按行加\n")


# ---------- 4. reshape:数据不变,换个 shape 给下一步用 ----------
print("=== 4. reshape ===")
img = np.arange(9).reshape(3, 3)   # 假装是一张 3x3 的小图片
print("图片 shape", img.shape, ":\n", img)
flat = img.reshape(9)
print("摊平后 shape", flat.shape, ":", flat, " <- 简单网络只收一排数")
print("flat[i*3+j] 和 img[i][j] 是同一个数:", flat[1 * 3 + 2], "==", img[1][2])
