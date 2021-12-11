def system_matrices(input):
    """Explanation goes here."""

    # Help parameters for the stiffness matrix
    help1 = float(modulus_of_elasticity * cross_sectional_area) / float(element_length)         # EA / L
    help2 = float(12 * modulus_of_elasticity * moment_of_inertia) / float(element_length ** 3)  # 12EI / L^3
    help3 = float(6 * modulus_of_elasticity * moment_of_inertia) / float(element_length ** 2)   # 6EI / L^2
    help4 = float(4 * modulus_of_elasticity * moment_of_inertia) / float(element_length)        # 4EI / L
    help5 = float(2 * modulus_of_elasticity * moment_of_inertia) / float(element_length)        # 2EI / L

    # Local stifness matrix
    stifness_matrix = [[help1, 0, 0, -help1, 0, 0],
                       [0, help2, help3, 0, -help2, help3],
                       [0, help3, help4, 0, -help3, help5],
                       [-help1, 0, 0, help1, 0, 0],
                       [0, -help2, -help3, 0, help2, -help3],
                       [0, help3, help5, 0, -help3, help4]]

    # Help parameters for the mass matrix
    help6 = float(mass_density * cross_sectional_area * element_length) / float(420)            # pAL / 420
    help7 = float(element_length)                                                               # L
    help8 = float(element_length ** 2)                                                          # L^2

    # Local mass matrix
    mass_matrix = help6 * [[140, 0, 0, 70, 0, 0]
                           [0, 156, 22 * help7, 0, 54, -13 * help7],
                           [0, 22 * help7, 4 * help8, 0, 13 * help7, -3 * help8],
                           [70, 0, 0, 140, 0, 0],
                           [0, 54, 13 * help7, 0, 156, -22 * help7],
                           [0, -13 * help7, -3 * help8, 0, -22 * help7, 4 * help8]]


# mass_density = 0
# modulus_of_elasticity = 0
# modulus_shear = 0
# modulus_bulk = 0
# poisson_ratio = 0
# ultimate_Strength = 0
# yield_strength = 0
