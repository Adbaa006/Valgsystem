stemmer = [3, 5, 6, 2, 7]
flest = -1

for i in range(len(stemmer)):
    if stemmer[i] > flest:
        flest = stemmer[i]

print(flest)