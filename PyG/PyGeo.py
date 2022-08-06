import torch_geometric
from torch_geometric.datasets import Planetoid

dataset = Planetoid(root="tutorial1", name="Cora")

print(dataset)
print(len(dataset))
print(dataset.num_classes)
print(dataset.num_node_features)
print(dataset.num_edge_features)
print(dataset.data)
