# (1) O terceiro maior elemento
v=[9,42,21,14,28,3,19,33,46,6]
terceiro_maior = -1
for numero in v:
  if numero %2!=0:
    if numero > terceiro_maior:
      terceiro_maior = numero
if terceiro_maior!= -1:
  print("numero maior impar é ",terceiro_maior)
else:
  print("não existe numero")