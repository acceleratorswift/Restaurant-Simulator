#restaurant simulator
#class Player
#imput name
#Print welcome message and name
#give them savings
#have a random satisfaction generator
#if satisfacton is above 7, earn $10
#otherwise no money earned
#five chances given to make the dish
#if amount earned exceeds 40, +1 win
#if they get three wins:
#get to choose the gift they want-- if and else
#Bonus: individual food gets own prices?

import random
import time

name = input("Hi, what is your name?")

class Player:
    def __init__(self, name, money, wins):
        self.name = name
        self.money = money
        self.wins = wins
    def introduce(self):
        print(f"Hi {self.name}! You have ${self.money} and {self.wins} wins")

chef = Player(name, 0, 0)

menu = {
    "Popcorn Chicken": {
        "Difficulty": 4.9,
        "Chicken": 1.0,
        "Spicy": 0.5,
        "Starch": 3.0#,
#       "Price": 2.5        
    },
    "Burger": {
        "Difficulty": 5.0,
        "Bun": 2.0,
        "Tomatoes": 2.0,
        "Patty": 1.0,
        "Lettuce": 1.5
#       "Price": 3.0
    },
    "Salad": {
        "Difficulty": 3.4,
        "Romaine Lettuce": 2.0,
        "Spinach": 3.5,
        "Cucumbers": 3.0,
        "Tomatoes": 2.5,
        "Radishes": 1.5,
        "Corn": 4.0,
#       "Price": 2.5
    }
}

i = 0

print(f"Hi {name}! Welcome to your shift!")
while i < 5:
    order = random.choice(list(menu))
    difficultyLevel = menu[order]["Difficulty"] 
    satisfactionLevel = random.randint(1, 10)
    input("Press Enter to see order.")
    print(f"Here is the order: {order}. The difficulty level is {difficultyLevel}/5")
    input("Press Enter to see ingredients required.")
    print("Here are the ingredients needed: ")
    for ingredient, amount in menu[order].items():
        if ingredient != "Difficulty":
            print(f"{ingredient}: {amount}")

    print("Have fun making the food!")
    input("Press Enter when you are ready to serve the food")
    print("Serving...")
    time.sleep(2)
    print("The customer is eating...")
    time.sleep(2)
    print("The customer is evaluating...")
    time.sleep(2)
    input("Press Enter to see satisfaction level.")
    print(f"The satisfaction level is {satisfactionLevel}/10.")
    if satisfactionLevel >= 7:
        chef.money += 10
        print(f"Well done! You have earned $10! Your balance is ${chef.money}.")
    else:
        print(f"Try next time! Your balance is ${chef.money}.")
    i += 1
print("Calculating total balance...")
time.sleep(2)
if chef.money >= 40:
    chef.money += 1
    print(f"Good Job! You have earned ${chef.money}! You have added one win! Your total wins now: {chef.wins}.")
else:
    print(f"Oh no, you only earned ${chef.money}... You did not add any wins. Your total wins now: {chef.wins}.")