from cross_section_libary import cross_section_libary


class CrossSection:
    def __init__(self):
        self.name = ''              # Section name
        self.area = 0               # Axial area (cm2)
        self.shear_area_z = 0       # V-shear area (cm2)
        self.shear_area_y = 0       # W-shear area (cm2)
        self.torsion_inertia = 0    # Torsion inertia (cm4)
        self.flex_intertia_z = 0    # Flex. inertia about V-axis (cm4)
        self.flex_intertia_y = 0    # Flex. inertia about W-axis (cm4)
        self.section_modulus_z = 0  # Section modulus about V-axis (cm3)
        self.section_modulus_y = 0  # Section modulus about W-axis (cm3)


class CrossSectionLibary(CrossSection):
    def __init__(self, cross_section):
        super().__init__()
        if cross_section not in cross_section_libary:
            raise KeyError(
                f'"{cross_section}" is not yet implemented. Please pick a cross-section from: {cross_section_libary.keys()}')
        self.name = cross_section
        self.type = cross_section_libary[cross_section][0]
        self.area = cross_section_libary[cross_section][1] * 100
        self.shear_area_z = cross_section_libary[cross_section][2] * 100
        self.shear_area_y = cross_section_libary[cross_section][3] * 100
        self.torsion_inertia = cross_section_libary[cross_section][4] * 10000
        self.flex_intertia_z = cross_section_libary[cross_section][5] * 10000
        self.flex_intertia_y = cross_section_libary[cross_section][6] * 10000
        self.section_modulus_z = cross_section_libary[cross_section][7] * 1000
        self.section_modulus_y = cross_section_libary[cross_section][8] * 1000
