from input_handler import InputHandler
from player_inputs import PlayerInput
from guess_printer import GuessPrinter
from guess_responder import GuessResponder
from chooser import Chooser
from colours import Colours
from success import Success
import colour_printer

class Mastermind:
    handler: InputHandler
    guess_printer: GuessPrinter
    guess_responder: GuessResponder
    chooser: Chooser
    last_score: int
    score_board: list[dict]

    def __init__(self):
        self.handler = InputHandler()
        self.guess_printer = GuessPrinter()
        self.guess_responder = GuessResponder()
        self.chooser = Chooser()
        self.last_score = 0
        self.score_board = [{"name": "FIL", "score": 8},{"name": "EPS", "score": 12}]

    def getName(self):
        while True:
                name = input("Please input three letter name: ")
                if len(name)==3:
                    return name
    
    def update_score(self, newScore:int):
        maxlen = 811
        if (self.score_board != []) and (newScore < self.score_board[-1]["score"]):
            name = self.getName()
            for i,record in enumerate(self.score_board):
                if newScore < record["score"]:
                    self.score_board.insert(i, {"name": name, "score": newScore})
                    if len(self.score_board) > maxlen:
                        self.score_board.pop()
                    break
        elif (len(self.score_board) < maxlen):
            name = self.getName()
            self.score_board.append({"name": name, "score": newScore})
        else:
            print("Too bad, you didn't do well enough to get on the scoreboard")
        self.show_scores()

    def show_scores(self):
        print()
        print(f"Nr.\tName\tScore")
        for i, record in enumerate(self.score_board, 1):
            print(f"{i}.\t{record["name"]}\t{record["score"]}")
        print()
        reset = input("press enter to return to main menu!")
        if reset == "reset":
            make_sure = input("Do you really want to reset the scores? [y/N]")
            if make_sure.lower() in ["y", "yes"]:
                self.score_board = []

    def main_menu(self):
        title = "●  MASTERMIND  ●"
        edges = "●"*len(title)
        between = "●" + " "*(len(title)-2) + "●"
        start_message = " 1. start"
        start = "●" + start_message +" "*(len(title)-len(start_message)-2) + "●"
        score_message = " 2. scores"
        score = "●" + score_message + " "*(len(title)-len(score_message)-2) + "●"
        quit_message = " 3. quit"
        quit = "●" + quit_message + " "*(len(title)-len(quit_message)-2) + "●"

        colour_printer.print_random(edges)
        colour_printer.print_random(between)
        colour_printer.print_random(title)
        colour_printer.print_random(between)
        colour_printer.print_random(start)
        colour_printer.print_random(score)
        colour_printer.print_random(quit)
        colour_printer.print_random(between)
        colour_printer.print_random(edges)
        print()
        
    def reset(self):
        self.chooser = Chooser()

    def start_game(self) -> tuple[Success, int]:
        correct_answer = self.chooser.get_pegs()
        #self.guess_printer.print_guess(correct_answer)
        allowed_nr_guesses = 16
        success = Success.FAIL
        nr_of_rounds = allowed_nr_guesses
        for i in range(allowed_nr_guesses):
            match i:
                case _ if i == 0:
                    mes = "first"
                case _ if i == allowed_nr_guesses-1:
                    mes = "last"
                case _:
                    mes = "next"
            response, guesses = self.handler.get_input(f"please write your {mes} guess: ")
            if response == PlayerInput.QUIT:
                success = Success.QUIT
                break
            self.guess_printer.print_guess(guesses)
            self.guess_responder.make_response(guesses, correct_answer)
            if guesses == correct_answer:
                success = Success.WIN
                nr_of_rounds = i + 1
                break
        match success:
            case Success.WIN:
                print("Congratualtions, you've won!")
                print(f"You did it in {nr_of_rounds} guesses!")
                return Success.WIN, nr_of_rounds
            case Success.FAIL:
                print("Too bad, you didn't win...")
                print("The correct answer was: ", end="")
                self.guess_printer.print_guess(correct_answer)
                print()
                return Success.FAIL, nr_of_rounds
            case Success.QUIT:
                print("Thanks for playing!")
                return Success.QUIT, nr_of_rounds


def main():
    game = Mastermind()
    while True:
        game.main_menu()
        player_choice = input()
        match player_choice:
            case "1" | "1.":
                success, turns = game.start_game()
                match success:
                    case Success.QUIT:
                        return
                    case Success.WIN:
                        game.update_score(turns)
                game.reset()
            case "2" | "2.":
                game.show_scores()
            case "3" | "3.":
                print("Thanks for playing!")
                return
            case _:
                continue
        
    

if __name__ == "__main__":
    main()