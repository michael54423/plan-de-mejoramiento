#plan de mojoramiento de evaluacion
#tema a 
#punto 1


import random
import math

cod_maximo=511
cod_minimo=0

vol_maximo=6
vol_minimo=0

N=1000
A=[]
for i in range(N):
    val=random.randint(0,511)
    A.append(val)
    
    print(i,val)

maxima_medicion=max(A)
minima_medicion=min(A)

A.sort(reverse=False)
maxima_medicion=A[-1]
minima_medicion=A[0]

print("maximo=",maxima_medicion)
print("minima=",minima_medicion)

a=vol_minimo
b=vol_maximo/cod_maximo

maximo_voltaje=b*maxima_medicion+a
minimo_voltaje=b*minima_medicion+a

print("v maximo=",maximo_voltaje)
print("v minimo",minimo_voltaje)
suma=0

for i in range(len(A)):
    suma=suma+A[i]
promedio=suma/len(A)

print("el promedio es=",promedio*b+a)

#3punto



def pylance(suma_cuadrados):
 cuadrados=[]
 for i in range(len(A)):
    cuadrados.append(A[i]**2)
    suma_cuadrados=suma_cuadrados+cuadrados[i]

 valor_rms=math.sqrt(suma_cuadrados/len(A))

 print("el valor del rms es=",valor_rms*b+a)
 print(A)


        