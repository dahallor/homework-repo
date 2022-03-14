x1 = 1
x2 = 1
w1 = 0
w2 = 0

delta_w1 = 2 * (x1 * w1 - 5 * x2 * w2 - 2) * x1
delta_w2 = -10 * x2 * (x1 * w1 - 5 * x2 * w2 -2)

print(delta_w1, delta_w2)

W = 0 + .01 * (-1 * -4)
print(W)