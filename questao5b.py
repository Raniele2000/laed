# 5) letra b) lista ordenada
lista=[9,42,21,14,25,3,19,33,45,6]
encontrou = False
for num in lista:
  if num *2 in lista:
    print("encontrados",num,"e",num *2)
    encontrou=True
    break
if not encontrou:
  print("não encontrado")



