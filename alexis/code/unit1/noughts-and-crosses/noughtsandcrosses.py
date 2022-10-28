import sys

class NoughtsAndCrossesGame:
    def __init__(self):
        self.board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        self.current_player = "X"
        self.winner = None
        self.choice = 0
        self.main()

    @staticmethod
    def display_options():
        text = (
               "Choose an option:\n"
             + "[1] [2] [3]\n" 
             + "[4] [5] [6]\n"
             + "[7] [8] [9]\n"
        )
        print(text)

    def get_input(self):
        """
        Get input from the user.
        It waits for a valid input or quits on q.
        """
        indexes = "123456789"

        while str(self.choice) not in indexes:  # Iterate through indexes
            usr_choice = input()                # Get input
            
            if usr_choice == "q":               # Quit on 'q'
                sys.exit()
            
            # Convert first of usr_choice to an int if it is numeric
            if usr_choice.isnumeric():         
                self.choice = int(usr_choice[0])
            else:
                print("Input must be numeric.")
        
    def display_board(self):
        for row in self.board:
            print(f"[{row[0]}] [{row[1]}] [{row[2]}]")

    def check_space_is_free(self, i, j):
        return True if self.board[i][j] == "-" else False

    def find_indexes(self, choice):
        i = (choice - 1) // 3
        j = (choice - 1) % 3
        return (i, j)

    def place_piece(self, i, j):
        self.board[i][j] = self.current_player

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = "X"

    def check_vertical(self):
        for n in range(len(self.board)):
            line = []
            for i in self.board:
                line.append(i[n])
            if line == ["X", "X", "X"]:
                self.winner = "X"
            elif line == ["O", "O", "O"]:
                self.winner = "O"

    def check_horizontal(self):
        for line in self.board:
            if line == ["X", "X", "X"]:
                self.winner = "X"
            elif line == ["O", "O", "O"]:
                self.winner = "O"

    def check_diags(self):
        down = [
            self.board[0][0],
            self.board[1][1],
            self.board[2][2]
        ]
        up = [
            self.board[0][2],
            self.board[1][1],
            self.board[2][0]
        ]

        if down == ["X", "X", "X"] or up == ["X", "X", "X"]:
            self.winner = "X"
        elif down == ["O", "O", "O"] or up == ["O", "O", "O"]:
            self.winner = "O"

    def check_draw(self):
        all_pieces = []
        for i in self.board:
            for j in i:
                all_pieces.append(j)
        return True if "-" not in all_pieces else False

    def main(self):
        is_draw = False
        while self.winner is None:
            is_free = False
            while not is_free:
                self.display_options()
                self.get_input()
                a, b = self.find_indexes(self.choice)
                is_free = self.check_space_is_free(a, b)
                if is_free:
                    self.place_piece(a, b)
                    self.change_player()
                else:
                    print("Space not free.")
                self.choice = 0
                
            self.display_board()
            self.check_vertical()
            self.check_horizontal()
            self.check_diags()
            is_draw = self.check_draw()
            if is_draw:
                break
        if is_draw:
            print("Draw!")
        else:
            print(f"{self.winner} Wins!")


if __name__ == "__main__":
    NoughtsAndCrossesGame()