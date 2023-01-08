import time
import random


def print_pause(story):
    print(story)
    time.sleep(2)


def intro():
    print_pause(
        "You find yourself standing in an open field,"
        "filled with grass and yellow wildflowers."
    )

    print_pause(
        "Rumor has it that a troll is somewhere around here,"
        "and has been terrifying the nearby village."
    )

    print_pause("In front of you is a house.")

    print_pause("To your right is a dark cave.")

    print_pause("In your hand you hold your trusty dagger.")

    print_pause("")


def replace(word, word1, template, chosen, chosen1):
    index = 0
    output = []
    while index < len(template):
        if template[index : index + len(word)] == word:
            output.append(chosen)
            index += len(word)
        elif template[index : index + len(word1)] == word1:
            output.append(chosen1)
            index += len(word1)
        else:
            output.append(template[index])
            index += 1
    print("".join(output))


def fight(items, chosen_monster):

    template1 = (
        "As the (monster) moves to attack,"
        "you unsheath your new (weapon)."
        "The (weapon) shines brightly in your hand"
        "as you brace yourself for the attack."
        "But the (monster) takes one look"
        "at your shiny new toy and runs away!"
        "You have rid the town of the (monster). You are victorious!"
    )
    if "sword" in items:
        replace("(monster)", "(weapon)", template1, chosen_monster, "sword")

    else:
        template3 = (
            "You do your best..."
            "but your dagger is no match for the wicked (monster)."
            "You have been defeated!"
        )
        replace("(monster)", "(weapon)", template3, chosen_monster, "sword")

    def play_again():
        play = input("do you want to play again? (y/n).\n")
        if play == "y":
            print_pause("ok! let's play again.")
            play_game()
        elif play == "n":
            print_pause("game over.")
        else:
            print_pause("I dont understand")
            play_again()

    play_again()


def run():
    print_pause(
        "you run back into the field."
        "Luckily, "
        "you don't seem to have been followed."
    )
    return choose()


def cave(items, chosen_monster):

    template4 = (
        "You peer cautiously into the cave."
        "It turns out to be only a very small cave."
        "Your eye catches a glint of metal behind a rock."
        "You have found the (weapon)"
        "You discard your silly old dagger and take the (weapon) with you."
        "You walk back out to the field"
    )
    items.append("sword")
    replace("(monster)", "(weapon)", template4, chosen_monster, "sword")
    choose()


def fight_run(items, chosen_monster):
    situation = input("Would you like to (1) fight or (2) run away?\n")
    while True:
        if situation == "1":
            return fight(items, chosen_monster)
        if situation == "2":
            return run()
        else:
            print_pause("I dont understand.")
            fight_run(items, chosen_monster)


def house(chosen_monster, items):

    template2 = (
        "You approach the door of the house."
        "You are about to knock when the door opens and out steps a (monster)."
        "Eek! This is the (monster)'s house!"
        "The (monster) attacks you! You feel a bit under-prepared for this,"
        "what with only having a tiny dagger."
    )

    replace("(monster)", "(weapon)", template2, chosen_monster, "sword")

    fight_run(items, chosen_monster)


def choose():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    global items
    items = []
    while True:
        choose = input("(Please enter 1 or 2.)\n")
        if choose == "1":
            monster = ["dragon", "gorgon", "medusa"]
            chosen_monster = random.choice(monster)
            return house(chosen_monster, items)

        elif choose == "2":
            monster = ["dragon", "gorgon", "medusa"]
            chosen_monster = random.choice(monster)
            if "sword" in items:
                print_pause(
                    "You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now."
                    "You walk back out to the field."
                )
            return cave(items, chosen_monster)

        else:
            print_pause("I don't understand")


def play_game():

    intro()
    choose()


play_game()
