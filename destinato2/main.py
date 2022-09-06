#proměnné
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 35
cara = "-" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
AKT_ROK = 2021

#Pozdrav a výpis
print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(dvojita_cara)
print(nabidka)
print(dvojita_cara)

#Výběr z nabídky destinací
destinace = input("CISLO DESTINACE:")
vybrana_destinace = mesta[int(destinace) - 1]

#destinace
if int(destinace) <= 6 and int(destinace) >= 1:
    print(f"DESTINACE: {vybrana_destinace}")
# elif int(destinace) > 6
else:
    print(f"VYBRANA DESTINACE {destinace} NEEXISTUJE! UKONCUJI...")
    quit()
print(cara)

#přepočítání slevy
if vybrana_destinace in slevy:
    nova_cena = ceny[int(destinace) - 1] * 0.75
    print(f"ZISKAVATE 25% SLEVU! CENA: {nova_cena}")
    print(cara)
else:
    nova_cena = ceny[int(destinace) - 1]

#ověřit jméno
jmeno = input("ZADEJTE JMENO: ")
prijmeni = input("ZADEJTE PRIJMENI: ")
print(cara)

if jmeno.isalpha() and prijmeni.isalpha():
    print(f"Cele jmeno: {jmeno} {prijmeni}")
    print(cara)

else:
    print("Jmeno nebo prijmeni nejsou v poradku! Ukoncuji..")
    quit()

#email
email = input("ZADEJTE EMAIL: ")

#ověření emailu
if "@" in email and email.split("@")[1] in domeny:
    print("Email je v poradku")
else:
    print(cara)
    print("Neplatna emailova adresa. Ukoncuji..")
    quit()
print(dvojita_cara)

#rekapitulace
print(f"Děkuji {jmeno} za objednávku.")
print(f"DESTINACE: {vybrana_destinace}")
print(f"Na tvůj mail: {email} jsme ti poslali lístek.")
quit()


