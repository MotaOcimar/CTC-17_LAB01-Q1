import matplotlib.pyplot as plt
from cost_map import CostMap
from path_planner import PathPlanner
import networkx as nx


def plot_path(cost_map, start_node_id, goal_node_id, path):
    lng = []
    lat = []
    for id in path:
        node = cost_map.get_node(id)
        lng.append(node.lng)
        lat.append(node.lat)
    start = cost_map.get_node(start_node_id)
    goal = cost_map.get_node(goal_node_id)
    plt.plot(lng, lat, linewidth=2)
    plt.plot(start.lng, start.lat, 'y*', markersize=8)
    plt.plot(goal.lng, goal.lat, 'rx', markersize=8)

    plt.xlabel('lng')
    plt.ylabel('lat')
    plt.title('A*')
    plt.show()


# Main:
data_filename = "./australia.csv"
start_node_id = 5
goal_node_id = 219
print_path = True
do_plot_path = False

cost_map = CostMap(data_filename)
path_planner = PathPlanner(cost_map)
path, cost = path_planner.a_star(start_node_id, goal_node_id)

print("Cost: ", cost*1.1)
if print_path:
    print("Path: ", path)
if do_plot_path:
    plot_path(cost_map, start_node_id, goal_node_id, path)

# Validation
graph = nx.Graph()
graph.add_nodes_from(cost_map.nodes.keys())

edges = []
for node_id in cost_map.nodes.keys():
    node = cost_map.nodes[node_id]
    current_edges = [ (node_id, successor.id) if node_id < successor.id else (successor.id, node_id) for successor in cost_map.get_successors(node) ]
    edges = edges + current_edges

graph.add_edges_from(edges)

validation_cost = nx.astar_path_length(graph, start_node_id, goal_node_id, heuristic=cost_map.distance_between, weight=cost_map.distance_between)
validation_path = nx.astar_path(graph, start_node_id, goal_node_id, heuristic=cost_map.distance_between, weight=cost_map.distance_between)

print("Validation cost: ", validation_cost*1.1)
print("Path difference", [i for i, j in zip(path, validation_path) if i != j])
