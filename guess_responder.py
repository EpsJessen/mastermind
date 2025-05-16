from colour_printer import print_colour
from colours import Colours
from guess_comparer import GuessComparer

class GuessResponder:
    comparer: GuessComparer
    answer_size: int

    def __init__(self, answer_size:int = 6):
        self.comparer = GuessComparer()
        self.answer_size = answer_size


    def respond(self,fully:int, partially:int) -> None:
        print("  ", end="")
        print_colour(Colours.GREEN, "○"*fully, False)
        print_colour(Colours.RED, "○"*(partially-fully), False)
        print_colour(Colours.WHITE, "○"*(self.answer_size-partially), True)

    def make_response(self, guesses: list[Colours], answers: list[Colours]) -> None:
        fully, partially = self.comparer.compare(guesses,answers)
        self.respond(fully, partially)

def main():
    resp = GuessResponder()
    resp.respond(2,3)

if __name__ == "__main__":
    main()