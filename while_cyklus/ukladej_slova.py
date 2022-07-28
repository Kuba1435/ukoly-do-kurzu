# proměnné
slova = []
# systém opakování dokud nebude proměnná obsahovat tři hodnoty
while len(slova) < 3:
    slovo = input("Zadej slovo ze čtyř: ".upper())

    # pokud je slovo na čtyři pismena
    if not slovo in slova and len(slovo) == 4:
        slova.append(slovo)
        print(f"{slovo} je uloženo")

    # pokud ne
    elif len(slovo) != 4:
        print("Slovo není dlouhé čtyři znaky")
        continue

    # pokud je již uloženo
    else:
        print("Slovo je již uloženo")
print("Už mám uložené tři slova")

# rekapitulace
print("-" * len("Už mám uložené tři slova"))
print(slova)




