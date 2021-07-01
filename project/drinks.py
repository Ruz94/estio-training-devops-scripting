class Drinks:
    def __init__(self, drinkChoice, drinkSize):
        self.drinkChoice = drinkChoice
        self.drinkSize = drinkSize


def setChoice(self, choice):
    self.choice = choice


def getChoice(self):
    return self.drinkChoice


def setSize(self, size):
    self.size = size


def getSize(self):
    return self.drinkSize


drinkChoices = ("Americano", "Latte", "Hot Chocolate",
                "Mocha", "Cappuccino, Macchiato")

drinkSizes = ("Small", "Medium", "Large")

counter = 0

for drink in drinkChoices:
    counter += 1
print(counter, " ", drinkChoices)
drinkChoice = int(input(
    "Please select a coffee. Americano is 1, Latte is 2, Cappucino is 3, Mocha is 4, Flat White is 5:"))

counter = 0

for size in drinkSizes:
    counter += 1
print(counter, " ", drinkSizes)
drinkSize = int(
    input("Please select a size, Small is 1, Medium is 2, Large is 3:"))

setChoice(drinkChoices[drinkChoice-1])
setSize(drinkSizes[drinkSize-1])

# self.drinkChoice = Drinks(
#     drinkChoices[drinkChoice - 1], drinkSizes[drinkSize - 1])

print("You have selected a", getSize, getChoice())
