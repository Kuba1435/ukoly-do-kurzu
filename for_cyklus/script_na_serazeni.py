# Zadaná proměnná
names = [
    'Michal', 'Pepa', 'Honza',
    'Pavel', 'Lukas', 'Matej',
    'Iva', 'Klara', 'Jana',
    'Honza', 'Vasek','Milan',
    'Michal'
]
sorted_names = list()

# Iterace přes všechna jména v seznamu "names"
for index, name in enumerate(names):

    # Pokud jde o první index seznam "names" potom jej pouze přidej
    if index == 0:
        sorted_names.append(name)
    else:

        # Pokud nejde o první index, iteruj přes seřazená jména
        for inner_index, sorted_name in enumerate(sorted_names):

            # Pokud je neseřazené jméno menší než seřazené..
            if name < sorted_name:

                # .. vlož jej na aktuální index a skončí vnitřní iteraci
                sorted_names.insert(inner_index, name)
                break

        # Pokud jsi prošel všechna seřazená jména, vlož neseřazené nakonec
        else:
            sorted_names.append(name)

# Vypiš seznam seřazených jmen
print(sorted_names)