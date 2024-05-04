from typing import List
from abc import ABC, abstractmethod

"""
Piece abstract class and implementations of supported pieces (Knight/Bishop)
"""


class Piece(ABC):

    @abstractmethod
    def identifier(self):
        # return "knight" or "bishop", in future any other supported piece
        pass

    @abstractmethod
    def generate_rules_for_cell(self, grid: List[List[int]], i: int, j: int) -> []:
        pass

    def get_val_from_grid_pos(self, grid, x, y):
        if (not self._is_within_grid(grid, x, y) or
                not isinstance(grid[x][y], int)):
            return None

        return grid[x][y]

    def _is_within_grid(self, grid, x, y):
        if (x < 0 or
                x >= len(grid) or
                y < 0 or
                y >= len(grid[0])):
            return False
        return True


class Knight(Piece):

    def identifier(self):
        return "knight"

    def generate_rules_for_cell(self, grid, i, j):  # the 8 possible moves for a knight
        tmp_rules = [self.get_val_from_grid_pos(grid, i - 2, j + 1), self.get_val_from_grid_pos(grid, i - 2, j - 1),
                     self.get_val_from_grid_pos(grid, i - 1, j + 2), self.get_val_from_grid_pos(grid, i - 1, j - 2),
                     self.get_val_from_grid_pos(grid, i + 1, j + 2), self.get_val_from_grid_pos(grid, i + 1, j - 2),
                     self.get_val_from_grid_pos(grid, i + 2, j - 1), self.get_val_from_grid_pos(grid, i + 2, j + 1)]

        tmp_rules = [x for x in tmp_rules if x is not None]

        return tmp_rules


class Bishop(Piece):

    def identifier(self):
        return "bishop"

    def generate_rules_for_cell(self, grid, i, j):  # the 4 possible directions a bishop can move in
        rules = []

        count = 1
        while (self._is_within_grid(grid, i - count, j - count) or
               self._is_within_grid(grid, i - count, j + count) or
               self._is_within_grid(grid, i + count, j - count) or
               self._is_within_grid(grid, i + count, j + count)):
            rules.append(self.get_val_from_grid_pos(grid, i - count, j - count))  # up left
            rules.append(self.get_val_from_grid_pos(grid, i - count, j + count))  # up right
            rules.append(self.get_val_from_grid_pos(grid, i + count, j - count))  # down left
            rules.append(self.get_val_from_grid_pos(grid, i + count, j + count))  # down right

            count += 1

        rules = [x for x in rules if x is not None]

        return rules


"""
Main phone number generator class.

Entry method solve() should be called to print the solution output to stdout. 

The assignment outline:

- Given a phone dial pad with numbers 0-9 (see this line for the phone grid)
- Given we start with chess piece(s) on given cell(s)
- Given chess pieces can only move per their rules in chess (e.g a Knight in L shape, Bishop diagonally)
- Given we want of phone number of length N (e.g 10), how many different phone numbers can we generate by moving the chess piece(s) around the number pad.

See the tests at the bottom of the file for nice examples. E.g a bishop starting on number 5 and producing phone numbers of length 2 produces [51, 53, 57, 59] (5 then each of the diagonal moves).

"""


class PhoneNumberGenerator:
    supported_pieces = [Knight, Bishop]
    valid_integer_start_points = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def __init__(self,
                 piece=None,
                 num_length=None,
                 starting_digits=None,
                 rows=None,
                 cols=None,
                 grid=None):
        if piece:
            print("Initialising in test environment")
            self.piece = piece
            self.num_length = num_length
            self.starting_digits = starting_digits
            self.rows = rows
            self.cols = cols
            self.grid = grid
        else:
            # read from stdin for production env
            self.piece = input()
            self.num_length = int(input())
            self.starting_digits = self._convert_strings_to_ints(input().split(" "))
            self.rows = int(input())
            self.cols = int(input())
            grid = []
            for _ in range(self.rows):
                row = self._convert_strings_to_ints(input().split(" "))
                if len(row) != self.cols:
                    raise ValueError(f"Invalid row length {len(row)} does not match declared columns value {self.cols}")
                grid.append(row)

            if len(grid) != self.rows:
                raise ValueError(f"Invalid grid row count {len(grid)} does not match declared row value {self.rows}")
            self.grid = grid

        self._verify_input_params()

    """
    Main entry point to solve number generation problem
    """

    def solve(self) -> int:
        piece = self._create_piece_from_input_string(self.piece)

        starting_dp = self._init_dp_array()

        rules = self._generate_all_rules(piece)

        dp = self._compute_dp_array(starting_dp, rules)

        possible_numbers = sum(dp)
        print(possible_numbers)

        return possible_numbers  # returned for ease of testing

    def _convert_strings_to_ints(self, input_list):

        out = []
        for val in input_list:
            if val in self.valid_integer_start_points:
                out.append(int(val))
            else:
                out.append(val)
        return out

    def _init_dp_array(self):
        dp = [0] * 10
        for num in self.starting_digits:
            dp[num] = 1
        if self.num_length == 7:  # account for rule 4 (even though this could be implied in starting digits)
            # Rule = if length 7 then we cannot start with 0 or 1
            dp[0] = 0
            dp[1] = 0
        return dp

    def _compute_dp_array(self, dp, rules):
        # main solving logic
        # for each digit 'cur', to arrive at that digit we have to get sum of all dp values for the cells in the
        # rules array for corresponding 'cur' rules. e.g to get to cell 1, use rules[1] = [8, 6]
        for i in range(1, self.num_length):
            tmp_dp = dp.copy()
            for j in range(10):
                # for cell 1, the ways of getting to it were 8 and 6 so add the totals at 8 and 6
                count = 0
                for rule in rules.get(j, []):
                    count += dp[rule]
                tmp_dp[j] = count
            dp = tmp_dp.copy()
        return dp

    def _generate_all_rules(self, piece: Piece) -> dict:
        rules = {}

        # initialise rules for each cell dynamically
        # depending on piece, the rules generated will vary
        for i in range(self.rows):
            for j in range(self.cols):
                cell_val = self.grid[i][j]
                if isinstance(cell_val, int):  # is valid numeric cell
                    rules[cell_val] = piece.generate_rules_for_cell(self.grid, i, j)
        return rules

    def _create_piece_from_input_string(self, piece_type: str) -> Piece:
        for piece_class in self.supported_pieces:
            if piece_class().identifier().lower() == piece_type.lower():
                return piece_class()
        raise ValueError(f"Invalid piece type {piece_type}")

    def _verify_input_params(self):
        if type(self.piece) != str:
            raise Exception(f"Invalid piece '{self.piece}' submitted")
        # TODO, many more checks can be added to verify the input is valid


"""
Unit tests

- Uncomment unittest code at the end of this file to execute
- Normally this would not be in the same file/directory 
"""
import unittest


class PhoneNumberGeneratorTest(unittest.TestCase):

    def test_sovle_bishop_length_1(self):
        victim = PhoneNumberGenerator(piece="bishop",
                                      num_length=1,
                                      starting_digits=[2, 3, 4, 5, 6, 7, 8, 9],
                                      rows=4,
                                      cols=3,
                                      grid=[
                                          [1, 2, 3],
                                          [4, 5, 6],
                                          [7, 8, 9],
                                          ['*', 0, '#']
                                      ])

        actual = victim.solve()
        assert actual == 8  # 8 numbers of length one which are just 'starting_digits'

    def test_sovle_bishop_length_2(self):
        victim = PhoneNumberGenerator(piece="bishop",
                                      num_length=2,
                                      starting_digits=[5],
                                      rows=4,
                                      cols=3,
                                      grid=[
                                          [1, 2, 3],
                                          [4, 5, 6],
                                          [7, 8, 9],
                                          ['*', 0, '#']
                                      ])

        actual = victim.solve()
        assert actual == 4  # 4 numbers by starting at 5 as a bishop [51, 53, 57, 59]

    def test_sovle_bishop_skips_invalid_cells(self):
        victim = PhoneNumberGenerator(piece="bishop",
                                      num_length=2,
                                      starting_digits=[1],
                                      rows=4,
                                      cols=3,
                                      grid=[
                                          [3, '*', '#'],
                                          ['*', '*', '#'],
                                          ['*', '*', 1],
                                          ['*', '*', '#']
                                      ])

        actual = victim.solve()
        assert actual == 1

    def test_sovle_knight_length_1(self):
        victim = PhoneNumberGenerator(piece="knight",
                                      num_length=1,
                                      starting_digits=[2, 3, 4, 5, 6, 7, 8, 9],
                                      rows=4,
                                      cols=3,
                                      grid=[
                                          [1, 2, 3],
                                          [4, 5, 6],
                                          [7, 8, 9],
                                          ['*', 0, '#']
                                      ])

        actual = victim.solve()
        assert actual == 8

    def test_sovle_knight_length_2(self):
        victim = PhoneNumberGenerator(piece="knight",
                                      num_length=7,
                                      starting_digits=[2, 3, 4, 5, 6, 7, 8, 9],
                                      rows=4,
                                      cols=3,
                                      grid=[
                                          [1, 2, 3],
                                          [4, 5, 6],
                                          [7, 8, 9],
                                          ['*', 0, '#']
                                      ])

        actual = victim.solve()
        assert actual == 952  # populated this after running, trusting it's output


# p = PhoneNumberGenerator()
# p.solve()

# uncomment me to run tests
if __name__ == "__main__":
    unittest.main()
