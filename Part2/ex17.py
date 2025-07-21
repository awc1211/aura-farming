import random
def randomgame():
    name2 = input("What is your name: ")
    adjectives = ["Beautiful", "Smart", "Charming", "Intelligent", "Sexy", "Strong"]
    animals = ["Gorilla", "Cat", "Doggy", "Rabbit", "Deer", "Bull"]
    codename = random.choice(adjectives)
    codeanimal = random.choice(animals)
    randomnumber = random.randint(0,100)
    print(f"{name2}, your codename is: {codename} {codeanimal}")
    print(f"Your lucky number is: {randomnumber}")

randomgame()