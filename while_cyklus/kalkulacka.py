#prommene
mod = True
#nekonecna smycka
while mod:
    operatori = {"+", "-", "*", "/", "off"}
    choice = input("""
Sčítání:    "+"
Odčítání:   "-"
Násobení:   "*"
Dělení:     "/"
Ukonči:     "off"
----------------------
Vyber si operaci: """
)
    #pokud uzivatel zada hodnotu off
    if choice.lower() == "off":
        print("Počtům zdar!")
        mod = False
        quit()

    #pokud je vyber v nabidce vyzada dve cisla
    elif choice in operatori:
        number_1 = input("Zadejte první číslo: ")
        number_2 = input("Zadejte druhé číslo: ")

        #pokud hodnota neni cislo
        if not number_1.isnumeric() or not number_2.isnumeric():
            print("Zadadé hodnoty nejsou čísla!")

        #pokud je hodnota cislo tak jej vypocita
        else:
                calculation = " ".join((number_1, choice, number_2))
                print(number_1, choice, number_2, "=", eval(calculation))
                print("======================")
                quit()

    #pokud neni hodnota v nabidce
    else:
        print(f"{choice} není v nabídce")
