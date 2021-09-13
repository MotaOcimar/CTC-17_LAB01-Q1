import heapq
from math import inf

class PathPlanner(object):
    def __init__(self, cost_map):
        self.cost_map = cost_map


    def construct_path(self, goal_node):
        current_node = goal_node
        reversed_path = []

        while current_node is not None:
            reversed_path.append(current_node.id)
            current_node = current_node.path_parent

        return reversed_path[::-1]


    def a_star(self, start_node_id, goal_node_id):
        start_node = self.cost_map.get_node(start_node_id)
        goal_node = self.cost_map.get_node(goal_node_id)

        # Initializes start node
        start_node.cost_to_here = 0 # g
        start_node.cost_from_here = start_node.distance_to(goal_node) # h
        start_node.cost_passing_through = start_node.cost_to_here + start_node.cost_from_here # f

        # Initializes the priority queue
        sorted_nodes = []
        heapq.heappush(sorted_nodes, start_node)

        # Iterates through the nodes with the lowest cost estimate looking for the goal
        while len(sorted_nodes) != 0:
            current_node = heapq.heappop(sorted_nodes)
            current_node.is_needed_to_improve = False
            if current_node.id == goal_node_id:
                break
            
            # Improve its successors' estimates
            successors = self.cost_map.get_successors(current_node)
            for successor in successors:
                cost_current_to_successor = current_node.distance_to(successor)

                if successor.cost_to_here > current_node.cost_to_here + cost_current_to_successor \
                    and successor.is_needed_to_improve:
                    successor.path_parent = current_node

                    successor.cost_to_here = current_node.cost_to_here + cost_current_to_successor # g
                    if successor.cost_from_here is inf: successor.cost_from_here = successor.distance_to(goal_node) # h
                    successor.cost_passing_through = successor.cost_to_here + successor.cost_from_here # f

                    if successor in sorted_nodes:
                        heapq.heapify(sorted_nodes) # Updates heap
                    else:
                        heapq.heappush(sorted_nodes, successor)

        return self.construct_path(goal_node), goal_node.cost_to_here
