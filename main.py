# Creator: Daj Kaspers
# GuessNumber game
# Creation Date: 31/5/2021 

# Import random for random generated number
import random

# Input fields
keuzeGetal1 = int(input("Vanaf welk getal "))
keuzeGetal2 = int(input("Tot welk getal "))
aantalRaden = int(input("Hoeveel keer mag je raden? "))

# Create random generated number
willekeurigGetal = random.randint (keuzeGetal1, keuzeGetal2)

# Set variables
gekozenGetal = 0
aantalRaden1 = 1
geraden = [""]

# While loop if the generated number is not guessed keep going until max guesses is hit
while (gekozenGetal != willekeurigGetal):
    gekozenGetal = int(input("\nGeef een getal tussen " + str(keuzeGetal1) + " en " + str(keuzeGetal2) + ": "))
    geraden.append(gekozenGetal)
    if gekozenGetal < keuzeGetal1:
        print ("voer een getal in wat hoger is dan " + str(keuzeGetal1))
    if gekozenGetal > keuzeGetal2:
        print ("voer een getal in wat lager is dan " + str(keuzeGetal2))

    if gekozenGetal < willekeurigGetal:
        print ("Hoger")
    if gekozenGetal > willekeurigGetal:
        print ("Lager")
    if gekozenGetal == willekeurigGetal:
        print("Correct")

    if aantalRaden1 == aantalRaden:
        print("\nMaximaal aantal keer geraden!")
        del geraden[0]
        print("Het raad-getal was " + str(willekeurigGetal) + " \nhieronder een overzicht van uw invoer: " + str(geraden))
        break
    aantalRaden1 += 1
