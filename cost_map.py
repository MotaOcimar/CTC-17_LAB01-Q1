import csv
from math import inf, sqrt
import geopy.distance as geo_distance

class CostMap(object):
    def __init__(self, data_filename):
        self.nodes = {}

        with open(data_filename, 'r', newline='') as data_file:
            data_reader = csv.reader(data_file)

            next(data_reader) # skip first line
            for row in data_reader:
                node_id = int(row[0])
                node_lat = float(row[2])
                node_lng = float(row[3])

                new_node = Node(node_id, node_lat, node_lng)
                self.nodes[node_id] = new_node

    def get_node(self, node_id):
        if node_id in self.nodes.keys():
            return self.nodes[node_id]
        return None

    def get_successors(self, node):
        successors = []
        
        if node.id - 2 in self.nodes.keys():
            successors.append(self.nodes[node.id-2])
        
        if node.id %2:
            if node.id - 1 in self.nodes.keys():
                successors.append(self.nodes[node.id-1])
        else:
            if node.id + 1 in self.nodes.keys():
                successors.append(self.nodes[node.id+1])
        
        if node.id + 2 in self.nodes.keys():
            successors.append(self.nodes[node.id+2])

        return successors


class Node(object):
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = lat
        self.lng = lng
        self.path_parent = None
        self.cost_passing_through = inf # f
        self.cost_to_here = inf # g
        self.cost_from_here = inf # h

    def distance_to(self, node):
        return geo_distance.distance((self.lat, self.lng), (node.lat, node.lng)).km

    def __lt__(self, other):
        return self.cost_passing_through < other.cost_passing_through

    def __eq__(self, other):
        return self.id == other.id
