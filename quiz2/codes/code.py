import numpy as np
import matplotlib.pyplot as plt

def u(x):
  if x >=0 :
    return 1
  else:
    return 0

X = np.arange(-5 , 5 , 1)
def h(x):
  res = []
  for i in range(len(x)):
    if x[i] == 0 :
      res.append(-2+((-0.5)**x[i]+8*u(x[i])/3))
    else:
      res.append((-0.5)**x[i]+8*u(x[i])/3)
  return res

plt.stem(X , h(X) , 'ko' , label = "$-2 \delta[n]+\\frac{1}{3}(-\\frac{1}{2})^{n} u[n]+\\frac{8}{3} u[n]$", use_line_collection=True)
plt.grid(True)
plt.title("h[n]")
plt.legend()
plt.show()