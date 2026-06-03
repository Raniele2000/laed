#(2)Imaginequenósordenamososprimeiros2 /3elementosdalistaLusandooalgoritmoda bolha
#letra (a)
Sim,Isso acontece porque os intervalos se sobrepõem,
A primeira ordenação organiza a maior parte inicial da lista,
A segunda ordenação organiza a maior parte final,
Como existe uma região em comum entre os dois intervalos, os elementos “fora de posição” conseguem migrar corretamente.
A terceira ordenação corrige os possíveis problemas restantes no início da lista,
Portanto, ao final do processo, toda a lista fica ordenada.
#letra(b):
otempo de execução é o(n**2)
