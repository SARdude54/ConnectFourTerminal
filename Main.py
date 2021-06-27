from Game import Game

print("Welcome to Connect Four.")
print('Type "Start" to begin. Type "Exit" to exit')
isResponding = True

while isResponding:
    response = input(">")
    if response.lower() == "Start".lower():
        g = Game()
        g.init_Game()
        isResponding = False

    elif response.lower() == "Exit".lower():
        print("Exiting the game")
        isResponding = False

    else:
        print("Please enter a valid command")
