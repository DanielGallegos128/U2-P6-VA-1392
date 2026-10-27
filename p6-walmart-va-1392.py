import matplotlib.pyplot as plt
import numpy as np
# Daniel Gallegos NC 1392

cant_productos=[100,150,200,300,500]
precio=[4000,7000,9000,12000,18000]

plt.plot(cant_productos,precio)
plt.show()

plt.plot(cant_productos,precio,color='green',marker='o',linestyle='dashed',linewidth=2,markersize=12)
plt.title("Ventas de Walmart 1392")
plt.xlabel("Cant prod")
plt.ylabel("Precio")
plt.show()