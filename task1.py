# Постройте график функции f(x) = 5x^2 + 10x - 30

from matplotlib import pyplot as plt

x = []
y = []
for i in range(-15, 15):
    x.append(i)

for i in range(len(x)):
    y.append(5 * x[i] * x[i] + 10 * x[i] - 30)

plt.plot(x, y)
plt.show()