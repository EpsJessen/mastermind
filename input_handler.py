from player_inputs import PlayerInput
from colours import Colours, colour_from_string
class InputHandler:
    guess:list[Colours] | None = None

    def __init__(self):
        pass

    def get_input(self, query:str) -> tuple[PlayerInput, list[Colours]]:
        bad_guess = False
        while True:
            newguess = input(query).strip()
            for i in range(bad_guess + 1):
                print('\033[1A' + '\33[K', end="")
            if newguess in ["q", "quit", "exit"]:
                return (PlayerInput.QUIT, [])
            answers = newguess.split()
            if len(answers) != 6:
                print("Please enter six colours")
                bad_guess = True
                continue
            input_colours:list[Colours] = []
            for answer in answers:
                colour = colour_from_string(answer)
                if colour == Colours.NOTACOLOUR:
                    print(f"Could not match {answer} to a colour, please try again")
                    bad_guess = True
                    continue
                input_colours.append(colour)
            self.guess = input_colours
            break
        return (PlayerInput.GUESS, input_colours)
            
    def get_last_guess(self)->list[Colours] | None:
        return self.guess