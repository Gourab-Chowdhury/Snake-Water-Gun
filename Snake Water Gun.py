'''Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.'''

import random
word = ['snake', 'water', 'gun']

a = input("Enter your choice(Snake, Water, Gun): ").lower()
b = random.choice(word)
print(f"Computer chooses {b}")

if a == b:
    print("The Match is draw")
elif a == 'gun' and b == 'snake':
    print("The gun beats the snake. You Won")
elif a == 'water' and b == 'gun':
    print("The water beats the gun. You Won")
elif a== 'snake' and b == 'water':
    print("The snake beats the water. You Won")
else:
    print("You Loss.")