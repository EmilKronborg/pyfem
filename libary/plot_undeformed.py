import matplotlib.pyplot as plt


def plot_undeformed(coordinates, connectivity):
    # TODO: change font type and size, fix the ticks so that they only occur at nodes.

    for node_i, node_j in connectivity:
        # Spatial coordinates for node_i and node_j.
        help1 = coordinates[node_i][0], coordinates[node_j][0]
        help2 = coordinates[node_i][1], coordinates[node_j][1]

        plt.plot(help1, help2, 'ok', markersize=3)  # Plotting the nodal points
        plt.plot(help1, help2, 'k', linewidth=1)    # Plotting the beam elements

    # Set the axis.
    # plt.axis('off')       # Turn off the axis
    plt.axis('equal')       # 1st and 2nd axis equal size

    # Set the font
    ax = plt.gca()          # Get the axis of the current plot
    ax.set_xlabel('x [m]')  # Setting the xlabel
    ax.set_ylabel('y [m]')  # Setting the ylabel
    # ax.annotate('txt', help1, help2)

    plt.text(help1[0], help1[1], 'txt')

    # Show the plot
    plt.show()


# return print(help1)

# # Stuff used to plot the height and width of a frame structure.
# # Minimum and maximum values in coordinates.
# min_x = min(coordinates)[0]
# max_x = max(coordinates)[0]
# min_y = min(coordinates)[1]
# max_y = max(coordinates)[1]

# # Height of the frame.
# ax = plt.gca()  # Get the axis of the current plot
# ax.annotate('', [-0.02, min_y], [-0.02, max_y], arrowprops=dict(arrowstyle='<->'))

# # Width of the frame.
# ax.annotate("", [min_x, -0.02], [max_x, -0.02], arrowprops=dict(arrowstyle='<->'))
