import random

partier = ["Arbeiderpartiet", "Fremskrittspartiet", "Høyre", "Sosialistisk Venstreparti", "Senterpartiet", "Rødt", "Miljøpartiet De Grønne", "Kristelig Folkeparti", "Venstre", "Blankt"]
sannsynlighet = [28, 24.4, 15.4, 6, 6, 6, 5, 5, 4, 1]
forkortelse = ["AP", "FRP", "H", "SV", "SP", "R", "MDG", "KRF", "V", "B"]
stemmer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
velgere = list(range(1, 4058875))
flest = -1
flestIndex = -1

def regne_prosent(stemmer):
    total = sum(stemmer)
    prosent = stemmer[i]
    svar = (prosent / total) * 100
    svar = round(svar,2)
    return svar

# Valgsimulering

for i in velgere:
    parti = random.choices(partier, weights=sannsynlighet, k=1)[0]
    for i in range(len(partier)):
        if parti == partier[i]:
            stemmer[i] += 1

print("Dette er resultatet: ")
for i in range(len(partier)):
    print(f"{partier[i]}: {stemmer[i]}")

print("\nStemmer per parti i prosent")
for i in range(len(stemmer)):
    print(f"{forkortelse[i]}: {regne_prosent(stemmer)} %")

for i in range(len(stemmer)):
    if stemmer[i] > flest:
        flest = stemmer[i]
        flestIndex = i
print(f"\nPartiet med flest stemmer ble {partier[flestIndex]} med {flest} stemmer")

"""
# Valg med brukerinput

should_continue = True

print("\n    Stortingsvalg    ")
print(f"Dette er partiene du kan stemme på: \n {partier}")

while should_continue:
    parti = input("Hvilket parti vil du stemme på? \n").capitalize()

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

