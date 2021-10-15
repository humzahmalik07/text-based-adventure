import action
import Character
import os
import sys
import intro

inventory_input = input("Batman or Green Lantern: ")

# This inventory is paired with specific characters
inventory = {"Batman": {"Night Vision Goggles":
                        {"description": "Use the Night Vision Goggles to see in the dark and find your way",
                         "damage": 0, "protection": 0},
                         },
             "Green Lantern": {"Power Ring":
                           {"description":
                            "Use this ring as a flashlight to find their way",
                            "damage": 0, "protection": 0}}
             }


# This function defines the player inventory


def player_inventory(player, inventory):
    """Print out the inventory for the choosen character"""
    protection_items = []
    weapons = []
    for item in inventory[player]:
        description = inventory[player][item]["description"]
        damage = inventory[player][item]["damage"]
        protection = inventory[player][item]["protection"]
        print(f"{player}'s {item} - {description}")
        print(f"damage: {damage}")
        print(f"protection: {protection}")
        if protection != 0 and damage == 0:
            protection_items.append(item)
        elif damage != 0:
            weapons.append(item)
    return protection_items, weapons

while True:
    if inventory_input == "Batman":
        intro.introduction()
        player_inventory("Batman", inventory)
        Character.character_intro()
        action.action_1()
        action.action_2()
        action.action_3()
        action.action_4()
        action.action_5()
        action.action_6()
        action.action_7()
        action.action_8()
        action.action_9()
        action.action_9()
        quit()
    if inventory_input == "Green Lantern":
        intro.introduction()
        player_inventory("Green Lantern", inventory)
        Character.character_intro_2()
        action.actions_1()
        action.actions_2()
        action.actions_3()
        action.actions_4()
        action.actions_5()
        action.actions_6()
        action.actions_7()
        action.actions_8()
        action.actions_10()
        quit()
    else:
        print("invalid action")
        os.execl(sys.executable, sys.executable, *sys.argv)
