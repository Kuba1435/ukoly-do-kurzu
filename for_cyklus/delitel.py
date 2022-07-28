#proměnné
result = []

#vstupní hodnoty
start = input("Zadejte počáteční hodnotu: ")
stop = input("Zadejte koncovou hodnotu: ")
divisor = input("Zadejte dělitele: ")

#ověření vstupu
if start.isnumeric() and stop.isnumeric() and divisor.isnumeric():
    for number in range(int(start), int(stop) + 1):
        if number % int(divisor) == 0:
            result.append(number)
            print(f"Čísla v rozsahu ( {start},{stop} ) dělitelná {divisor}:")
            print(result)
else:
    print("Zadané hodnoty musejí být číselného výrazu!")
    quit()



