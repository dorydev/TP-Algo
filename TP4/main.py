import matplotlib.pyplot as plt
import random as rd
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

class Random_number:
    def __init__(self, a, c, m, y0, n):
        self.a = a
        self.c = c
        self.m = m
        self.y0 = y0
        self.n = n

        self.graphic_render()
        self.histogramme()

    def congruential_linear_generator(self, y):
        return (self.a * y + self.c) % self.m

    def generate_values(self):
        values = []
        y = self.y0
        for _ in range(self.n):
            y = self.congruential_linear_generator(y)
            values.append(y)
        return values

    def histogramme(self):
        y_value = self.generate_values()
        plt.hist(np.array(y_value[1::2]) / self.m, bins=10, density=True, color="white", edgecolor="black", alpha=0.5, label='Histogramme de y')
        x = np.linspace(0, 1, 100)
        plt.plot(x, np.ones_like(x), color='red', linestyle='--', label='Densité de la loi uniforme')

        plt.xlabel('Valeurs de y')
        plt.ylabel('Densité de probabilité')
        plt.title('Histogramme de y comparé à la densité d\'une loi uniforme')
        plt.legend()
        plt.grid(True)
        plt.show()

    #graphic part
    def plot_pairs(self, values):
        plt.scatter(values[::2], values[1::2], s=1, alpha=0.7, cmap='viridis')
        plt.title("Random generator")
        plt.xlabel("y2i")
        plt.ylabel("y2i+1")
        plt.show()

    def graphic_render(self):
        values = self.generate_values()
        self.plot_pairs(values)

rd_nbr = Random_number(843314861, 453816693, 2**31, 1, 10000)
#res  = valeurs(25, 16, 256, 11, 10)
#res_2 = valeurs(843314861, 453816693, 2**31, 1, 10)
#print(res)

