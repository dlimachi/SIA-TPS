class Board:
    def __init__(self, board_file):
        self.board = self.load_board(board_file)
        self.player_position = self.find_player_position()
        self.box_positions = self.find_box_positions()

    def load_board(self, board_file):
        with open(board_file, 'r') as file:
            return [list(line.strip()) for line in file]

    def find_player_position(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == '@':
                    return (i, j)
        return None

    def find_box_positions(self):
        box_positions = []
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == '$':
                    box_positions.append((i, j))
        return box_positions

    def get_boxes_positions(self):
        return self.box_positions
