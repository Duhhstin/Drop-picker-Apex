import random
# Docks, Carrier, Oasis, Elysium, Hydroponics, Bonsai Plaza,
# Orbital Cannon, Grow Towers, Gardens, Solar Array,
# Estates, Hammond Labs, Turbine, Energy Depot,
# Power Grid, Rift
MIN = 1
MAX = 16

def main():

    #While loop to re-roll locations.
    loop = "y"
    while loop == "y" or loop == "Y":
        #If statement to control what happens on each roll.
        number = random.randint(MIN, MAX)
        if number == 1:
            print("Docks", number)

        elif number == 2:
            print("Carrier", number)

        elif number == 3:
            print("Oasis", number)

        elif number == 4:
            print("Elysium", number)

        elif number == 5:
            print("Hydroponics", number)

        elif number == 6:
            print("Bonsai Plaza", number)

        elif number == 7:
            print("Orbital Cannon", number)

        elif number == 8:
            print("Grow Towers", number)

        elif number == 9:
            print("Gardens", number)

        elif number == 10:
            print("Solar Array", number)

        elif number == 11:
            print("Estates", number)

        elif number == 12:
            print("Hammond Labs", number)

        elif number == 13:
            print("Turbine", number)

        elif number == 14:
            print("Energy Depot", number)

        elif number == 15:
            print("Power Grid", number)

        else:
            print("Rift", number)

        loop = input("Do you want to drop "
                     "somewhere else? (y=yes): ")

main()







