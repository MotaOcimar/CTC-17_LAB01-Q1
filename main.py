from cost_map import CostMap
from path_planner import PathPlanner


def plot_path(cost_map, start_node_id, goal_node_id, path):
    # TODO
    pass

# Main:
data_filename = "./australia.csv"
start_node_id = 5
goal_node_id = 219

cost_map = CostMap(data_filename)
path_planner = PathPlanner(cost_map)
path, cost = path_planner.a_star(start_node_id, goal_node_id)

print("Cost: ", cost)
plot_path(cost_map, start_node_id, goal_node_id, path)
