#proměnné
oddelovac = "=" * 62
uzivatele = {"tomas", "petr", "marek", "kuba"}
sluzby = ("dostupne filmy", "detaily filmu", "reziseri")
film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
    )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

#filmy pod jednou proměnnou
filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4
}

#Přihlášení, uvítání uživatele a vypsat nabídky
jmeno = input("Zadejte jméno: ")
if jmeno in uzivatele:
    print("V pořádku")
else:
    print("Neregistrovaný uživatel! ukončuji...")
    quit()
print(oddelovac)
print("VITEJTE V NASEM FILMOVEM SLOVNIKU!".center(62))
print(oddelovac)
print(f"| {' | '.join(sluzby)} |".center(62),)
print(oddelovac)

#Umožnit výběr služeb, výpis všech filmů a ukončení
sluzba = input("vyberte sluzbu: ")

#dostupne filmy
if sluzba in sluzby:
    if sluzba.lower() == "dostupne filmy":
        print("DOSTUPNÉ FILMY:")
        print(tuple(filmy.keys()))
        print(oddelovac)
        quit()
    #detaily filmu
    elif sluzba.lower() == "detaily filmu":
        print("DOSTUPNE FILMY:")
        print(tuple(filmy.keys()))
        film = input(f"Vyberte film:")
        print(film)
        if film in filmy:
            print(f"FILM: {film}")
            print(filmy.get(film))
            print(oddelovac)
            quit()
        else:
            print(f"Film {film} není k dispozici")
            print(oddelovac)
            quit()
    #reziseri
    elif sluzba.lower() == "reziseri":
        print(f"Režiséři:")
        print(f"{film_1['JMENO'].upper()}: {film_1['REZISER']} ")
        print(f"{film_2['JMENO'].upper()}: {film_2['REZISER']} ")
        print(f"{film_3['JMENO'].upper()}: {film_3['REZISER']} ")
        print(f"{film_4['JMENO'].upper()}: {film_4['REZISER']} ")
        print(oddelovac)
        quit()
else:
    print("Neznámá služba! ukončuji...")
    print(oddelovac)
    quit()