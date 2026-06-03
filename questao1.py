# (1) O maior número impar
v=[9,42,21,14,28,3,19,32,46,6]
maior_impar = -1
for numero in v:
  if numero %2!=0:
    if numero >maior_impar:
      maior_impar = numero
if maior_impar != -1:
  print("numero maior impar é ",maior_impar)
else:
  print("não existe numero")