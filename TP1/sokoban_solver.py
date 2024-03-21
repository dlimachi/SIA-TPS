# -*- coding: utf-8 -*-
import sys
from board import Board
from search import SearchEngine
from heuristics import manhattan_heuristic, combined_heuristic

def main():
    if len(sys.argv) < 5:
        print("Usage: python sokoban_solver.py <method> <heuristic> <weight> <board_file>")
        return

    method = sys.argv[1]
    heuristic = sys.argv[2]
    weight = float(sys.argv[3])
    board_file = sys.argv[4]

    # Cargar el tablero desde el archivo
    board = Board(board_file)

    # Seleccionar la heurística
    if heuristic == 'manhattan':
        selected_heuristic = manhattan_heuristic
    elif heuristic == 'combined':
        selected_heuristic = combined_heuristic
    else:
        print("Error: Invalid heuristic")
        return

    # Crear el motor de búsqueda
    search_engine = SearchEngine(board, selected_heuristic)

    # Ejecutar el algoritmo de búsqueda seleccionado
    if method == 'bfs':
        solution = search_engine.breadth_first_search()
    elif method == 'dfs':
        solution = search_engine.depth_first_search()
    elif method == 'astar':
        solution = search_engine.astar_search()
    elif method == 'greedy':
        solution = search_engine.greedy_search()
    else:
        print("Error: Invalid search method")
        return

    # Imprimir la solución
    if solution is not None:
        print("Solution:", solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
