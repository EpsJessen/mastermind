from colours import Colours

class GuessComparer:
    def __init__(self):
        pass

    def compare(self, guesses:list[Colours], answers:list[Colours]) -> tuple[int, int]:
        answer_copy = answers.copy()
        correct_colour_and_place = 0
        correct_colour = 0
        for place, guess in enumerate(guesses):
            if guess == answers[place]:
                correct_colour_and_place += 1
        for guess in guesses:
            if guess in answer_copy:
                correct_colour += 1
                answer_copy.remove(guess)
        return correct_colour_and_place, correct_colour

def main():
    cmp = GuessComparer()
    guesses = [Colours.BLUE, Colours.RED, Colours.YELLOW, Colours.BLUE]
    answers = [Colours.BLUE, Colours.GREEN, Colours.BLUE, Colours.RED]
    full, partial = cmp.compare(guesses, answers)
    print(f"There were {full} correctly placed, and further {partial-full} correct colours")
if __name__ == "__main__":
    main()