#zadané hodnoty
sequence = [2, 3, 5, 1, 6, 4, 8, 7]
counts = {}

# Cyklus, který spočítá jednotlivé výskyty čísel
for cislo in sequence:

# .. pokud číslo není uložené, eviduj jej jako první hodnotu
    if cislo not in counts:
        counts[cislo] = 1

# .. pokud číslo je uložené, inkrementuj původní hodnotu
    else:
        counts[cislo] = counts[cislo] + 1

# Setřiď podle klíče a vypiš seřazené hodnoty
for key, value in sorted(counts.items()):
    print(f"key: {key} value: {value}")