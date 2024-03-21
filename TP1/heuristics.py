# -*- coding: utf-8 -*-

def manhattan_heuristic(board):
    distance = 0
    for i, row in enumerate(board.board):  # Acceder a board.board en lugar de board
        for j, cell in enumerate(row):
            if cell == '*':
                distance += closest_target_distance(board, i, j)
    return distance

def closest_target_distance(board, x, y):
    min_distance = float('inf')
    for i, row in enumerate(board.board):  # Acceder a board.board en lugar de board
        for j, cell in enumerate(row):
            if cell == '.':
                distance = abs(x - i) + abs(y - j)
                min_distance = min(min_distance, distance)
    return min_distance

def combined_heuristic(board):
    goals = [(i, j) for i, row in enumerate(board.board) for j, cell in enumerate(row) if cell == '.']
    return combined(board, goals)

def combined(board, goals):
    distance = 0
    for box in board.get_boxes_positions():  # Utilizar el método get_boxes_positions()
        min_distance_with_turns = float('inf')
        for goal in goals:
            manhattan_distance = abs(box[0] - goal[0]) + abs(box[1] - goal[1])
            turns_needed = 0 if (box[0] - goal[0]) * (box[1] - goal[1]) == 0 else 1
            distance_with_turns = manhattan_distance + turns_needed * 2
            min_distance_with_turns = min(min_distance_with_turns, distance_with_turns)
        distance += min_distance_with_turns
    return distance
