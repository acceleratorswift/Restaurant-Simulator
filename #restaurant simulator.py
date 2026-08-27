#restaurant simulator
#class Player
#imput name
#Print welcome message and name
#give them savings
#have a random satisfaction generator
#if satisfacton is above 7, earn $10
#otherwise no money earned
#five chances given to make the dish
#if amount earned exceeds 40, they win best employee of the month
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
    # def introduce(self):
    #     print(f"Hi {self.name}! You have ${self.money} and {self.wins} wins")

    # introduce(self.name)

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
while i <= 5:
    print(f"Hi {name}! Welcome to shift {i}!")
