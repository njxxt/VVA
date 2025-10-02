import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(14, 8))


years = ['1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946']
ci_t = [18500, 19200, 17600, 14200, 13800, 15200, 16800, 18100]
mi_t = [1200, 1500, 4800, 6200, 5800, 4200, 2500, 1800]
total_t = [i + j for i, j in zip(ci_t, mi_t)]


bar = plt.bar(years, ci_t, color='blue', edgecolor='black', linewidth=1.5, label='Civil trains', alpha=0.735)
Mo = plt.bar(years, mi_t, color='red', bottom=ci_t, edgecolor='black', linewidth=1.5, label='Military trains', alpha=0.735)

plt.plot(np.arange(len(years)), total_t, color='green', linewidth=4, marker='o', markersize=8, markerfacecolor='white', markeredgewidth=2, markeredgecolor='#2ca02c', label='Sum the qua')


for i, (ci, mi, tt) in enumerate(zip(ci_t, mi_t, total_t)):
    plt.text(i, tt + 800, f'{tt}', ha='center', va='bottom', color='#2ca02c') #gre
    plt.text(i, ci / 2, f'{ci}', ha='center', va='center', color='white') #ci
    plt.text(i, ci + mi / 2, f'{mi}', ha='center', va='center', color='white')


plt.ylabel('The qua of trains', fontsize=13, fontweight='bold')
plt.xlabel('Y-y', fontsize=13, fontweight='bold')
plt.legend(loc='upper left')
plt.title('The quantity of trains in the USSR during the Great Patriotic war:\n(1939-1946 yy)', fontsize=12, fontweight='bold', color='#8B0000')

plt.grid(axis='y', alpha=0.3)
plt.ylim(0, 26000)



plt.show()









