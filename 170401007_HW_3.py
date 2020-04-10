import sympy as sp
import sympy.plotting as syp
import matplotlib.pyplot as plt
#  Sorumuz:
# Bir bankaya yeni bir müşteri gelme süresi 5dk ortalamalı üstel dağılıma sahiptir.
# Bu bankaya 10 dk içerisnde her dakika için müşteri gelmeme olasılığını hesaplayınız.

# üstel dağılım = 5  = 1/lambda    lambda = 1/5 = 0.2
# 10dk içerisnde gelmeme dediğine göre biz p(x>10) durumlarını incelememiz gerekiyor
# O halde her dakika için oluşan olaslıkları 1-p(x) ile buluruz.

x = sp.symbols('x')  # yeni müşteri gelme süresi.

lamb = sp.symbols('lambda')
# Exponential Distribution Formulu:
exponential = 1-(sp.exp(-x*lamb))
f = 1-exponential
# Soruyu çözebilmek için mutlaka lambda değerini bilmek gerekir

x_values=[]
y_values=[]
# x değerlerinin 0 dan büyük olması gerekiyor.
for value in range(1,10):
    y = f.subs({x:value,lamb:0.2}).evalf() # x'e karşılık gelecek olan y değerlerini bulduk
    x_values.append(value)
    y_values.append(y)
plt.plot(x_values,y_values) 

sp.plot(f.subs(lamb,0.2),(x,1,10),tittle='Exponential')
plt.show()




