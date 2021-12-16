import unittest
import bingo

class BingoTest(unittest.TestCase):
    def test_drawnNumbers(self):
        input = open('2021/day4/test_input', 'r').readlines()
        game = bingo.Bingo(input)
        expectedDrawnNumbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
        self.assertEqual(expectedDrawnNumbers, game.drawnNumbers)

    def test_createBoards(self):
        input = open('2021/day4/test_input', 'r').readlines()
        game = bingo.Bingo(input)

        self.assertEqual(3, len(game.boards))
        for board in game.boards:
            self.assertEqual(5, len(board.lines))
            self.assertEqual(5, len(board.columns))
    
    def test_winner(self):
        input = open('2021/day4/test_input', 'r').readlines()
        game = bingo.Bingo(input)
        winner = game.playToWin()

        self.assertEqual(2, winner.index)
        self.assertEqual(4512, winner.score)
        self.assertEqual(24, winner.drawnNumber)

    def test_loser(self):
        input = open('2021/day4/test_input', 'r').readlines()
        game = bingo.Bingo(input)
        winner = game.playToLose()

        self.assertEqual(1, winner.index)
        self.assertEqual(1924, winner.score)
        self.assertEqual(13, winner.drawnNumber)

if __name__ == '__main__':
    unittest.main()