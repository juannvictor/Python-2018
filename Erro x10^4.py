#FELIPE PENA SALES  TIA:31709850
#JUAN VICTOR        TIA:31711081
alfa = 0.0001
vet = [
    [0,  1],
    [3, 2],
    
    
]
n = len(vet)
rj = [1.0/n for _ in range(n)]
p = [1.0/n for _ in range(n)]

for z in range(100):
    p_old = [x for x in p]
    for i in range(n):
        pi = 0.0
        for j in range(n):
            pi += alfa * vet[i][j] * p_old[j]
        pi += (1-alfa) * rj[i]
        p[i] = pi
print(p)
