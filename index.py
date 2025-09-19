import random

partier = ["Arbeiderpartiet", "Fremskrittspartiet", "Høyre", "Sosialistisk Venstreparti", "Senterpartiet", "Rødt", "Miljøpartiet De Grønne", "Kristelig Folkeparti", "Venstre", "Blankt"] # Liste med partier
sannsynlighet = [28, 24.4, 15.4, 6, 6, 6, 5, 5, 4, 1] # Sannynlighet for at partiet velges, gir elementet en vekt og vekten sees på i forhold til hverandre
forkortelse = ["AP", "FRP", "H", "SV", "SP", "R", "MDG", "KRF", "V", "B"] # Partienes forkortelser, for forenkling både ved input og print
stemmer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Liste med stemmer for hvert parti
velgere = list(range(1, 4058875)) # Antall velgere, "valget" kjøres en gang per velger
flest = -1 # Verdi til variabelen "flest" til senere kode
flestIndex = -1 # Verdi til variabelen "flestIndes" til senere kode

# Funksjon for å regne ut prosent
def regne_prosent(stemmer):
    total = sum(stemmer) # Total tilsvarer summen av stemmene
    prosent = stemmer[i] # Prosent tilsvarer hver av stemmene i lista
    svar = (prosent / total) * 100 # Gir "svar" verdi ved å regne ut prosent med verdiene prosent og total har gjennom lista
    svar = round(svar,2) # Avrunder svaret til to desimaltall
    return svar # Returnerer "svar" med verdien

# Valgsimulering
for i in velgere: # Sier at følgene skal utføres for hver av elementene i listen "velgere"
    parti = random.choices(partier, weights=sannsynlighet, k=1)[0]
    # Random.choices lager en liste med elementer, her skal den ta utgangspunkt i elementene i "partier" og vekten de har i "sannsynlighet"
    # Ettersom random.choices lager en liste med mulige utfall, brukes k=1 for å bestemme antall utfall, i dette tilfellet skal listen inneholde ett element
    # [0] sier at du vil benytte element 0 i listen, så selv om k=1 gir deg ett element, vil [0] hente ut elementet så du ikke ser det som et element i en liste, men et frittstående element
    for i in range(len(partier)): # Sier at følgende skal benytte hele lengden på lista "partier"
        if parti == partier[i]: # Sammenligner inputen med partiene for å se om de matcher
            stemmer[i] += 1 # Dersom input matcher med et parti vil stemmen med samme plassering i lista som partiet få en stemme

print("Dette er resultatet: ")
for i in range(len(partier)): # Sier at følgene skal benytte hele lengden av lista "partier"
    print(f"{partier[i]:<27}: {stemmer[i]}") # Den skal printe hvert av partiene fra lista med deres tilsvarende stemme

print("\nStemmer per parti i prosent")
for i in range(len(stemmer)): #Sier at følgende skal benytte hele lengden av lista "stemmer"
    print(f"{forkortelse[i]:<5}: {regne_prosent(stemmer)} %") # Den skal printe hver av forkortelsene med deres tilsvarende prosent med svarene fra funksjonen som regner ut prosentandelen 

for i in range(len(stemmer)): #Sier at følgende skal benytte hele lengden av lista "stemmer"
    if stemmer[i] > flest: # Sammenligner verdiene i lista "stemmer" med verdien til variabelen "flest"
        flest = stemmer[i] # Dersom en verdi i lista er større enn "flest" vil den bli den nye verdien til "flest, dette gjøres helt til "flest" har tatt den høyeste verdien i lista, altså finnes det ikke flere elementer i lista som er høyere og man har funnet det høyeste tallet
        flestIndex = i # Knytter verdien til "flest" tatt fra lista opp mot en plassering
print(f"\nPartiet med flest stemmer ble {partier[flestIndex]} med {flest} stemmer") # FlestIndex bruker plasseringen til å finne riktig plassering i lista med partier

"""
# Valg med brukerinput

should_continue = True # Gir verdien True som betyr at den kjører

print("\n    Stortingsvalg    ")
print(f"Dette er partiene du kan stemme på: \n {partier}")

while should_continue: # Mens should_contine er True kjører følgende kode
    parti = input("Hvilket parti vil du stemme på? \n").capitalize() # Ber om brukerinput til å velge et parti, .capitalized() sier at inputen alltid skal få stor forbokstav, for å korrespondere med hvordan det er skrevet i lista

    for i in range(len(partier)): # Samme kode som brukt tidligere 
        if parti == partier[i]:
            stemmer[i] += 1

    for i in range(len(forkortelse)): # Samme kode som den over, bruker bare elementer i lista "forkortelse istedenfor"
        if parti == forkortelse[i]:
            stemmer[i] += 1
   
    if parti in partier:
        print(f"Du stemte {parti}, takk for at du stemte") # Hvis inputen er et element i lista, printer den dette med hvilket parti bruker skrev i inputen

    elif parti in forkortelse:
        print(f"Du stemte {parti}, takk for at du stemte") # Samme som over, men benytter lista "forkortelser istedenfor"

    elif parti == "vis resultat":
        should_continue = False # Endrer verdien til should_continue til False, noe som stopper while-løkken

    elif parti not in partier:
        print(f"Vennligst velg et parti \nDette er partiene du kan stemme på: \n {partier}") # Sir ifra om inputen ikke stemmer med elementer i lista og ber bruker skrive inn på nytt

print("Dette er resultatet: ")
for i in range(len(partier)):
    print(f"{partier[i]}: {stemmer[i]}") # Samme kode som forklart tidligere
          
print(f"Partiet som vant fikk {flest_stemmer(stemmer)} stemmer") # Mindre kompleks versjon av tidligere forklart kode

print("Stemmer per parti i prosent")
for i in range(len(stemmer)):
    print(regne_prosent(stemmer)) # Mindre kompleks versjon av tidligere forklart kode
"""

