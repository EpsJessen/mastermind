from colours import Colours, get_random_colour
import random

def print_colour(colour:Colours, to_print:str, newline = True) -> None:
    match colour:
        case Colours.RED:
            print(f"\033[31m{to_print}\033[0m", end="")
        case Colours.GREEN:
            print(f"\033[32m{to_print}\033[0m", end="")
        case Colours.BLUE:
            print(f"\033[34m{to_print}\033[0m", end="")
        case Colours.YELLOW:
            print(f"\033[33m{to_print}\033[0m", end="")
        case Colours.WHITE:
            print(f"\033[37m{to_print}\033[0m", end="")
        case Colours.PURPLE:
            print(f"\033[35m{to_print}\033[0m", end="")
        case Colours.NOTACOLOUR:
            print(f"\033[0m{to_print}\033[0m", end="")
    if newline:
        print()

def print_random(text:str)-> None:
    for letter in text:
        print_colour(get_random_colour(), letter, False)
    print()