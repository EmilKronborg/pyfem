def topology(coordinates, connectivity):
    """This function assign degrees of freedom (DOF) to each node and each beam element.

    Parameters
    ----------
    coordinates : list
        Coordinate for each nodal point given in meters.
    connectivity : list
        The connectivity of the given nodal points, that is, the spatial definition of each beam element.

    Returns
    -------
    [type]
        [description]
    """

    # Getting total number of nodes and initializing beam_dof.
    number_of_nodes = len(coordinates)
    beam_dof = []

    # Generating a matrix containing the nodal DOF.
    nodal_dof = [(idx * 3 + 1, idx * 3 + 2, idx * 3 + 3) for idx in range(number_of_nodes)]

    # Assigning DOF to each beam element based on the connectivity.
    for node_1, node_2 in connectivity:
        beam_dof.append((*nodal_dof[node_1], *nodal_dof[node_2]))

    return nodal_dof, beam_dof

