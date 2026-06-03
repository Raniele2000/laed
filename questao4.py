#4 questão
def verificar_elementos_iguais(matriz):
    repetido = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            for a in range(len(matriz)):
                for b in range(len(matriz[x])):

                    if i != a or j != y:
                        if matriz[i][j] == matriz[a][b]:
                            print("Sim, o elemento", matriz[i][j], "aparece mais de uma vez")
                            repetido = True
                            return
    if repetido == False:
        print("Não existem elementos repetidos")
