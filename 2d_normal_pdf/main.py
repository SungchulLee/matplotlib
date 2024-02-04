import matplotlib.pyplot as plt
import numpy as np

def f(X, Y):
    return np.exp( - X**2 / 2 - Y**2 / 2 ) / ( 2 * np.pi )


def main():
    x = np.linspace(-4,4,100)
    y = np.linspace(-4,4,100)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig, ax = plt.subplots(1, 1, figsize=(5*1.61803398875,5), subplot_kw={'projection': '3d'})

    ax.set_title("Standard Normal PDF", fontsize=15)
    ax.plot_surface(X, Y, Z,
                    rstride=2,
                    cstride=2,
                    cmap=plt.cm.coolwarm,
                    linewidth=0.5,
                    antialiased=True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.set_zticks( (0.05, 0.10, 0.15) )

    plt.show()

if __name__ == "__main__":
    main()