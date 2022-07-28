# Zadaná proměnná
result = []

# Vstup uživatele
user_input = input("Hello, please write your numbers separated by commas and press enter to confirm:")

# Rozdělené hodnoty schované v proměnné "numbers"
numbers = user_input.split(',')

# Jednotlivé hodnoty projdi
for number in numbers:

# .. očisti od mezer a ulož do proměnné "result"
    clean = int(number.strip())
    result.append(clean)

# Nakonec výsledek vypiš s doplňujícím textem "List:"
print(f"List: {result}")