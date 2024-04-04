"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    per condition:Karel is on the left side of the well,facing East
    """
    up()
    cross()
    down()
def up():
    """
    per_condition:Karel is on the left side of the well,facing East
    post_condition:Karel is facing North
    """
    turn_left()
    #facing north
    while not right_is_clear():
        move()
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    """
def turn_right():
    for i in range(3):
        turn_left()


def cross():
    """
    pre_condition:Karel is facing North
    post_condition:Karel is at upper right,facing South

    """
    turn_right()
    move()
    turn_right()

def down():
    """
    pre_condition:Karel is at upper right,facing South
    post_condition:Karel is on the right side of the well,facing South
    """
    while front_is_clear():
        move()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
