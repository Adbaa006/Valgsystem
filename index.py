partier = ["Arbeiderpartiet", "Fremskrittspartiet", "Høyre", "Sosialistisk Venstreparti", "Senterpartiet", "Rødt", "Miljøpartiet De Grønne", "Kristelig Folkeparti", "Venstre"]
forkortelser = ["ap", "frp", "h", "sv", "sp", "r", "mdg", "krf", "v"]
stemmer = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def flest_stemmer(stemmer):
    størst = stemmer[0]
    for stemme in stemmer:
        if stemme > størst:
            størst = stemme
    return størst

while True:
    print("=== Stortingsvalg ===")
    print(f"Dette er partiene du kan stemme på: \n {partier}")
    parti = input("Hvilket parti vil du stemme på? \n").lower()
    if input == "Arbeiderpartiet":
        print(f"Godt valg. Du stemte {parti}")
    else: 
        print("Stem igjen")