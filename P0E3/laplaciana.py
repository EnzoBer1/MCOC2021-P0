from numpy import zeros, half, single, double, longdouble

def laplaciana(N):
    A = zeros((N,N), dtype = longdouble)
    
    for i in range(N):
        for j in range(i+1):
            
            if i == j:
                A[i,i] = 2
                
            elif abs(i-j) == 1:
                A[i,j] = -1
                A[j,i] = -1
    
    #print (A)
    return A


