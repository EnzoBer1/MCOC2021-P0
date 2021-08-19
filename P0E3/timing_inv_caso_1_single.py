from time import perf_counter
from numpy import zeros
import numpy as np
from laplaciana import laplaciana
import matplotlib.pyplot as plt

Ns = [10,20,50,100,200,500,1000,1500,2000,5000]

corridas = [1,2,3,4,5,6,7,8,9,10]

dts_inversion = [] #guardo los tiempos en que se invierte la matriz por corrida
mems = [] #guardo los bytes usados para invertir la matriz por corrida

txt = open("timing_inv_caso_1_single.txt","w")

for corrida in corridas:
    for N in Ns:
        
    
        t1= perf_counter()
        A = laplaciana(N)
        t2 = perf_counter()
        Am1 = np.linalg.inv(A) #matriz inversa de A
        t3 = perf_counter()
        bytes_total = A.nbytes + Am1.nbytes
        
        
        dt_ensamblaje = t2 - t1
        dt_inversion = t3 - t2 #presentar tiempo de inversion en graf.
        
        
        dts_inversion.append(dt_inversion)
        mems.append(bytes_total)
        
        txt.write(f"N = {N}; Tiempo inversión = {dt_inversion} seg.; Uso de memoria = {bytes_total} bytes\n" )
        
        print ("N =",N)
        print (f"Uso memoria: {bytes_total} bytes")
        print (f"Tiempo ensamblaje: {dt_ensamblaje} seg")
        print (f"Tiempo inversion: {dt_inversion} seg")
        print ("----------------------------------------------------")
     
txt.close()

def separar_lista(lista,n):
    tiempos_grafico = []
    tiempos_grafico.append([lista[i*n:i*n+n] for i in range(n)])
    return tiempos_grafico

x1 = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y1 = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]

tiempo1 = [0.1/1000,1/1000,10/1000,0.1,1,10,60,60*10]
memoria1 = [1*10**3,10*10**3,100*10**3,1*10**6,10*10**6,100*10**6,1*10**9,10*10**9]
tamaño1 = [10,20,50,100,200,500,1000,2000,5000,10000,20000]


for i in range(len(corridas)):
    
    
    plt.subplot(2,1,1)
    plt.loglog(Ns,dts_inversion[i*10:i*10+10],"-o")
    plt.xticks(tamaño1,x1)
    plt.yticks(tiempo1,y1)
    plt.xlim(right=20000)
    plt.grid()
    plt.ylabel("Tiempo inversión (s)")
    
    plt.subplot(2,1,2)
    plt.loglog(Ns,mems[i*10:i*10+10],"-o")
    plt.xticks(tamaño1,x1)
    plt.yticks(memoria1,y2)
    plt.grid()
    plt.ylabel("Uso memoria")
    plt.xlabel("Tamaño matriz N")
    plt.xlim(right=20000)
    plt.hlines(y=10**8,xmin=0,xmax=2000,linestyle="--")
    
    
                             
plt.show()                         









#la forma en que se escribe una función afecta el desempeño





