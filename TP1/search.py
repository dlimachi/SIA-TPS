from queue import PriorityQueue
from node import Node

class SearchEngine:
    def __init__(self, board, heuristic):
        self.board = board
        self.heuristic = heuristic

    def astar_search(self):
        frontier = PriorityQueue()
        frontier.put((self.heuristic(self.board), Node(self.board)))  # Pasar self.board como argumento
        explored = set()

        while not frontier.empty():
            current_node = frontier.get()[1]

            if current_node.state.is_goal():
                return current_node

            explored.add(current_node.state)

            for successor in self.get_successors(current_node):
                if successor.state not in explored:
                    priority = successor.cost + self.heuristic(successor.state)  # Pasar successor.state como argumento
                    frontier.put((priority, successor))

        return None
