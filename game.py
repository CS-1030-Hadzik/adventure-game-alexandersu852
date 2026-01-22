"""
Adventure Game
Author: Alex Su
Version: 1.0
Description:
Text-based choose your own adventure game
Navigate through a strange mechanical world.
"""



# Welcome message and introduction
print("Welcome to the Adventure Game!") 
print("Your journey begins here...")

# Ask for the player's name
player_name = input("What is your name, adventurer? ")

# Concatenated strings for personalized message, with f-strings for readability
print (f"Welcome, {player_name}! Your journey begins now.")

# Describe setting
starting_area = """
You open your eyes.
You're on some bridge in the sky, giant mechanical cogs stretch down below you.
A mechanical planet of sorts.
In front of you lies an elevator, descending into the world...
"""
print(starting_area)

# Ask player their first decision
decision = input("Do you wish to take the elevator? (yes or no): ").lower()

# Respond based on player's decision
if decision == "yes":
    print (f"Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print (player_name + ", you decide to wait. Perhaps courage will find you later.")
else: 
    print("Unsure of what to do, you stare at the planet below for a while longer...")