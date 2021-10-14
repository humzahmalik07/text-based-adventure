# valid directions and actions to move

valid_actions = ["forward", "backward", "left", "right"]


# valid action or hint for Batman


valid_actions_2 = ["goggles"]

# valid action or hint for Green Lantern


valid_hint = ["ring"]

# This function defines the intro for Batman

def menu():
    print("""Choose an action:
    """)
    for action in valid_actions:
        print(f"* {action}")

# This defines the menu for the hint for Batman


def menu_2():
    for action in valid_actions_2:
        print(f"* {action}")

# This defines the menu for the hint for Green Lantern


def menu_3():
    for action in valid_hint:
        print(f"* {action}")


# This function prints out the ending message of the game


def end_script():
    print("""
    You have successfully escaped out of the temple and
    you have completed the game.
    """)

# This defines the first action of the game for Batman


def action_1():
    print("""
      LEVEL 1
      """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Wall ahead ")
        action_1()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_1()
    if action_input.lower() in valid_actions[2]:
        print(f" You are turning to the left side of the temple")
        action_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_1()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for your next direction.
            The direction is left. Enter left when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_1()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_1()


# This defines the second action for Batman


def action_2():
    print("""
        LEVEL 2
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead ")
        action_3()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_2()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_2()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_2()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_2()


# This defines the third action for Batman


def action_3():
    print("""
        LEVEL 3
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead")
        action_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_3()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_3()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_3()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_3()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_3()


# This defines the fourth action for Batman


def action_4():
    print("""
        LEVEL 4
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Dead end ")
        action_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_4()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_4()
    if action_input.lower() in valid_actions[3]:
        print(f" Turn right to walk towards the exit ")
        action_5()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is right. Enter right when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_4()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_4()


# This defines the fifth action for Batman


def action_5():
    print("""
        LEVEL 5
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        action_6()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_5()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_5()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_5()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_5()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_5()


# This defines the sixth action for Batman


def action_6():
    print("""
        LEVEL 6
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        action_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_6()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_6()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_6()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_6()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_6()


# This defines the seventh action for Batman


def action_7():
    print("""
        LEVEL 7
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        action_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_7()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_7()
    if action_input.lower() in valid_actions[3]:
        print(f" turn right towards the exit ")
        action_8()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is right. Enter right when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_7()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_7()


# This defines the eighth action for Batman


def action_8():
    print("""
        LEVEL 8
        """)
    menu()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        action_8()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_8()
    if action_input.lower() in valid_actions[2]:
        print(f" Turn left. You are getting closer!")
        action_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_8()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is left. Enter left when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_8()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_8()


# This defines the ninth action for Batman


def action_9():
    print("""
        LEVEL 9
        """)
    menu()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f""" You found the exit! """)
        end_script()
        quit()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_9()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_9()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The final direction is forward.
            Enter forward when the menu restarts."""
              )
        action_9()
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_1()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_9()

# This defines the first action taken by the user for Green Lantern


def actions_1():
    print("""
      LEVEL 1
      """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Wall ahead ")
        actions_1()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_1()
    if action_input.lower() in valid_actions[2]:
        print(f" You are turning to the left side of the temple")
        actions_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_1()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Power Ring.
      This ring is used as a flashlight
      and gives you a hint for you next direction.
            The direction is left. Enter left when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_1()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_1()


# This defines the second action taken by the user for Green Lantern


def actions_2():
    print("""
        LEVEL 2
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead ")
        actions_3()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_2()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_2()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Power Ring.
      This ring is used as a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_2()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_2()

# This defines the third action taken by the user for Green Lantern


def actions_3():
    print("""
        LEVEL 3
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead")
        actions_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_3()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_3()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_3()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Power Ring.
      This ring is used a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_3()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_3()


# This defines the fourth action taken by the user for Green Lantern


def actions_4():
    print("""
        LEVEL 4
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Dead end ")
        actions_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_4()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_4()
    if action_input.lower() in valid_actions[3]:
        print(f" Turn right to walk towards the exit ")
        actions_5()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
            The direction is right. Enter right when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_4()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_4()


# This defines the fifth action taken by the user for Green Lantern


def actions_5():
    print("""
        LEVEL 5
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        actions_6()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_5()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_5()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_5()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_5()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_5()


# This defines the sixth action taken by the user for Green Lantern


def actions_6():
    print("""
        LEVEL 6
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        actions_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_6()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_6()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_6()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_6()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_6()


# This defines the seventh action taken by the user for Green Lantern


def actions_7():
    print("""
        LEVEL 7
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        actions_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_7()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_7()
    if action_input.lower() in valid_actions[3]:
        print(f" turn right towards the exit ")
        actions_8()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
            The direction is right. Enter right when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_7()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_7()


# This defines the eighth action taken by the user for Green Lantern


def actions_8():
    print("""
        LEVEL 8
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        actions_8()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_8()
    if action_input.lower() in valid_actions[2]:
        print(f" Turn left. You are getting closer!")
        actions_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_8()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
            The direction is left. Enter left when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_8()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_8()


# This defines the ninth action taken by the user for Green Lantern


def actions_9():
    print("""
        LEVEL 9
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f""" You found the exit! """)
        end_script()
        quit()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_9()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_9()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_9()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_9()