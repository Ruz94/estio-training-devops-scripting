# from tools import Clear

coffeeTypes = ("Americano", "Latte", "Cappucino", "Mocha", "Flat White")
sizes = ("Small", "Regular", "Large")

# Clear()

exitapp = False

while exitapp == False:
    try:
        counter = 0
        for coffee in coffeeTypes:
            counter += 1
            print(counter, " ", coffee)

        coffeeChoice = int(input("Please select a coffee: "))
        if coffeeChoice < 1 or coffeeChoice > 5:
            break

        counter = 0
        for size in sizes:
            counter += 1
            print(counter, " ", size)
        sizeChoice = int(input("Please select a size: "))

        print("You selected a", sizes[sizeChoice - 1],
              coffeeTypes[coffeeChoice - 1])
    except:
        # Clear()
        print("Sorry, did not understand your selection, try again.")
