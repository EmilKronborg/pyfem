
class Material:
    """
    Base class for all materials.
    """
    # TODO: Implement the shear area coefficient for Timeshenko beam theory.

    def __init__(self):
        self.mass_density = 0           # kg / M^3
        self.modulus_of_elasticity = 0  # Pa
        self.poissons_ratio = 0         # No unit
        self.shear_modulus = 0          # Pa
        self.bulk_modulus = 0           # Pa
        self.ultimate_strength = 0      # Pa
        self.yield_strength = 0         # Pa


class Steel(Material):
    """
    Super class for steel. Here, the attributes of the Material class are inherited, while some specific values, corre-
    sponding to structural steel, are set.
    """
    # TODO: _steel_type correctly returns the right string, but steel_type returns None. Why?

    def __init__(self, steel_type):
        super().__init__()
        self.mass_density = 7850
        self.modulus_of_elasticity = 205e9
        self.poissons_ratio = 0.3
        self.shear_modulus = self.modulus_of_elasticity / (2 * (1 + self.poissons_ratio))
        self.bulk_modulus = self.modulus_of_elasticity / (3 * (1 - 2 * self.poissons_ratio))
        self._steel_type = steel_type

    @property
    def steel_type(self):
        # S235 steel (assuming 16 mm < t <= 40 mm)
        if self._steel_type == 'S235':
            self.yield_strength = 225e6
            self.ultimate_strength = 340e6
        # S275 steel (assuming 16 mm < t <= 40 mm)
        elif self._steel_type == 'S275':
            self.yield_strength = 345e6
            self.ultimate_strength = 470e6
        # S355 steel (assuming 16 mm < t <= 40 mm)
        elif self._steel_type == 'S355':
            self.yield_strength = 345e6
            self.ultimate_strength = 470e6
        # S450 steel (assuming 16 mm < t <= 40 mm)
        elif self._steel_type == 'S450':
            self.yield_strength = 430
            self.ultimate_strength = 550
        else:
            raise NameError(f'"{self._steel_type}" is not yet implemented. Please pick something else.')

    @steel_type.setter
    def steel_type(self, value):
        if not isinstance(value, str):
            raise TypeError(f'"steel_type" must be a string, but is of type {type(self._steel_type)}.')
        self._steel_type = value
