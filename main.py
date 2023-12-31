"""
#last edit 27/10/2023 (ver.9)

*Compleat??? Edit By NN

!------------------------------------------------------------

TODO:Mini Project Programming Fundamental KMUTNB BKK Thailand
=> By Noppasin Renruang CprE. 6601012620119

?ref. https://www.geeksforgeeks.org/how-to-find-the-index-of-value-in-numpy-array/
?ref. https://www.adamsmith.haus/python/answers/how-to-replace-elements-in-a-numpy-array-if-a-condition-is-met-in-python
?ref. https://github.com/jakevdp/PythonDataScienceHandbook
?ref. https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python

!------------------------------------------------------------
"""

from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
from random import choices
import datetime
import time as t


class BackEnd:
    def __init__(self, array) -> None:
        self.array = array
        self.first_time = datetime.datetime.now()
        self.lst_value = [-1, 1]
        self.round_ = 1
        self.createArray()

    def createArray(self) -> None:
        """
        The function creates a 2D array and initializes certain elements with specific values.
        """
        self.array[4, 4] = -1
        self.array[4, 5] = 1
        self.array[5, 4] = 1
        self.array[5, 5] = -1
        for i in [0, 9]:
            for j in range(10):
                self.array[i, j] = 9
                self.array[j, i] = 9

    def showNumberOfBlackWhite(self, white_value: int = -1, black_value: int = 1) -> str:
        """
        The function `showNumberOfBlackWhite` returns the count of white and black values in an array, along
        with their sum.

        :param white_value: The `white_value` parameter is an optional integer parameter that represents the
        value of white in the array. By default, it is set to -1
        :type white_value: int
        :param black_value: The `black_value` parameter is an optional integer parameter that represents the
        value used to identify black elements in the array. By default, it is set to 1, defaults to 1
        :type black_value: int (optional)
        :return: a string that displays the number of white and black values in the array, as well as the
        sum of both.
        """
        return f'White: {np.sum(self.array == white_value)}   Black: {np.sum(self.array == black_value)}'

    def getNewValueOfDirection(self, row: int, col: int, key_direction: str) -> int:
        """
        The function `getNewValueOfDirection` returns the value of a specific direction in a 2D array given
        the row, column, and direction key.

        :param row: The parameter `row` represents the row index of the element in the array
        :type row: int
        :param col: The parameter `col` represents the column index of the element in the array
        :type col: int
        :param key_direction: The `key_direction` parameter is a string that represents the direction for
        which you want to retrieve the value from the `self.array` array. The possible values for
        `key_direction` are 'NW', 'N', 'NE', 'W', 'E', 'SW', 'S', and
        :type key_direction: str
        :return: the value of the specified direction in the array.
        """
        direction_value = {
            'NW':  self.array[row - 1, col - 1], 'N': self.array[row - 1, col], 'NE': self.array[row - 1, col + 1],
            'W':   self.array[row, col - 1], 'E': self.array[row, col + 1],
            'SW':  self.array[row + 1, col - 1], 'S': self.array[row + 1, col], 'SE': self.array[row + 1, col + 1]
        }
        return direction_value[key_direction]

    def getNewRowColOfDirection(self, row: int, col: int, key_direction: str) -> tuple:
        """
        The function `getNewRowColOfDirection` takes in a current row and column position, as well as a key
        direction, and returns the new row and column position based on the given direction.

        :param row: The parameter `row` represents the current row position in a grid or matrix. It is an
        integer value
        :type row: int
        :param col: The `col` parameter represents the column index of a cell in a grid
        :type col: int
        :param key_direction: The `key_direction` parameter is a string that represents the direction in
        which you want to move. It can have one of the following values: 'NW', 'N', 'NE', 'W', 'E', 'SW',
        'S', 'SE'
        :type key_direction: str
        :return: a tuple containing the new row and column values based on the given key_direction.
        """
        direction = {
            'NW':  {'row': row - 1, 'col': col - 1},    'N': {'row': row - 1, 'col': col}, 'NE': {'row': row - 1, 'col': col + 1},
            'W':   {'row': row, 'col': col - 1},        'E': {'row': row, 'col': col + 1},
            'SW':  {'row': row + 1, 'col': col - 1},    'S': {'row': row + 1, 'col': col}, 'SE': {'row': row + 1, 'col': col + 1}
        }
        return (direction[key_direction]['row'], direction[key_direction]['col'])

    def letEat(self, row: int, col: int, key_direction: str) -> None:
        """
        The function `letEat` changes the color of adjacent cells in a grid until it reaches a cell with a
        different color.

        :param row: The row parameter represents the current row index in the array
        :type row: int
        :param col: The parameter "col" represents the column index of the current position in the array
        :type col: int
        :param key_direction: The `key_direction` parameter is a string that represents the direction in
        which the movement should occur. It can have one of the following values: "up", "down", "left", or
        "right"
        :type key_direction: str
        """
        # original value (center)
        value = self.array[row, col]
        while True:
            # change another color
            if (value != self.getNewValueOfDirection(row, col, key_direction)):
                # change color
                self.array[self.getNewRowColOfDirection(row, col, key_direction)[
                    0], self.getNewRowColOfDirection(row, col, key_direction)[1]] = value
                # move 1 direction to check
                row, col = self.getNewRowColOfDirection(
                    row, col, key_direction)
            else:
                break

    def getWayToEat(self, row: int, col: int) -> None:
        """
        The function `getWayToEat` checks all directions around a given position in a 2D array and performs
        certain actions based on the values in those directions.

        :param row: The row parameter represents the current row position in the array
        :type row: int
        :param col: The parameter `col` represents the column index of a 2D array
        :type col: int
        """
        direction = {
            'NW':  self.array[row - 1, col - 1], 'N': self.array[row - 1, col], 'NE': self.array[row - 1, col + 1],
            'W':   self.array[row, col - 1], 'E': self.array[row, col + 1],
            'SW':  self.array[row + 1, col - 1], 'S': self.array[row + 1, col], 'SE': self.array[row + 1, col + 1]
        }
        # save original row and col
        save_row, save_col = row, col
        # check all direction
        for key, value in direction.items():
            # -----------------------------------------------
            # black 1 white -1  =>True
            # empty 0           => False
            # outside map 9     => False
            # -----------------------------------------------
            if (value != 9 and value != 0):
                # set row and col
                row, col = save_row, save_col
                # save color (center)
                save_val = self.array[row, col]
                while True:
                    # print("\t", key, value, "row=>", row, "col=>", col, sep="\t")
                    # change row and col with direction to check value
                    row, col = self.getNewRowColOfDirection(row, col, key)
                    # get same color    => True
                    if save_val == self.getNewValueOfDirection(row, col, key):
                        # print()
                        # print('last position = ', 'row:', row,'col', col, '| direction:', key)
                        # print()
                        # call function to change color use reference row and col to change
                        self.letEat(save_row, save_col, key)
                        break
                    # get 0 (empty) or 9 (outside map)  => True
                    elif not (self.getNewValueOfDirection(row, col, key)) or self.getNewValueOfDirection(row, col, key) == 9:
                        break

    def getWayToEatPreview(self, row: int, col: int, value_to_check: int) -> list:
        """
        The function `getWayToEatPreview` takes in a row and column position, as well as a value to check,
        and returns a list of positions where the value can be eaten based on the surrounding values in the
        array.

        :param row: The row parameter represents the current row position in the array
        :type row: int
        :param col: The parameter "col" represents the column index of the element in the array that we want
        to check for a way to eat
        :type col: int
        :param value_to_check: The `value_to_check` parameter is the value that you want to check against in
        the `direction` dictionary. It is used to determine if a certain condition is met in the `if`
        statement inside the `for` loop
        :type value_to_check: int
        :return: a list of tuples, where each tuple represents the row and column coordinates of a position
        in the array that can be eaten.
        """
        direction = {
            'NW':  self.array[row - 1, col - 1], 'N': self.array[row - 1, col], 'NE': self.array[row - 1, col + 1],
            'W':   self.array[row, col - 1], 'E': self.array[row, col + 1],
            'SW':  self.array[row + 1, col - 1], 'S': self.array[row + 1, col], 'SE': self.array[row + 1, col + 1]
        }
        # save original row and col
        save_row, save_col = row, col
        data_to_eat = []
        for key, value in direction.items():
            # black 1 white -1 =>True    empty 0 => False
            if (value != 9 and value != 0 and value != value_to_check and value != 2):
                # set row and col
                row, col = save_row, save_col
                # save color (center)
                save_val = self.array[row, col]
                while True:
                    row, col = self.getNewRowColOfDirection(row, col, key)
                    # get same color   => True
                    if save_val == self.getNewValueOfDirection(row, col, key):
                        break

                    # get 0 (empty) => True
                    elif not (self.getNewValueOfDirection(row, col, key)):
                        # move 1 direction to set value
                        row, col = self.getNewRowColOfDirection(row, col, key)
                        # set preview to value 2 in self.array
                        self.array[row, col] = 2
                        data_append = (row, col)
                        data_to_eat.append(data_append)
                        break
                    # get 9 (outside map) or get 2 (preview)   => True
                    elif (self.getNewValueOfDirection(row, col, key) == 9) or (self.getNewValueOfDirection(row, col, key) == 2):
                        break
        return data_to_eat

    def preview(self, value_to_check: int) -> list:
        """
        The `preview` function takes an integer value as input and returns a list of valid moves based on
        the value's position in the array.

        :param value_to_check: The value that you want to check for in the array
        :type value_to_check: int
        :return: a list of valid moves.
        """
        valid_move = []
        # loop all index that have your value
        for i in range(len(np.where(self.array == value_to_check)[0])):
            data = self.getWayToEatPreview(row=np.where(self.array == value_to_check)[
                                           0][i], col=np.where(self.array == value_to_check)[1][i], value_to_check=value_to_check)
            valid_move.extend(data)
        return valid_move

    @staticmethod
    def protectInput(text: str) -> str:
        """
        The `protectInput` function prompts the user for input and returns the input only if it is not
        empty.

        :param text: The `text` parameter is a string that represents the prompt or message that will be
        displayed to the user when asking for input
        :type text: str
        :return: The function `protectInput` returns a string.
        """
        while True:
            result = input(text)
            if result:
                return result

    def checkWin(self, turn: int) -> bool:
        """
        The function `checkWin` checks if there is a winner in a game based on the current state of the
        board and the current turn.

        :param turn: The "turn" parameter represents the current turn in the game. It is an integer value
        that indicates which player's turn it is
        :type turn: int
        :return: The function `checkWin` returns a boolean value. It returns `True` if there is a win
        condition (either all spaces on the board are filled or there are no valid moves left), and `False`
        otherwise.
        """
        # count empty if not have mean full board
        if np.sum(self.array == -1) + np.sum(self.array == 1) == 64:
            colorWin = 'White' if np.sum(
                self.array == -1) > np.sum(self.array == 1) else 'Black'
            print(colorWin, "Win")
            return True
        # can't move => lose
        elif self.valid_move == []:
            # turn => lose
            # black 1 white -1  *toggle stage*
            colorWin = 'White' if turn == 1 else 'Black'
            print(colorWin, "Win")
            return True
        else:
            return False

    def getDeltaTime(self) -> str:
        """
        The `getDeltaTime` function calculates the time difference between the current time and a previously
        set time and returns it in minutes and seconds.
        :return: The function `getDeltaTime` returns a string that represents the time difference between
        the current time and the time stored in the `self.first_time` variable. The string format is
        "{minutes} minutes, {seconds} seconds".
        """
        # self.first_time => set at __init__
        later_time = datetime.datetime.now()
        difference = later_time - self.first_time

        datetime.timedelta(0, 8, 562000)
        seconds_in_day = 24 * 60 * 60

        delta_time = divmod(
            difference.days * seconds_in_day + difference.seconds, 60)
        return f"{delta_time[0]} minutes, {delta_time[1]} seconds"

class PVP(BackEnd):
    def __init__(self, array) -> None:
        super().__init__(array)

    def runGame(self, i, j):
        while main.run:
            # player turn (white)
            if self.lst_value[self.round_]:
                # self.valid_move = self.preview(self.lst_value[self.round_])
                print('=>>>>>',self.valid_move)
                callback = self.tyrPlayerMove(i, j)
                if callback == 'break':
                    # Get Win
                    break
                elif callback == 'not_valid_move':
                    # self.lst_value[self.round_] = -1
                    break

    def tyrPlayerMove(self, i, j) -> str:
        # self.valid_move = self.preview(self.lst_value[self.round_])

        print("preview >>\n\n", self.array)
        self.row, self.col = i, j

        if (self.row, self.col) not in self.valid_move:
            print(self.valid_move,i,j)
            print("***\tnot valid move\t***")
            return 'not_valid_move'
        # reset_preview
        self.array = np.where(self.array == 2, 0, self.array)
        print("reset preview >>\n\n", self.array)

        # set color from input
        self.array[self.row, self.col] = self.lst_value[self.round_]
        self.getWayToEat(row=self.row, col=self.col)
        print(self.showNumberOfBlackWhite())
        print(self.getDeltaTime())
        self.round_ = not (self.round_)
        self.valid_move = self.preview(self.lst_value[self.round_])
        main.update()
        add_string = '>> {} Move '.format("White" if self.lst_value[self.round_] == -1 else ("Black " if self.lst_value[self.round_] == 1 else "empty"))
        row_chr = [chr(k) for k in range(ord('A'),ord('I'))]
        add_string += f'{row_chr[self.row - 1]}{self.col}\n'
        main.mytext.insert('1.0',add_string)
        if (self.checkWin(self.lst_value[self.round_])):
            print('in here we win', self.lst_value[self.round_])
            main.show_winner()
            return 'break'
            # win

class PVA_Easy(BackEnd):
    def __init__(self, array) -> None:
        super().__init__(array)

    def runGame(self, i, j):

        # for _ in range(10):
        while main.run:
            # player turn (white)
            if self.lst_value[self.round_] == -1:
                # self.valid_move = self.preview(self.lst_value[self.round_])
                print('=>>>>>',self.valid_move)
                callback = self.tyrPlayerMove(i, j)
                if callback == 'break':
                    # Get Win
                    break
                elif callback == 'not_valid_move':
                    self.lst_value[self.round_] = -1
                    break
            # Bot turn
            else:
                print("preview Bot (no2)>>\n\n", self.array)

                bot_move = choices(self.valid_move)
                self.row, self.col = bot_move[0][0], bot_move[0][1]

                # bot_move = choices(self.valid_move)
                # print("bot move =>",bot_move)
                # print("valid_move =>",self.valid_move)
                self.array = np.where(self.array == 2, 0, self.array)
                print("reset preview >>\n\n", self.array)
                # set color from input
                self.array[self.row, self.col] = self.lst_value[self.round_]
                self.getWayToEat(row=self.row, col=self.col)
                print(self.showNumberOfBlackWhite())
                print(self.getDeltaTime())
                self.round_ = not (self.round_)
                self.valid_move = self.preview(self.lst_value[self.round_])
                main.update()
                add_string = '>> {} Move '.format("White" if self.lst_value[self.round_] == -1 else ("Black " if self.lst_value[self.round_] == 1 else "empty"))
                row_chr = [chr(k) for k in range(ord('A'),ord('I'))]
                add_string += f'{row_chr[self.row - 1]}{self.col}\n'
                main.mytext.insert('1.0',add_string)
                if (self.checkWin(self.lst_value[self.round_])):
                    print('in here we win', self.lst_value[self.round_])
                    main.show_winner()
                    # win
                break

    def tyrPlayerMove(self, i, j) -> str:
        # self.valid_move = self.preview(self.lst_value[self.round_])

        print("preview >>\n\n", self.array)
        self.row, self.col = i, j

        if (self.row, self.col) not in self.valid_move:
            print(self.valid_move,i,j)
            print("***\tnot valid move\t***")
            return 'not_valid_move'
        # reset_preview
        self.array = np.where(self.array == 2, 0, self.array)
        print("reset preview >>\n\n", self.array)

        # set color from input
        self.array[self.row, self.col] = self.lst_value[self.round_]
        self.getWayToEat(row=self.row, col=self.col)
        print(self.showNumberOfBlackWhite())
        print(self.getDeltaTime())
        self.round_ = not (self.round_)
        self.valid_move = self.preview(self.lst_value[self.round_])
        main.update()
        add_string = '>> {} Move '.format("White" if self.lst_value[self.round_] == -1 else ("Black " if self.lst_value[self.round_] == 1 else "empty"))
        row_chr = [chr(k) for k in range(ord('A'),ord('I'))]
        add_string += f'{row_chr[self.row - 1]}{self.col}\n'
        main.mytext.insert('1.0',add_string)
        if (self.checkWin(self.lst_value[self.round_])):
            print('in here we win', self.lst_value[self.round_])
            main.show_winner()
            return 'break'
            # win

class PVA_Normal(BackEnd):
    def __init__(self, array) -> None:
        super().__init__(array)

    def runGame(self, i, j):

        # for _ in range(10):
        while main.run:
            # player turn (white)
            if self.lst_value[self.round_] == -1:
                # self.valid_move = self.preview(self.lst_value[self.round_])
                print('=>>>>>',self.valid_move)
                callback = self.tyrPlayerMove(i, j)
                if callback == 'break':
                    # Get Win
                    break
                elif callback == 'not_valid_move':
                    self.lst_value[self.round_] = -1
                    break
            # Bot turn
            else:
                print("preview Bot (no2)>>\n\n", self.array)

                bast_value = abs(self.valid_move[0][0] - self.valid_move[0][1])
                bast_move = (self.valid_move[0][0], self.valid_move[0][1])
                for move in self.valid_move:
                    if bast_value > abs(move[0] - move[1]):
                        bast_value = abs(move[0] - move[1])
                        bast_move = (move[0], move[1])
                bot_move = bast_move

                # bot_move = choices(self.valid_move)
                # print("bot move =>",bot_move)
                # print("valid_move =>",self.valid_move)
                self.array = np.where(self.array == 2, 0, self.array)
                print("reset preview >>\n\n", self.array)
                self.row, self.col = bot_move[0], bot_move[1]
                # set color from input
                self.array[self.row, self.col] = self.lst_value[self.round_]
                self.getWayToEat(row=self.row, col=self.col)
                print(self.showNumberOfBlackWhite())
                print(self.getDeltaTime())
                self.round_ = not (self.round_)
                self.valid_move = self.preview(self.lst_value[self.round_])
                main.update()
                if (self.checkWin(self.lst_value[self.round_])):
                    print('in here we win', self.lst_value[self.round_])
                    main.show_winner()
                    # win
                break

    def tyrPlayerMove(self, i, j) -> str:
        # self.valid_move = self.preview(self.lst_value[self.round_])

        print("preview >>\n\n", self.array)
        self.row, self.col = i, j

        if (self.row, self.col) not in self.valid_move:
            print(self.valid_move,i,j)
            print("***\tnot valid move\t***")
            return 'not_valid_move'
        # reset_preview
        self.array = np.where(self.array == 2, 0, self.array)
        print("reset preview >>\n\n", self.array)

        # set color from input
        self.array[self.row, self.col] = self.lst_value[self.round_]
        self.getWayToEat(row=self.row, col=self.col)
        print(self.showNumberOfBlackWhite())
        print(self.getDeltaTime())
        self.round_ = not (self.round_)
        self.valid_move = self.preview(self.lst_value[self.round_])
        main.update()
        add_string = '>> {} Move '.format("White" if self.lst_value[self.round_] == -1 else ("Black " if self.lst_value[self.round_] == 1 else "empty"))
        row_chr = [chr(k) for k in range(ord('A'),ord('I'))]
        add_string += f'{row_chr[self.row - 1]}{self.col}\n'
        main.mytext.insert('1.0',add_string)
        if (self.checkWin(self.lst_value[self.round_])):
            print('in here we win', self.lst_value[self.round_])
            main.show_winner()
            return 'break'
            # win

class AVA_Easy(BackEnd):
    def __init__(self, array) -> None:
        super().__init__(array)

    def runGame(self):
        if main.run:
            # for _ in range(20):
            print('-'*100)
            # player turn (white)
            if self.lst_value[self.round_] == -1:
                print("Bot1"*10)
                print("preview Bot (no2)>>\n\n", self.array)
                self.valid_move = self.preview(self.lst_value[self.round_])

                print(self.showNumberOfBlackWhite())
                print(self.getDeltaTime())

                print('#'*100)
                print("preview move>>\n\n", self.array)
                print("#"*100)

                # reset_preview
                self.array = np.where(self.array == 2, 0, self.array)

                if (self.checkWin(self.lst_value[self.round_])):
                    print("-"*50, "1")
                    main.show_winner()
                else:
                    bot_move = choices(self.valid_move)
                    print("bot move =>", bot_move)
                    print("valid_move =>", self.valid_move)
                    self.row, self.col = bot_move[0][0], bot_move[0][1]
                    # set color from input
                    self.array[self.row,self.col] = self.lst_value[self.round_]
                    self.getWayToEat(row=self.row, col=self.col)
                    self.round_ = not (self.round_)
                    main.update()
                    add_string = '>> {} Move '.format("White" if self.lst_value[self.round_] == -1 else ("Black " if self.lst_value[self.round_] == 1 else "empty"))
                    row_chr = [chr(k) for k in range(ord('A'),ord('I'))]
                    add_string += f'{row_chr[self.row - 1]}{self.col}\n'
                    main.mytext.insert('1.0',add_string)
                    main.after(750, main.mode.runGame)

            # Bot turn
            else:
                print("Bot2"*10)
                print("preview Bot (no2)>>\n\n", self.array)
                self.valid_move = self.preview(self.lst_value[self.round_])

                print(self.showNumberOfBlackWhite())
                print(self.getDeltaTime())

                print('#'*100)
                print("preview move>>\n\n", self.array)
                print("#"*100)

                # reset_preview
                self.array = np.where(self.array == 2, 0, self.array)

                if (self.checkWin(self.lst_value[self.round_])):
                    print("-"*50, "2")
                    main.show_winner()
                else:
                    bot_move = choices(self.valid_move)
                    print("bot move =>", bot_move)
                    print("valid_move =>", self.valid_move)
                    self.row, self.col = bot_move[0][0], bot_move[0][1]
                    # set color from input
                    self.array[self.row,self.col] = self.lst_value[self.round_]
                    self.getWayToEat(row=self.row, col=self.col)
                    self.round_ = not (self.round_)
                    main.update()
                    add_string = '>> {} Move '.format("White" if self.lst_value[self.round_] == -1 else ("Black " if self.lst_value[self.round_] == 1 else "empty"))
                    row_chr = [chr(k) for k in range(ord('A'),ord('I'))]
                    add_string += f'{row_chr[self.row - 1]}{self.col}\n'
                    main.mytext.insert('1.0',add_string)
                    main.after(750, main.mode.runGame)

class UI(Tk):
    def __init__(self):
        super().__init__()

        self.set_value()
        self.home_page()

    def set_value(self):
        # ''' ### Font-End value ###'''#
        self.geometry("1000x700+500+50")
        self.title("Othello")

        self.x_axis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.y_axis = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.btn = [['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '']]  # Board
        self.button = ['', '', '', '', '', '']  # homepage + 2btn
        self.textbtn = ['PVP', 'PVA Easy', 'PVA Normal',
                        'AVA', 'Home page', 'Restart']  # homepage + 2btn
        self.picture = [ImageTk.PhotoImage(Image.open("Empty.png")),
                        ImageTk.PhotoImage(Image.open("black.png")),
                        ImageTk.PhotoImage(Image.open("pre.png")),
                        ImageTk.PhotoImage(Image.open("nothing.png")),
                        ImageTk.PhotoImage(Image.open("home_page.png")),
                        ImageTk.PhotoImage(Image.open("restart.png")),
                        ImageTk.PhotoImage(Image.open("button.png")),
                        ImageTk.PhotoImage(Image.open("tone.png")),
                        ImageTk.PhotoImage(Image.open("white.png"))]  # 0 1 2 3(nothing) -1
        self.bg_image = ImageTk.PhotoImage(Image.open("background.png"))
        self.custom_font = ("Times New Roman", 24)

        # ''' ### Back-End value ###'''#
        self.modes = [PVP, PVA_Easy, PVA_Normal, AVA_Easy]
        self.Game = True
        self.run = 0

    def home_page(self):
        self.clean_UI()
        background_label = Label(self, image=self.bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # using for make a button stick in middle
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0,weight=8)
        self.grid_rowconfigure(1,weight=3)
        self.grid_rowconfigure(2,weight=3)
        self.grid_rowconfigure(3,weight=3)
        self.grid_rowconfigure(5,weight=5)
        #self.label = Label(self, text="Othello", font=("Times New Roman",72))
        #self.label.grid(row=0, column=1, sticky="NEW")

        for i in range(4):
            self.button = Button(
                self, text=self.textbtn[i],font=self.custom_font,image=self.picture[6],
                compound="center",foreground="lime", command=lambda num=i: self.getmode(num))
            self.button.grid(row=i+1, column=1, sticky="NEW")

    def create_board(self):
        self.clean_UI()
        self.Game = True
        self.run = 1
        self.label = Label(self, image=self.picture[3])
        self.label.grid(row=0, column=0, padx=5, pady=5)
        background_label = Label(self, image=self.picture[7])
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # self.realtime() # Label real time
        self.realTime = Label(self, text=f'{self.mode.getDeltaTime()}', font=self.custom_font,background="#BBF5EF",compound="center")
        self.realTime.grid(row=0, column=9, padx=20)
        self.after(1000, self.realtime)
        self.Turn = Label(self, text='{} Turn'.format("White" if self.mode.lst_value[self.mode.round_] == -1 else ("Black" if self.mode.lst_value[self.mode.round_] == 1 else "empty")), font=self.custom_font,background="#BBF5EF",compound="center")
        self.Turn.grid(row=1, column=9, padx=20)
        self.numbw = Label(self, text=f'{self.mode.showNumberOfBlackWhite()}', font=self.custom_font,background="#BBF5EF",compound="center")
        self.numbw.grid(row=2, column=9)
        self.mytext = Text(self, width = 22, height = 10, font = ('Calibri',12), wrap = WORD, padx = 10, pady = 10, bd = 4, selectbackground = 'Green', selectforeground = 'Red')
        self.mytext.grid(row=3, column=9,rowspan=4)

        for i in range(8):  # ABCD
            self.label = Label(
                self, text=self.x_axis[i], width=1, height=1, font=self.custom_font,background="#BBF5EF",compound="center")
            self.label.grid(row=0, column=i+1)

        for i in range(8):  # 1234
            self.label = Label(
                self, text=self.y_axis[i], width=1, height=1, font=self.custom_font,background="#BBF5EF",compound="center")
            self.label.grid(row=i+1, column=0)

        for i in range(4, 6):  # 2 btn
            self.button = Button(
                self, text=self.textbtn[i],image= self.picture[i], command=lambda i=i: self.ingame(i))
            self.button.grid(row=i+3, column=9)

        for i in range(8):  # board
            for j in range(8):
                self.btn[i][j] = Button(
                    self, text='', width=72, height=72, image=self.picture[3])
                self.btn[i][j].grid(row=i+1, column=j+1)

    def clean_UI(self):
        for widget in self.winfo_children():
            widget.grid_forget()

    def getmode(self, num):
        global restart
        self.clean_UI()
        self.mode = self.modes[num](np.zeros((10, 10), dtype=np.int8))
        restart = self.modes[num]
        self.start_game()

    def start_game(self):
        self.mode.round_ = not (self.mode.round_)
        if 'AVA_Easy' in str(self.mode):
            self.create_board()
            self.mode.runGame()
        else:
            self.mode.valid_move = self.mode.preview(
                self.mode.lst_value[self.mode.round_])
            print(self.mode.valid_move)

        self.create_board()
        self.update()

    def restart_game(self):
        self.mode = restart(np.zeros((10, 10), dtype=np.int8))
        self.clean_UI()
        self.start_game()

    def update(self):
        for i in range(8):  # ยัดกระดานเข้าUI
            for j in range(8):
                if self.mode.array[i+1][j+1] in [0, 1, -1]:
                    self.btn[i][j].config(
                        image=self.picture[self.mode.array[i+1][j+1]])
                else:
                    self.btn[i][j].config(
                        image=self.picture[2], command=lambda i=i+1, j=j+1: self.mode.runGame(i, j))

        self.Turn.config(text='{} Turn'.format("White" if self.mode.lst_value[self.mode.round_] == -1 else (
            "Black" if self.mode.lst_value[self.mode.round_] == 1 else "empty")))
        self.numbw.config(text=f'{self.mode.showNumberOfBlackWhite()}')

    def ingame(self, i):
        self.run = 0
        self.Game = False
        if i == 4:  # back to home page
            self.home_page()
        else:  # restart the game
            self.mode.round_ = not (self.mode.round_)
            self.restart_game()

    def realtime(self):
        if self.Game:
            self.realTime.config(text=f'{self.mode.getDeltaTime()}')
            self.after(1000, self.realtime)
        else:
            pass

    def show_winner(self):
        self.Game = not (self.Game)
        messagebox.showinfo("GAME END!!!", "{} WIN".format("White" if np.sum(
            self.mode.array == -1) > np.sum(self.mode.array == 1) else "Black"))

if __name__ == '__main__':
    # *** PVP MODE *** #
    # pvp_mode = PVP(np.zeros((10, 10), dtype=np.int8))
    # pvp_mode.runGame()

    # *** PVA MODE EASY *** #
    # pva_mode_easy = PVA_Easy(np.zeros((10, 10), dtype=np.int8))
    # pva_mode_easy.runGame()

    # *** PVA MODE NORMAL *** #
    # mode = PVA_Normal(np.zeros((10, 10), dtype=np.int8))

    # *** AVA MODE *** #
    # ava_mode_easy = AVA_Easy(np.zeros((10, 10), dtype=np.int8))
    # ava_mode_easy.runGame()
    main = UI()
    main.mainloop()