import matplotlib.pyplot as plt

M, I, S, T = (0,0), (3.5, 0), (5.18,6.28), (2.28,8.51)
# a = 5.18-3.5
# b = 6.23
# ans = a**2+b**2
# ans = ans**(1/2)
# print(b/a)
def line_gen(C1, C2):   
  return ((C1[0], C2[0]), (C1[1], C2[1]))  
l1 = line_gen(M, I)
l2 = line_gen(I, S)
l3 = line_gen(S, T)
l4 = line_gen(T, M)
 
def drawLine(line):   
  plt.plot(line[0], line[1])   
def drawVertix(coordinate, name):  
  plt.plot(coordinate[0], coordinate[1], 'o')   
  plt.text(coordinate[0] * (1 + 0.1), coordinate[1] * (1 - 0.1) , name)
  
# drawing Quadrilateral
drawLine(l1)
drawLine(l2)
drawLine(l3)
drawLine(l4)

 # plotting vertices
drawVertix(M, "M")
drawVertix(I, "I")
drawVertix(S, "S")
drawVertix(T,"T") 
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Quadrilateral MIST')
plt.grid()
plt.show()