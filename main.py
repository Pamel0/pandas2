import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
from PIL import Image


# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro:', label='linia')
# plt.ylabel('wartości z wektora')
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r:')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo' )
#
# # plt.axis([0, 6, 0, 20])
# plt.show()

# t = np.arange(0, 5, 0.1)
#
# plt.plot(t, t, 'r-', t, t**2, 'b:', t, t**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'], loc='center left')
# plt.show()

# x = np.linspace(0, 2, 100)
#
# plt.plot(x, x, label='liniowa')
# plt.plot(x, x**2, label='kwadratowa')
# plt.plot(x, x**3, label='sześcienna')
#
# plt.xlabel('etykieta osi x')
# plt.ylabel('etykieta osi y')
# plt.title('Wykres trzech linii')
#
# plt.savefig('plot.png')
# plt.show()
#
# im1 = Image.open('plot.png')
# im1 = im1.convert('RGB')
# im1.save('plot.jpg')

# x = np.arange(1,20)
# y = (1/x)
# plt.plot(x, y, 'mo-')
# plt.legend(labels=['wykres'])
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Ciekawy wykres')
# plt.show()

# x = np.arange(0,10, 0.1)
# y = np.sin(x)
# plt.plot(x, y, 'rH-')
# plt.legend(labels=['skill'])
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('kolejny Ciekawy wykres')
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)

# plt.subplot(2, 1, 1)
# plt.plot(x1, y1)
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# plt.title('wykres sin(x)')
#
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.ylabel('cos(x)')
# plt.xlabel('x')
# plt.title('wykres cos(x)')
#
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# fig, axs = pl.subplots(3, 2)
# # print(type(fig))
# # print(type(axs))
# # plt.show()
# axs[0, 0].plot(x1, y1, 'g-')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[0, 0].set_title('Wykres sin(x)')
#
# axs[1, 1].plot(x2, y2, 'r-')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[1, 1].set_title('Wykres cos(x)')
#
# axs[2, 0].plot(x2, y2, 'r-')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
# axs[2, 0].set_title('Wykres cos(x)')
#
#
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
#
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 51, 50),
#         'd': np. random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter(data=data, x='a', y='b', color='red', s='d')
# plt.xlabel('wartości z klucza a')
# plt.ylabel('wartości z klucza b')
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [746400000, 4561000000, 420500000],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa']}
#
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Populacja').sum())
# print(etykiety)
# print(wartosci)
# plt.bar(x=etykiety, height=wartosci, color=['red', 'green', 'blue'])
# plt.xlabel('Kontynent')
# plt.ylabel('Populacja na kontynentach')
# plt.show()

# x = np.random.randn(10000)
#
# plt.hist(x, bins=10, facecolor='g', alpha=0.75, density=True)
#
# plt.xlabel('Wartość')
# plt.ylabel('Prawdopodobieństwa')
# plt.title('Histogram')
# plt.show()


#wykres kołowy, ogarnąć

