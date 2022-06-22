import matplotlib.pyplot as pl
from functions import add

x=list(range(10))
y=add(x,x)

plt.plot(x,y)
plt.savefig("plot.png")
