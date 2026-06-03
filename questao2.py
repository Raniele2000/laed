 # (2)O k-ésimo maior elemento
v=[9,42,21,14,25,3,19,33,46,6]
k=4
for i in range(k):
    maior = v[0]
    pos =0
    for j in range(len(v)):
        if v[j] > maior:
           maior =v[j]
           pos = j
    v[pos]=-2
print("maior elemento",maior)


