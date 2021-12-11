def material_types(material):
    """Libary of different materials. Currently, only common steel types are supported.

        Usage example: material_types('355') returns material properties corresponding to S355 steel in a dictionary.
    """

    mat = {}
    mat['mass_density'] = 7850                                 # kg / m3
    mat['modulus_of_elasticity'] = 2.05 * 10**11               # Pa
    mat['possions_ratio'] = 0.3                                # No unit
    mat['shear_modulus'] = 2.05 * 10**11 / (2 * (1 + 0.3))     # Pa
    mat['bulk_modulus'] = 2.05 * 10**11 / (3 * (1 - 2 * 0.3))  # Pa
    if material == 'S235':
        mat['yield_strength'] = 225     # MPa (assuming 16 mm < t <= 40 mm)
        mat['ultimate_strength'] = 340  # MPa
    elif material == 'S275':
        mat['yield_strength'] = 345     # MPa (assuming 16 mm < t <= 40 mm)
        mat['ultimate_strength'] = 470  # MPa
    elif material == 'S355':
        mat['yield_strength'] = 345     # MPa (assuming 16 mm < t <= 40 mm)
        mat['ultimate_strength'] = 470  # MPa
    elif material == 'S450':
        mat['yield_strength'] = 430     # MPa (assuming 16 mm < t <= 40 mm)
        mat['ultimate_strength'] = 550  # MPa
    else:
        raise NameError('This material is not yet implemented. Please pick something else.')
    return mat
