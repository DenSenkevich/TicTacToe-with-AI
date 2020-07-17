import random


class Matrix:

    def __init__(self):
        self.action = True
        self.level = "easy"
        self.cells = []
        self.dict = {
            "1 3": 0, "2 3": 1, "3 3": 2,
            "1 2": 3, "2 2": 4, "3 2": 5,
            "1 1": 6, "2 1": 7, "3 1": 8
        }
        self.win_positions = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 4, 8), (2, 4, 6), (0, 3, 6),
            (1, 4, 7), (2, 5, 8)
        )
        self.free_spots = list()
        self.player1 = None
        self.player2 = None

    def start(self):
        modes = ("user", "easy", "medium", "hard")
        while True:
            start_inp = input("Input command:").split()
            if start_inp[0] == "start" and len(start_inp) == 3:
                if start_inp[1] in modes and start_inp[2] in modes:
                    self.player1 = start_inp[1]
                    self.player2 = start_inp[2]
                    break
                else:
                    print("Bad parameters!")
            else:
                print("Bad parameters!")
        cells = "         "
        self.cells = list(cells.replace("_", " "))
        self.print_matrix()
        self.ask_player()

    def print_matrix(self):
        print("---------")
        for i in range(0, 7, 3):
            print(f"| {self.cells[i]} {self.cells[i + 1]} {self.cells[i + 2]} |")
        print("---------")

    def ask_player(self):
        while self.action:
            if self.cells.count("X") == self.cells.count("O"):
                if self.player1 == "easy":
                    self.easy_move()
                elif self.player1 == "user":
                    self.user_move()
                elif self.player1 == "medium":
                    self.medium_move()
                elif self.player1 == "hard":
                    self.medium_move()
            else:
                if self.player2 == "easy":
                    self.easy_move()
                elif self.player2 == "user":
                    self.user_move()
                elif self.player2 == "medium":
                    self.medium_move()
                elif self.player2 == "hard":
                    self.medium_move()

    def user_move(self):
        inp = input("Enter the coordinates:")
        if inp[0].isdigit() and inp[1] == " " and inp[2].isdigit():
            if 0 <= int(inp[0]) <= 3 and 0 <= int(inp[2]) <= 3:
                if self.cells[self.dict[inp]] == " ":
                    self.draw_cell(self.dict[inp])
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

    def easy_move(self):
        print(f'Making move level "easy"')
        self.free_spots = list()
        for i in range(len(self.cells)):
            if self.cells[i] == " ":
                self.free_spots.append(i)
        ai_move = random.choice(self.free_spots)
        self.draw_cell(ai_move)

    def medium_move(self):
        print(f'Making move level "medium"')
        for (a, b, c) in self.win_positions:
            check1 = (self.cells[a], self.cells[b], self.cells[c]).count("X") == 2
            check2 = (self.cells[a], self.cells[b], self.cells[c]).count("O") == 2
            if self.cells.count("X") == self.cells.count("O"):
                if check1:
                    check = (a, b, c)
                    for el in check:
                        if self.cells[el] == " ":
                            self.draw_cell(el)
                            return
            else:
                if check2:
                    check = (a, b, c)
                    for el in check:
                        if self.cells[el] == " ":
                            self.draw_cell(el)
                            return
            if check1 or check2:
                check = (a, b, c)
                for el in check:
                    if self.cells[el] == " ":
                        self.draw_cell(el)
                        return
        self.free_spots = list()
        for i in range(len(self.cells)):
            if self.cells[i] == " ":
                self.free_spots.append(i)
        ai_move = random.choice(self.free_spots)
        self.draw_cell(ai_move)

    def draw_cell(self, item):
        if self.cells.count("X") == self.cells.count("O"):
            self.cells[item] = "X"
        else:
            self.cells[item] = "O"
        self.print_matrix()
        for (a, b, c) in self.win_positions:
            if (self.cells[a], self.cells[b], self.cells[c]) == ("X", "X", "X"):
                print("X wins")
                self.action = False
                return
            elif (self.cells[a], self.cells[b], self.cells[c]) == ("O", "O", "O"):
                print("O wins")
                self.action = False
                return
            elif self.cells.count("X") == 5 and self.cells.count("O") == 4:
                print("Draw")
                self.action = False
                return


game = Matrix()
game.start()

# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)
# cells[0] cells[1] cells[2]
# cells[3] cells[4] cells[5]
# cells[6] cells[7] cells[8]
