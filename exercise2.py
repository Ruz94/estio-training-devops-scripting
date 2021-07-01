userName = input("Enter your name: ")
userNum = int(input("Enter a random number: "))

if isinstance(userName, str) and isinstance(userNum, int):
    print("Name:", userName, "Number:", userNum)
