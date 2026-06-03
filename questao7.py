# (7)Contando inversões
lista=[9,2,7,7,2,2,1,7,7,9]
contador=0
for i in range(len(lista)):
  for j in range(i+1,len(lista)):
    if lista[i]>lista[j]:
      contador+=1
print("quantidade de inversões:",contador)