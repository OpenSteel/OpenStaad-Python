from ops_get import *

# Create an instance of the class
geometry = StaadProGeometry()

# Get the number of nodes
node_count = geometry.GetNodeCount()
print(f"There are {node_count} nodes in the model.")

# Get the coordinates of the first node
coordinates = geometry.GetNodeCoordinates(1)
print(f"The coordinates of the first node are ({coordinates[0]}, {coordinates[1]}, {coordinates[2]}).")