from dataclasses import dataclass

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

        for index, row in enumerate(clearBoard):
            column = []
            column.append(row[index])
            columns.append(Line(column))

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

def separateBoardLines(input: list[str]) -> list[list[str]]:
    boardLines = []
    sublist = []

    for line in input:
        if line.isspace() is False:
            sublist.append(line)

        if len(sublist) == 5:
            boardLines.append(sublist)
            sublist = []
    
    return boardLines


def createBoards(input: list[str]) -> list[Board]:
    boardInputs = separateBoardLines(input)
    boards = []

    for boardInput in boardInputs:
        boards.append(Board(boardInput))
        
    return boards

def convertToNumbers(input: str) -> list[int]:
    numbers = []

    for string in input.split(","):
        if string.isnumeric:
            numbers.append(int(string))
    
    return numbers

def playToWin(boards: list[Board], drawnNumbers: list[int]) -> int:
    for number in drawnNumbers:
        for board in boards:
            board.markNumber(number)
            isWinner = board.checkWinner()

            if isWinner:
                return board.calculatePoints(number)

path = "2021/Day 4 input"
file = open(path, 'r')
input = file.readlines()
drawnNumbersInput = input.pop(0)
input.pop(0) # removes empty line after popping drawn numbers
boards = createBoards(input)
drawnNumbers = convertToNumbers(drawnNumbersInput)
score = playToWin(boards, drawnNumbers)
print(score)