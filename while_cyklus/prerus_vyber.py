#proměnné
ovoce = {"jablko", "banan", "citron", "pomeranc"}

#vyber z nabidky
print("Dostupné ovoce:", ", ".join(ovoce))
for ovoce_podsebou in ovoce:
    vyber = input("VYBER Z DOSTUPNÉHO OVOCE: ")

    #pokud je v nabidce
    while vyber in ovoce_podsebou:
        print("Bezva, toto ovoce je v nabídce")
        quit()
    #pokud neni v nabidce
    else:
        print("Ovoce není v nabídce")
        continue