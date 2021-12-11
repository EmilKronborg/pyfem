from libary.emil2 import Beam, Node, CrossSectionLibrary
from libary.Material import Steel
# from libary.plot_undeformed import plot_undeformed

a = 0.210
b = 0.215
c = 0.210

coordinates = [(0, 0),      # Node 0
               (b, 0),      # Node 1
               (b, c),      # Node 2
               (0, c),      # Node 3
               (0, 2 * a),  # Node 4
               (b, 2 * a),  # Node 5
               (0, 3 * a),  # Node 6
               (b, 3 * a),  # Node 7
               (0, 4 * a),  # Node 8
               (b, 4 * a),  # Node 9
               (0, 5 * a),  # Node 10
               (b, 5 * a),  # Node 11
               (0, 6 * a),  # Node 12
               (b, 6 * a)]  # Node 13

connectivity = [(0, 3),
                (3, 4),
                (4, 6),
                (6, 8),
                (8, 10),
                (10, 12),
                (12, 13),
                (13, 11),
                (11, 9),
                (9, 7),
                (7, 5),
                (5, 2),
                (2, 1),
                (3, 2),
                (4, 5),
                (10, 11),
                (6, 7),
                (8, 9),
                (4, 7)]

# TODO: Get this loop out of the main file
nodes = {}                                               # Creating an empty dictionary for the nodes
for idx, coords in enumerate(coordinates):               # Looping over the index and coordinates in each tuple
    node = Node(coords)                                  # Assigning x and y coordinates
    node.dof = (idx * 3 + 1, idx * 3 + 2, idx * 3 + 3)   # Assigning DOF to each node
    nodes['Node ' + str(idx)] = node                     # Naming each node in ascending order

# TODO: Get this loop out of the main file
"""
Assign beam names with list comprehension?
In the tuples in connectivity, the material group can easily be implemented.
tuple = (node_i, node_j, material_group) can be decomposed into by
node_i, node_j, material_group = tuple. In that way,
node_i = [node[0] for node in connectivity]
"""
S355 = Steel('S355')
beams = {}                                               # Creating an empty dictionary for the beams
for idx, conn in enumerate(connectivity):                # Looping over the index and connectivities in each tuple
    beam = Beam()                                        # Calling Beam class
    beam.node_i = nodes['Node ' + str(conn[0])]          # Assigning properties for node_i
    beam.node_j = nodes['Node ' + str(conn[1])]          # Assigning properties for node_j
    beam.material = S355                                 # Assigning material to each beam
    beam.cross_section = 'INP200'
    beam.type = 'Euler Bernoulli'
    beams['Element ' + str(idx)] = beam                  # Naming each beam in ascending order

curr_angle = None
cs = CrossSectionLibrary('IPE300')


def stiffness_matrix(beams):
    for idx in range(0, 19):
        curr_beam = beams['Element ' + str(idx)].length
        # curr_beam = beams.angle
        # curr_angle = curr_beam.angle


stiffness_matrix(beams)

print('stop')


# plot_undeformed(coordinates, connectivity)


# for idx, coords in enumerate(coordinates):
#     plt.plot(coords[0], coords[1], 'ok', markersize=3)
#     plt.text(coords[0], coords[1], 'N' + str(idx), ha='right')
# plt.axis('equal')
# plt.show()
