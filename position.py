class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash((self.row, self.column))