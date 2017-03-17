# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Main Character")
define e = Character ("Egglord")
define s = Character ("Shy Meme")
define l = Character ("Loli")
define t = Character ("Tsundere")
define y = Character ("Yandere")
define c = Character ("Chicken Manager")
define a = Character ("Aubergine")


# The game starts here.

label start:
    
    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "My name is Omelette. I live on Easter Island."

    e "I've just started working at this cafe. It's alright, the manager is a little weird, but he said I'd like the other employees."

    e "My first day is tomorrow. Let's see how things go."

    scene # insert cafe bg
    with fade
    
    "My first day. 
    
    # This ends the game.

    return
