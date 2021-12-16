from dataclasses import dataclass
from collections import namedtuple

Win = namedtuple('Win', ['index', 'score', 'drawnNumber'])

@dataclass
class Field:
    value: int
    marked: bool = False
    
    def markField(self):
        self.marked = True

class Line:
    def __init__(self, line: list[int]):
        self.fields = self.createFields(line)
    
    def createFields(self, line: list[int]) -> list[Field]:
        fields = []

        for number in line:
            fields.append(Field(number))
        
        return fields
    
    def markNumber(self, number: int):
        for field in self.fields:
            if field.value is number:
                field.markField()

    def checkWinner(self) -> bool:
        count = 0

        for field in self.fields:
            if field.marked:
                count += 1
        
        if count == 5:
            return True
        else:
            return False
    
    def calculatePoints(self) -> int:
        score = 0

        for field in self.fields:
            if field.marked is False:
                score += field.value
        
        return score


class Board:
    def __init__(self, board: list[str]):
        self.lines = self.createLines(board)
        self.columns = self.createColumns(board)
        
    def createLines(self, board: list[str]) -> list[Line]:
        lines = []

        for line in board:
            clearLine = self.clearLine(line)
            lines.append(Line(clearLine))

        return lines

    def createColumns(self, board: list[str]) -> list[Line]:
        columns = []
        clearBoard = []

        for line in board:
            clearBoard.append(self.clearLine(line))

        i = 0
        while i < len(clearBoard):
            column = []

            for line in clearBoard:
                column.append(line[i])
            
            columns.append(Line(column))
            i += 1

        return columns

    def clearLine(self, line: list[str]) -> list[int]:
        line = line.rstrip().split(" ")
        clearLine = []

        for string in line:
            if string.isnumeric():
                clearLine.append(int(string))
        
        return clearLine

    def markNumber(self, number: int):
        for line in self.lines:
            line.markNumber(number)

        for column in self.columns:
            column.markNumber(number)

    def checkWinner(self) -> bool:
        for line in self.lines:
            if line.checkWinner():
                return True

        for column in self.columns:
            if column.checkWinner():
                return True
        
        return False
    
    def calculatePoints(self, number: int) -> int:
        score = 0

        for line in self.lines:
            score += line.calculatePoints()

        return score * number

class Bingo:
    def __init__(self, input: list[str]):
        self.boards = self.createBoards(input)
        self.drawnNumbers = self.convertToNumbers(input.pop(0))

    def convertToNumbers(self, input: str) -> list[int]:
        numbers = []

        for string in input.split(","):
            if string.isnumeric:
                numbers.append(int(string))
        
        return numbers

    def createBoards(self, input: list[str]) -> list[Board]:
        boardInputs = self.separateBoardLines(input)
        boards = []

        for boardInput in boardInputs:
            boards.append(Board(boardInput))
            
        return boards
        
    def separateBoardLines(self, input: list[str]) -> list[list[str]]:
        boardLines = []
        sublist = []

        for line in input[1:]:
            if line.isspace() is False:
                sublist.append(line)

            if len(sublist) == 5:
                boardLines.append(sublist)
                sublist = []
        
        return boardLines

    def playToWin(self) -> Win:
        for number in self.drawnNumbers:
            for board in self.boards:
                board.markNumber(number)

                if board.checkWinner():
                    return Win(self.boards.index(board), board.calculatePoints(number), number)

    def playToLose(self) -> Win:
        losers = self.boards.copy()

        for number in self.drawnNumbers:

            if len(losers) > 1:
                newLosers = []

                for board in losers:
                    board.markNumber(number)

                    if board.checkWinner() is False:
                        newLosers.append(board)
                
                losers = newLosers.copy()
            else:
                winner = losers[0]
                winner.markNumber(number)
                
                if winner.checkWinner():
                    return Win(self.boards.index(winner), winner.calculatePoints(number), number)