partier = ["Arbeiderpartiet", "Fremskrittspartiet", "Høyre", "Sosialistisk Venstreparti", "Senterpartiet", "Rødt", "Miljøpartiet De Grønne", "Kristelig Folkeparti", "Venstre"]
stemmer = [0, 0, 0, 0, 0, 0, 0, 0, 0]
svar1 = ["Arbeiderpartiet", "Fremskrittspartiet", "Høyre", "Sosialistisk Venstreparti", "Senterpartiet", "Rødt", "Miljøpartiet De Grønne", "Kristelig Folkeparti", "Venstre"]
svar2 = ["arbeiderpartiet", "fremskrittspartiet", "høyre", "sosialistisk venstreparti", "senterpartiet", "rødt", "miljøpartiet de grønne", "kristelig folkeparti", "venstre"]
svar3 = ["ap", "frp", "h", "sv", "sp", "r", "mdg", "krf", "v"]

while True:
    print("=== Stortingsvalg ===")
    print(f"Dette er partiene du kan stemme på: \n {partier}")
    print(input("Hvilket parti vil du stemme på? \n"))
    if input == svar1:
        print("Godt valg!")
'''    
    elif input == svar2:
        print("Takk for din stemme!")

    elif input == svar3:
        print("Kom deg hjem nå")

    else:
        print("Ugyldig stemme, velg et parti \n")
'''