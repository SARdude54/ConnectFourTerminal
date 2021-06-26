class Game:
    def __init__(self):
        self.instructions = "Enter the coordinate you want to place. \n For example: \n '> D6' \n" \
                            "Type 'View' to list available positions to place"
        self.chars = []
        self.board = """
        A|    B|    C|    D|    E|    F|    G|
===============================================
1 ||_____|_____|_____|_____|_____|_____|_____|
2 ||_____|_____|_____|_____|_____|_____|_____|
3 ||_____|_____|_____|_____|_____|_____|_____|
4 ||_____|_____|_____|_____|_____|_____|_____|
5 ||_____|_____|_____|_____|_____|_____|_____|
6 ||_____|_____|_____|_____|_____|_____|_____|
"""
        for char in self.board:
            self.chars.append(char)

        self.positions = ["A1", "A2", "A3", "A4", "A5", "A6",
                          "B1", "B2", "B3", "B4", "B5", "B6",
                          "C1", "C2", "C3", "C4", "C5", "C6",
                          "D1", "D2", "D3", "D4", "D5", "D6",
                          "E1", "E2", "E3", "E4", "E5", "E6",
                          "F1", "F2", "F3", "F4", "F5", "F6",
                          "G1", "G2", "G3", "G4", "G5", "G6"]

        # Positions. Constant Variables
        self.A1 = 102
        self.B1 = 108
        self.C1 = 114
        self.D1 = 120
        self.E1 = 126
        self.F1 = 132
        self.G1 = 138

        self.A2 = 149
        self.B2 = 155
        self.C2 = 161
        self.D2 = 167
        self.E2 = 173
        self.F2 = 179
        self.G2 = 185

        self.A3 = 196
        self.B3 = 202
        self.C3 = 208
        self.D3 = 214
        self.E3 = 220
        self.F3 = 226
        self.G3 = 232

        self.A4 = 243
        self.B4 = 249
        self.C4 = 255
        self.D4 = 261
        self.E4 = 267
        self.F4 = 273
        self.G4 = 279

        self.A5 = 290
        self.B5 = 296
        self.C5 = 302
        self.D5 = 308
        self.E5 = 314
        self.F5 = 320
        self.G5 = 326

        self.A6 = 337
        self.B6 = 343
        self.C6 = 349
        self.D6 = 355
        self.E6 = 361
        self.F6 = 367
        self.G6 = 373

        self.row_1 = [self.A1, self.B1, self.C1, self.D1, self.E1, self.F1, self.G1]
        self.row_2 = [self.A2, self.B2, self.C2, self.D2, self.E2, self.F2, self.G2]
        self.row_3 = [self.A3, self.B3, self.C3, self.D3, self.E3, self.F3, self.G3]
        self.row_4 = [self.A4, self.B4, self.C4, self.D4, self.E4, self.F4, self.G4]
        self.row_5 = [self.A5, self.B5, self.C5, self.D5, self.E5, self.F5, self.G5]
        self.row_6 = [self.A6, self.B6, self.C6, self.D6, self.E6, self.F6, self.G6]

        self.column_1 = [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6]
        self.column_2 = [self.B1, self.B2, self.B3, self.B4, self.B5, self.B6]
        self.column_3 = [self.C1, self.C2, self.C3, self.C4, self.C5, self.C6]
        self.column_4 = [self.D1, self.D2, self.D3, self.D4, self.D5, self.D6]
        self.column_5 = [self.E1, self.E2, self.E3, self.E4, self.E5, self.E6]
        self.column_6 = [self.F1, self.F2, self.F3, self.F4, self.F5, self.F6]
        self.column_7 = [self.G1, self.G2, self.G3, self.G4, self.G5, self.G6]

        self.all_pos_values = self.column_1 + self.column_2 + self.column_3 + \
                              self.column_4 + self.column_5 + self.column_6 + self.column_7

        self.positions_dict = {}

        for pos, pos_value in zip(self.positions, self.all_pos_values):
            self.positions_dict[pos] = pos_value

        self.invert_positions_dict = {pos_value: pos for pos, pos_value in self.positions_dict.items()}

        self.left_diagonal_1 = [self.D6, self.E5, self.F4, self.G3]
        print(self.positions_dict)
        print(self.invert_positions_dict)
        print(self.invert_positions_dict[320])

    def init_Game(self):
        """
        Initiates game loops.
        :return: None
        """
        playing = True
        player1_turn = True
        player2_turn = False
        print(self.instructions)

        while playing:

            while player1_turn:
                input_ = input(self.board + "\n Player 1 \n >")

                if input_.lower() == "View".lower():
                    self.check_available_positions()
                elif input_ in self.positions:
                    if self.is_valid_input(input_):
                        self.update_board(self.positions_dict[input_], "O")
                        player1_turn = False
                        player2_turn = True
                    else:
                        print("You can't place it here")
                else:
                    print("Invalid input")
            while player2_turn:
                input_ = input(self.board + "\n Player 2 \n >")
                if input_.lower() == "View".lower():
                    self.check_available_positions()
                elif input_ in self.positions:
                    if self.is_valid_input(input_):
                        self.update_board(self.positions_dict[input_], "X")
                        player1_turn = True
                        player2_turn = False
                    else:
                        print("You can't place it here")
                else:
                    print("Invalid input")

    def _check_available_positions(self):
        """
        Checks possible coords for player to place and appends to list.
        :return: list
        """
        available_positions = []
        is_column1_empty = True
        is_column2_empty = True
        is_column3_empty = True
        is_column4_empty = True
        is_column5_empty = True
        is_column6_empty = True
        is_column7_empty = True

        # Check column 1
        for pos_value in self.column_1:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column1_empty = False
        if is_column1_empty:
            available_positions.append(self.invert_positions_dict[self.column_1[-1]])
        else:
            for pos_value in self.column_1[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 2
        for pos_value in self.column_2:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column2_empty = False
        if is_column2_empty:
            available_positions.append(self.invert_positions_dict[self.column_2[-1]])
        else:
            for pos_value in self.column_2[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 3
        for pos_value in self.column_3:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column3_empty = False
        if is_column3_empty:
            available_positions.append(self.invert_positions_dict[self.column_3[-1]])
        else:
            for pos_value in self.column_3[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 4
        for pos_value in self.column_4:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column4_empty = False
        if is_column4_empty:
            available_positions.append(self.invert_positions_dict[self.column_4[-1]])
        else:
            for pos_value in self.column_4[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 5
        for pos_value in self.column_5:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column5_empty = False
        if is_column5_empty:
            available_positions.append(self.invert_positions_dict[self.column_5[-1]])
        else:
            for pos_value in self.column_5[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 6
        for pos_value in self.column_6:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column6_empty = False
        if is_column6_empty:
            available_positions.append(self.invert_positions_dict[self.column_6[-1]])
        else:
            for pos_value in self.column_6[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 7
        for pos_value in self.column_7:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column7_empty = False
        if is_column7_empty:
            available_positions.append(self.invert_positions_dict[self.column_7[-1]])
        else:
            for pos_value in self.column_7[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        return available_positions

    def check_available_positions(self):
        """
        Method will display possible coords for player to place.
        :return: None
        """
        available_positions = []
        is_column1_empty = True
        is_column2_empty = True
        is_column3_empty = True
        is_column4_empty = True
        is_column5_empty = True
        is_column6_empty = True
        is_column7_empty = True

        # Check column 1
        for pos_value in self.column_1:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column1_empty = False
        if is_column1_empty:
            available_positions.append(self.invert_positions_dict[self.column_1[-1]])
        else:
            for pos_value in self.column_1[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 2
        for pos_value in self.column_2:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column2_empty = False
        if is_column2_empty:
            available_positions.append(self.invert_positions_dict[self.column_2[-1]])
        else:
            for pos_value in self.column_2[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 3
        for pos_value in self.column_3:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column3_empty = False
        if is_column3_empty:
            available_positions.append(self.invert_positions_dict[self.column_3[-1]])
        else:
            for pos_value in self.column_3[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 4
        for pos_value in self.column_4:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column4_empty = False
        if is_column4_empty:
            available_positions.append(self.invert_positions_dict[self.column_4[-1]])
        else:
            for pos_value in self.column_4[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 5
        for pos_value in self.column_5:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column5_empty = False
        if is_column5_empty:
            available_positions.append(self.invert_positions_dict[self.column_5[-1]])
        else:
            for pos_value in self.column_5[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 6
        for pos_value in self.column_6:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column6_empty = False
        if is_column6_empty:
            available_positions.append(self.invert_positions_dict[self.column_6[-1]])
        else:
            for pos_value in self.column_6[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        # Check column 7
        for pos_value in self.column_7:
            if self.board[pos_value] == "X" or self.board[pos_value] == "O":
                is_column7_empty = False
        if is_column7_empty:
            available_positions.append(self.invert_positions_dict[self.column_7[-1]])
        else:
            for pos_value in self.column_7[::-1]:
                if self.board[pos_value] == "_":
                    available_positions.append(self.invert_positions_dict[pos_value])
                    break

        for pos in available_positions:
            print(pos)

    def is_valid_input(self, response):
        """
        Checks if the player entered a valid coordinate.
        :param response: str
        :return: bool
        """
        if response in self._check_available_positions():
            return True
        else:
            return False

    def update_board(self, pos, value):
        """
        Updates board string.
        :param pos: int
        :param value: str
        :return: str
        """
        self.chars[pos] = value
        updated_board = "".join(self.chars)
        self.board = updated_board
        return self.board
