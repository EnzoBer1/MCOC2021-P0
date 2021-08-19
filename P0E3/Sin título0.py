from scipy import linalg
from laplaciana import laplaciana
from time import perf_counter
import numpy as np

Ns = [10,100,1000]
dts_inversion = [] #guardo los tiempos en que se invierte la matriz
mems = [] #guardo los bytes usados para invertir la matriz


for N in Ns:
   
    t1= perf_counter()
    A = laplaciana(N)
    t2 = perf_counter()
    #Am1 = linalg.inv(A, overwrite_a = False) #matriz inversa de A
    Am1 = np.linalg.inv(A)
    t3 = perf_counter()
    
    bytes_total = A.nbytes + Am1.nbytes
    
    
    dt_ensamblaje = t2 - t1
    dt_inversion = t3 - t2 #presentar tiempo de inversion en graf.
    
    dts_inversion.append(dt_inversion)
    mems.append(bytes_total)
    
    
    print ("N =",N)
    print (f"Uso memoria: {bytes_total} bytes")
    print (f"Tiempo ensamblaje: {dt_ensamblaje} seg")
    print (f"Tiempo inversion: {dt_inversion} seg")
    print ("----------------------------------------------------")
    
    
    
