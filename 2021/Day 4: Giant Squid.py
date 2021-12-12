class Field:
    def __init__(self, value: int):
        self.value = value
        self.marked = False

    def markField(self):
        self.marked = True

class Line:
    def __init__(self, line: list[str]):
        self.fields = createFields(line)

    def createFields(line: list[str]) -> list[Field]:
        fields = [Field]

        for string in line:
            fields.append(Field(int(string)))
        
        return fields

class Board:
    def __init__(self, board: list[str]):
        self.lines = createLines(board)
        self.columns = createColumns(board)

    def createLines(board: list[str]) -> list[Line]:
        # todo: implement
        return []

    def createColumds(board: list[str]) -> list[Line]:
        # todo: implement
        return []

def separateBoardLines(input: list[str]) -> list[list[str]]:
    boardLines = []
    sublist = []

    for line in input:
        if line.isspace() == False:
            sublist.append(line)
        else:
            boardLines.append(sublist)
            sublist = []
    
    return boardLines


def createBoards(input: list[str]) -> list[Board]:
    boardInputs = separateBoardLines(input)
    boards = []
    for boardInput in boardInputs:
        boards.append(Board(boardInput))
    return boards

path = "2021/Day 4 input"
file = open(path, 'r')
input = file.readlines()
drawnNumbers = input.pop(0)
input.pop(0) # removes empty line after popping drawn numbers
boards = createBoards(input)
