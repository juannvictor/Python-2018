#FELIPE PENA SALES  TIA:31709850
#JUAN VICTOR        TIA:31711081
alfa = 0.01
vet = [
    [0, 0, 1],
    [0.5, 0, 0],
    [0.5, 1, 0],
    
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
