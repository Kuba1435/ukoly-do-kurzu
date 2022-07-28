# Zadej rozměry šachovnice
size = 10

# Zadej symboly
symbols = ['#', ' ']

# Vytvoř šachovnici
desk = []

# Iteruj přes řádky šachovnice a vytvoř proměnnou "line"
for row in range(size):
    line = []

# Iteruj přes jednotlivé pole v každém řádku
    for cell in range(size):

# Vytvoř index, který vybere jednu z hodnot v proměnné "symbols"
        index = (row + cell) % len(symbols)
        line.append(symbols[index])
# Přidej hotové buňky do proměnné "line"
    desk.append("".join(line))

# Vypiš výslednou šachovnici
print("\n".join(desk))
