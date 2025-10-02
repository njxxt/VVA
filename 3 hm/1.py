import numpy as np
import matplotlib.pyplot as plt

count = -10
def tib():
    x = []
    y = []
    for i in range(1, 11):
        x.append(i + count)
    for i in range(1, 11):
        y.append(abs( x[i - 1] + np.random.normal(-0.1, 0.1) * np.random.normal(-i**0.5, i)))

    plt.ylabel('intent to drive for tibet')
    plt.xlabel('qua of days')
    plt.plot(x, y, marker='o', markerfacecolor='pink', color='red')
    plt.title('Stonks', fontweight='bold')
    plt.grid(True)
    plt.show()

while True:
    count += 10
    if input() == '☭':
        print(tib())
    else:
        break