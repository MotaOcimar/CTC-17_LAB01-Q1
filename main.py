import matplotlib.pyplot as plt
from cost_map import CostMap
from path_planner import PathPlanner


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

cost_map = CostMap(data_filename)
path_planner = PathPlanner(cost_map)
path, cost = path_planner.a_star(start_node_id, goal_node_id)

print("Cost: ", cost*1.1)
print("Path: ", path)
plot_path(cost_map, start_node_id, goal_node_id, path)
