"""
File: PotholeFilling.py
Name: Vicky
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre_condition:Karel is at the(2,1)
    post_condition:Karel is at thee (2,7)
    """
    for i in range(3):
        go_in()
        put_99_beeper()
        go_out()


def go_in():
    """
    pre_condition:Kare is the upper left，facing East
    post_condition:Kare is the upper right，facing South
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre_condition:Kare is the upper right，facing South
    post_condition:Kare is the upper left，facing East
     """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
        for i in range(3):
            turn_left()


def put_99_beeper():
    """
    Kare will put 99 beeper
    """
    for i in range(99):
         put_beeper()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
