# Iterace čísel od 1 do 100
for cislo in range(1, 101):

# pokud je číslo násobek 3 a současně 5
    if cislo % 15 == 0:
        print("Fizz Buzz")
# pokud je číslo násobek 3
    elif cislo % 3 == 0:
        print("Fizz")

# pokud je číslo násobek 5
    elif cislo % 5 == 0:
        print("Buzz")

# pokud jde o jakékoliv jiné číslo
    else:
        print(cislo)