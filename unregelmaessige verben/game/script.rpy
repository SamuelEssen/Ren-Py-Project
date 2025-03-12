# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Julia", color="#f7f7f7")
define m = Character("Marie", color="#1c4622")
define v = Character("Valerie", color="#b33b95")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Julia ist nach Klagenfurt Deutsch zu lernen gekommen."

    j "Soooo, Ich bin endlich gekommen!"
    j "Jetzt brauch ich Marie finden. Sie muss schon hier sein."

    # This ends the game.


label meeting:
    scene bg room

    show Marie

    show Valerie

    m "Julia, wir sind hier!"

    j "Oh, hallochen!"

    v "Hey! Wir haben auf dich schon zwanzig Minuten gewartet."

    j "Sorry, unser Zug so langsam gefahren. Deshalb sind wir so spät angekommen."

    v "Nah! Alles gut. Macht nichts."

    j "Danke, dass ihr mich geholt haben."

    m "Kein Problem, Babe. Wir sind Freunde." 
    m "Außerdem haben wir heute frei and wir haben wir dich vermisst."

    return