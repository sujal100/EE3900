import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
x = np.linspace(-5,5,300)
y = x ** 2 + 2

# Create the plot
plt.plot(x,y,label='$x^2 + 2$')

# Add a title
plt.title('')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')

# Add a Legenda
plt.legend()
# Show the plot
plt.show()