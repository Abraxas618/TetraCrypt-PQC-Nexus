from pathlib import Path

# Define the content for tetrahedral_network.py
tetrahedral_network_code = """
import numpy as np

class TetrahedralNode:
    def __init__(self, id, position):
        self.id = id
        self.position = np.array(position)
        self.connections = []

    def connect(self, other_node):
        if other_node.id not in self.connections:
            self.connections.append(other_node.id)

class TetrahedralNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id, position):
        if id not in self.nodes:
            self.nodes[id] = TetrahedralNode(id, position)

    def connect_nodes(self, id1, id2):
        if id1 in self.nodes and id2 in self.nodes:
            self.nodes[id1].connect(self.nodes[id2])
            self.nodes[id2].connect(self.nodes[id1])

    def generate_base_tetrahedron(self):
        # Add 4 nodes of a tetrahedron
        positions = {
            'A': [1, 1, 1],
            'B': [-1, -1, 1],
            'C': [-1, 1, -1],
            'D': [1, -1, -1]
        }
        for id, pos in positions.items():
            self.add_node(id, pos)

        # Connect nodes to form a tetrahedron
        self.connect_nodes('A', 'B')
        self.connect_nodes('A', 'C')
        self.connect_nodes('A', 'D')
        self.connect_nodes('B', 'C')
        self.connect_nodes('B', 'D')
        self.connect_nodes('C', 'D')

    def get_adjacency_matrix(self):
        node_ids = list(self.nodes.keys())
        size = len(node_ids)
        matrix = np.zeros((size, size))
        for i, id1 in enumerate(node_ids):
            for j, id2 in enumerate(node_ids):
                if id2 in self.nodes[id1].connections:
                    matrix[i][j] = 1
        return matrix, node_ids
"""

# Save to src/models/tetrahedral_network.py
models_dir = Path("src/models")
models_dir.mkdir(parents=True, exist_ok=True)
file_path = models_dir / "tetrahedral_network.py"
file_path.write_text(tetrahedral_network_code)

file_path.name
