import sympy as sp
import sympy.plotting as syp
import matplotlib.pyplot as plt

x = sp.symbols('x') 
lamb = sp.symbols('lambda')
# Exponential Distribution Formulu:
exponential = 1-(sp.exp(-x*lamb))
# Soruyu çözebilmek için mutlaka lambda değerini bilmek gerekir

x_values=[]
y_values=[]
# x değerlerinin 0 dan büyük olması gerekiyor.
for value in range(1,10):
    y = exponential.subs({x:value,lamb:2}).evalf()
    x_values.append(value)
    y_values.append(y)
plt.plot(x_values,y_values)    
plt.show()




