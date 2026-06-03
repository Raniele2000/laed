#5 questão
def verificar_linhas_iguais(matriz):
    iguais = False
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            linha_igual = True
            for k in range(len(matriz[i])):

                if matriz[i][k] != matriz[j][k]:
                    linha_igual = False
            if linha_igual == True:
                print("Sim, as linhas", i, "e", j, "são iguais")
                iguais = True
                return
    if iguais == False:
        print("Não existem linhas iguais")