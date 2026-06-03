#(6)Os dois elementos mais próximos
lista=[9,2,7,7,2,2,1,7,7,9]
menor_dif= abs(lista[0]- lista[1])
a = lista[0]
b=lista[1]
for i in range(len(lista)-1):
  for j in range(i + 1,len(lista)):
     dif = abs(lista[i + 1] - lista[i])
     if dif < menor_dif:
        menor_dif = dif
        a=lista[i]
        b=lista[j]
print("elementos mais proximos ", a ,"e", b )
print("diferença",menor_dif)