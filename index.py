import random

partier = ["arbeiderpartiet", "fremskrittspartiet", "høyre", "sosialistisk venstreparti", "senterpartiet", "rødt", "miljøpartiet de grønne", "kristelig folkeparti", "venstre"]
forkortelse = ["ap", "frp", "h", "sv", "sp", "r", "mdg", "krf", "v"]
stemmer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
velgere = list(range(1, 4058875))

def flest_stemmer(stemmer):
    stemmer.sort()
    siste = stemmer.pop()
    return siste


def regne_prosent(stemmer):
    total = sum(stemmer)
    prosent = stemmer[i]
    svar = (prosent / total) * 100
    round(svar,2)
    return svar

for i in velgere:
    parti = random.choice(partier)
    for i in range(len(partier)):
        if parti == partier[i]:
            stemmer[i] += 1


print("Dette er resultatet: ")
for i in range(len(partier)):
    print(f"{partier[i]}: {stemmer[i]}")

print("Stemmer per parti i prosent")
for i in range(len(stemmer)):
    print(f"{regne_prosent(stemmer)}%")

print("Partiet med flest stemmer")
print(flest_stemmer(stemmer))

"""
should_continue = True

print("\n    Stortingsvalg    ")
print(f"Dette er partiene du kan stemme på: \n {partier}")

while should_continue:
    parti = input("Hvilket parti vil du stemme på? \n").lower()

    for i in range(len(partier)):
        if parti == partier[i]:
            stemmer[i] += 1

    for i in range(len(forkortelse)):
        if parti == forkortelse[i]:
            stemmer[i] += 1
   
    if parti in partier:
        print(f"Du stemte {parti}, takk for at du stemte")

    elif parti in forkortelse:
        print(f"Du stemte {parti}, takk for at du stemte")

    elif parti == "vis resultat":
        should_continue = False

    elif parti not in partier:
        print(f"Vennligst velg et parti \nDette er partiene du kan stemme på: \n {partier}")

print("Dette er resultatet: ")
for i in range(len(partier)):
    print(f"{partier[i]}: {stemmer[i]}")
          
print(f"Partiet som vant fikk {flest_stemmer(stemmer)} stemmer")

print("Stemmer per parti i prosent")
for i in range(len(stemmer)):
    print(regne_prosent(stemmer))
"""