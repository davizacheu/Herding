class LandParcel:
    # Define color constants as class-level attributes
    DESERT = (245, 245, 220)
    SPARSE = (236, 255, 220)
    PASTEL_GREEN = (193, 225, 193)
    EUCALYPTUS = (95, 133, 117)
    HUNTER_GREEN = (53, 94, 59)

    def __init__(self, vegetation, x_origin, y_origin, side):
        self.vegetation = vegetation
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.length = side
        self.color = self.get_color()

    def get_color(self):
        # Use a dictionary to map vegetation values to colors
        vegetation_color_map = {
            0: self.DESERT,
            1: self.SPARSE,
            2: self.PASTEL_GREEN,
            3: self.EUCALYPTUS,
            4: self.HUNTER_GREEN
        }
        return vegetation_color_map.get(self.vegetation,
                                        (0, 0, 0))  # Default to black if vegetation value is not recognized
