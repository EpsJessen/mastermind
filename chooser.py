from colours import Colours, get_random_colour
import random

class Chooser:
    _chosen_pegs = []

    def __init__(self):
        pegs = []
        for _ in range(6):
            pegs.append(get_random_colour())
        self._chosen_pegs = pegs

    def get_pegs(self) -> list[Colours]:
        return self._chosen_pegs
    
    def set_pegs(self, colours:list[Colours]):
        try:
            assert len(colours) == 6
            self._chosen_pegs = colours
        except AssertionError:
            print("list of colours not correct length")