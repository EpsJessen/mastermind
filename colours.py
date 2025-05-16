from enum import Enum
import random

class Colours(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5
    PURPLE = 6
    NOTACOLOUR = 100

def colour_from_string(string_colour:str)-> Colours:
    match string_colour.upper():
                    case "RED" | "R" | "1":
                        return Colours.RED
                    case "GREEN" | "G" | "2" | "GRN":
                        return Colours.GREEN
                    case "BLUE" | "B" | "3" | "BLU":
                        return Colours.BLUE
                    case "YELLOW" | "Y" | "4" | "YLW" | "YEL":
                        return Colours.YELLOW
                    case "WHITE" | "W" | "5" | "WHI" | "WHT":
                        return Colours.WHITE
                    case "PURPLE" | "P" | "6" |"PUR" | "PRP" | "PPL" | "PRL":
                        return Colours.PURPLE
                    case _:
                        return Colours.NOTACOLOUR
         
def get_random_colour():
    return random.choice(list(Colours)[:-1])