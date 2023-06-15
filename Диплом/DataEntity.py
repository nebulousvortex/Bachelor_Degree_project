import numpy as np


class DataEntity:

    def __init__(self):
        self.graph_array = np.array([])
        self.attributes_array = np.array([])

    def get_graph(self, index):
        return self.graph_array[index]

    def get_attribute(self, index):
        return self.attributes_array[index]

    def add_graph(self, value):
        self.graph_array = np.append(self.graph_array, value)

    def add_attribute(self, value):
        self.attributes_array = np.append(self.attributes_array, value)

    def get_graph_count(self):
        return len(self.graph_array)

    def get_attribute_count(self):
        return len(self.attributes_array)

    def delete_graph(self):
        self.graph_array = np.delete(self.graph_array, -1)

    def delete_attribute(self):
        self.attributes_array = np.delete(self.attributes_array, -1)
