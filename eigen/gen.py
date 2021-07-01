import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt


def sample():
    x = np.random.rand(1)[0]
    real = 5 * x - 3
    imag = -8 * x + 5
    return real + imag * 1j


def fish(count):
    """ Reproduction of http://www.bohemianmatrices.com/gallery/Eigenfish_5/
    """
    eigenvalues = []
    for _ in range(count):
        a = sample()
        b = sample()
        # eigenfish 1
        # mat = np.array([[0, 1, a, 0], [1, 1, 0, 0], [1, 0, 1, 1], [1, b, 0, 1]])
        # eigenfish 2
        # mat = np.array([[0, a, 1, 0], [1, 1, 0, 0], [1, 0, 1, 1], [1, 0, b, 1]])
        mat = np.array([[0, a, 1, 0], [1, 1, 0, 0], [1, 0, 1, 1], [1, 0, b, 1]])
        values, vectors = la.eig(mat)
        eigenvalues.extend(values)
        # eigenvalues.append(values[0])
    return eigenvalues


def plot(values):
    x = [v.real for v in values]
    y = [v.imag for v in values]
    plt.scatter(x, y, marker="o", color=(0.9, 0.4, 0.1), s=3, alpha=0.5)
    plt.xlabel('real')
    plt.ylabel('imag')
    plt.title('eigenfish')
    ax = plt.gca()
    ax.set_facecolor((0.0, 0.0, 0.0))
    # plt.style.use('dark_background')
    plt.show()
