import os

class LineColumnMap:
    def __init__(self, text):
        new_line_char = os.linesep[-1]
        line_start_positions = [0]
        for position in range(len(text)):
            if text[position] == new_line_char:
                line_start_positions.append(position + 1)
        self.line_start_positions = line_start_positions

    def get_line(self, position):
        for i, line_start_position in enumerate(self.line_start_positions):
            if line_start_position > position:
                return i
        return len(self.line_start_positions)

    def get_column(self, position):
        line_start_position = self.line_start_positions[self.get_line(position) - 1]
        return position - line_start_position + 1