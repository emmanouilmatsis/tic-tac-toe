import unittest

import requests


class ValidationTestCase(unittest.TestCase):

    def setUp(self):
        """Set up fixture."""

        self.url = "http://localhost:8080"

    def test_valid_boards(self):
        """Tests if board string representation and content is valid."""

        boards = [
                "         ", # empty
                "x        ", # x first (x-1=o)
                "ox       ", # o first (x=o)
                "xox      ", # x first (x-1=o)
                ]

        for board in boards:
            with self.subTest(valid_board=board):
                r = requests.get(self.url, params={"board": board})
                self.assertEqual(r.status_code, requests.codes.ok)

    def test_invalid_boards(self):
        """Tests if board string representation and content is valid."""

        boards = [
                "        ", # invalid (b<9)
                "          ", # invalid (b>9)
                "xo      z", # invalid (char)
                "xoxoxoxox", # invalid (not +)
                "xx       ", # invalid (x-1>o)
                "oxxx     ", # invalid (x-1>o)
                "oo       ", # invalid (x+1<o)
                "xooo     ", # invalid (x+1<o)
                "o        ", # not o turn (x+1=o)
                "oxo      ", # not o turn (x+1=o)
                "xxxo o   ", # horizontal win
                "xo xo x  ", # vertical win
                "  xoxox  ", # diagonal win
                "xo  xo  x", # diagonal win
                ]

        for board in boards:
            with self.subTest(invalid_board=board):
                r = requests.get(self.url, params={"board": board})
                self.assertEqual(r.status_code, requests.codes.bad)


class StrategyTestCase(unittest.TestCase):

    def setUp(self):
        """Set up fixture."""

        self.url = "http://localhost:8080"

    def test_strategy(self):
        """Tests the the tic tac toe strategy implementation."""

        boards = [
                ("xox ox   ", "xox ox o "), # win
                ("x xo     ", "xoxo     "), # block
                ("o  x   xo", "oo x   xo"), # fork
                ("x   o   x", "xo  o   x"), # blockfork
                ("x        ", "x   o    "), # center
                ("o   x   x", "o o x   x"), # opposite
                ("         ", "    o    "), # empty
                ("o   x    ", "oo  x    "), # side
                ]

        for board in boards:
            with self.subTest(board=board):
                r = requests.get(url=self.url, params={"board": board[0]})
                self.assertEqual(r.text, board[1])


if __name__ == "__main__":
    unittest.main()
