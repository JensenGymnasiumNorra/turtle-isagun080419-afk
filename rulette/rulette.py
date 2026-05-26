import random

saldo = 100

print("Välkommen till Roulette!")
print("Du börjar med 100 kr.")

while saldo > 0:
    print(f"Ditt saldo: {saldo} kr")

    satsning = int(input("Hur mycket vill du satsa? "))

    if satsning <= 0 or satsning > saldo:
        print("Ogiltig satsning!")
        continue

    nummer = int(input("Välj ett nummer mellan 0 och 36: "))

    if nummer < 0 or nummer > 36:
        print("Numret måste vara mellan 0 och 36!")
        continue

    roulette_nummer = random.randint(0, 36)

    print(f"Rouletten landade på: {roulette_nummer}")

    if nummer == roulette_nummer:
        vinst = satsning * 35
        saldo += vinst
        print(f"Du vann {vinst} kr!")
    else:
        saldo -= satsning
        print("Du förlorade!")

    print()

    fortsätt = input("Vill du spela igen? (ja/nej): ").lower()

    if fortsätt != "ja":
        break

print(f"Spelet är slut! Du har {saldo} kr kvar.")