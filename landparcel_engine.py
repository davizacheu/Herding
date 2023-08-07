from landparcel import LandParcel


class LandParcelEngine:
    # Size of the land squares
    CELL_SIZE = 4
    # Radii for different vegetation levels
    SPARSE_RADIUS = 8
    PASTEL_RADIUS = 6
    EUCALYPTUS_RADIUS = 4
    HUNTER_RADIUS = 2

    @classmethod
    def initialize_land(cls, procedural_cells):
        rows, cols = procedural_cells.shape
        land = []

        for row in range(rows):
            row_land_parcels = []
            for col in range(cols):
                if procedural_cells[row, col] == 1:
                    land_parcel = LandParcel(4,
                                             col * LandParcelEngine.CELL_SIZE,
                                             row * LandParcelEngine.CELL_SIZE,
                                             LandParcelEngine.CELL_SIZE - 1)
                    row_land_parcels.append(land_parcel)
                else:
                    # Find the closest entry of value 1 in the procedural_cells within vicinity
                    min_distance = float('inf')  # Initialize with a large value
                    closest_row, closest_col = None, None

                    for i in range(-LandParcelEngine.SPARSE_RADIUS, LandParcelEngine.SPARSE_RADIUS + 1):
                        for j in range(-LandParcelEngine.SPARSE_RADIUS, LandParcelEngine.SPARSE_RADIUS + 1):
                            if i == 0 and j == 0:
                                continue  # Skip the current cell
                            new_row, new_col = row + i, col + j
                            if 0 <= new_row < rows and 0 <= new_col < cols \
                                    and procedural_cells[new_row, new_col] == 1:
                                distance = (i ** 2 + j ** 2) ** (1 / 2)
                                if distance < min_distance:
                                    min_distance = distance
                                    closest_row, closest_col = new_row, new_col

            land.append(row_land_parcels)

        return land
