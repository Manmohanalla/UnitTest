a=['ab','bd','cd']
b=['ab','cd','bd']
print [i for i, j in zip(a, b) if i == j]

