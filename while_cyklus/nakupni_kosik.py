#proměnné
kosik = dict()
oddelovac = ("=" * 40)
potraviny = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}
nabidka ="""+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomenrac  |    15,-  |
+-----------+----------+
"""


#Úvodní sekce s uvítáním a výpisem zboží
print("Vitejte u naseho nakupniho kosiku!".center(len(oddelovac)), oddelovac, nabidka, sep="\n")

#cyklus přidavani zbozi
while (zbozi := input("Zbozi:")) != "q":

    #pokud neni zbozi v nabidce
    if zbozi not in potraviny:
        print(f"Zbozi {zbozi} neni v nabidce")

    #pokud zbozi neni jeste v kosiku
    elif zbozi not in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi] = [potraviny[zbozi][0], 1]
        potraviny[zbozi][1] = potraviny[zbozi][1] - 1

    #pokud je zbozi v kosiku
    elif zbozi in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi][1] = kosik[zbozi][1] + 1
        potraviny[zbozi][1] = potraviny[zbozi][1] - 1

    #pokud zbozi neni skladem
    elif potraviny[zbozi][1] == 0:
        print(f"Zbozi {zbozi} neni skladem")

#vypis kosiku
print(oddelovac, kosik, sep="\n")
quit()






