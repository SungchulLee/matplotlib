import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)

n = 100

x = np.random.normal(size=(n,))

noize_level = 0.5
noize = noize_level * np.random.normal(size=(n,)) 

y = 1 + x + noize 
y_pred = 1 + x

plt.plot(x,y,'o')
plt.plot(x,y_pred)

plt.savefig('img/linear_regression.png');