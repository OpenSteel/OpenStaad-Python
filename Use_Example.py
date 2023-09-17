import ops_get as ops

# Get the number of nodes
node_count = ops.GetNodeCount()
print(f"There are {node_count} nodes in the model.")

# Get the coordinates of the first node
coordinates = ops.GetNodeCoordinates(1)
print(f"The coordinates of the first node are ({coordinates[0]}, {coordinates[1]}, {coordinates[2]}).")
