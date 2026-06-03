#3 questão
def mediana_duas_listas(A, B):
    n = len(A)
    i = 0
    j = 0
    contador = 0
    atual = 0
    anterior = 0
    while contador <= n:
        anterior = atual
        if i < n and (j >= n or A[i] < B[j]):
            atual = A[i]
            i += 1
        else:
            atual = B[j]
            j += 1
        contador += 1
    return anterior