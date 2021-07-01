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
drinkChoice = int(input("What drink would you like: "))

counter = 0

for size in drinkSizes:
    counter += 1
print(counter, " ", drinkSizes)
drinkSize = int(input("What size would you like: "))

setChoice(drinkChoices[drinkChoice-1])
setSize(drinkSizes[drinkSize-1])

# self.drinkChoice = Drinks(
#     drinkChoices[drinkChoice - 1], drinkSizes[drinkSize - 1])

print("You have selected a", getSize, getChoice())
