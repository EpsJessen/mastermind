from colours import Colours
from colour_printer import print_colour

class GuessPrinter:
    def __init__(self):
        pass

    def print_guess(self, guesses:list[Colours]) -> None:
        for guess in guesses:
            print_colour(guess, "●", False)

def main():
    resp = GuessPrinter
    guesses = [Colours.BLUE, Colours.RED, Colours.YELLOW, Colours.BLUE]
    resp.print_guess(resp, guesses)

if __name__ == "__main__":
    main()