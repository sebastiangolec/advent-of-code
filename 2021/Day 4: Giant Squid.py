class Field:
    def __init__(self, value: int):
        self._value = value
        self._marked = False

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
    
    @property
    def marked(self):
        return self._marked
    
    @marked.setter
    def marked(self, value):
        self._marked = value

    def markField(self):
        self.marked = True

class Line:
    def __init__(self, line: list[int]):
        self._fields = self.createFields(line)
    
    @property
    def fields(self):
        return self._fields
    
    @fields.setter
    def fields(self, value):
        self._fields = value

    def createFields(self, line: list[int]) -> list[Field]:
        fields = []

        for number in line:
            fields.append(Field(number))
        
        return fields
    
    def markNumber(self, number: int):
        for field in self.fields:
            if field.value == number:
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
            if field.marked == False:
                score += field.value
        
        return score


class Board:
    def __init__(self, board: list[str]):
        self._lines = self.createLines(board)
        self._columns = self.createColumns(board)
        
    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        self._columns = value
    
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

def separateBoardLines(input: list[str]) -> list[list[str]]:
    boardLines = []
    sublist = []

    for line in input:
        if line.isspace() == False:
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

def play(boards: list[Board], drawnNumbers: list[int]) -> int:
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
score = play(boards, drawnNumbers)
print(score)