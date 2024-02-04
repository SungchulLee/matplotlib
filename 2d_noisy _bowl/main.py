import matplotlib.pyplot as plt
import numpy as np

def f(X, Y, seed=0):
    np.random.seed(seed)
    return X**2 + Y**2 + 0.15*np.random.normal(0., 1., X.shape)

def main():
    x = np.linspace(-1.5, 1.5, 80)
    y = np.linspace(-1.5, 1.5, 80)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig, ax = plt.subplots(1, 1, figsize=(9,6), subplot_kw={'projection': '3d'})

    ax.plot_surface(X, Y, Z,
                    rstride=2,
                    cstride=2,
                    cmap=plt.cm.coolwarm,
                    linewidth=0.5,
                    antialiased=True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')

    plt.show()

if __name__ == "__main__":
    main()