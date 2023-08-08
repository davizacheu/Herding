from landparcel import LandParcel
import numpy as np
import random

# class CELL_SIZE:
# Size of the land squares
CELL_SIZE = 4
# Radii for different vegetation levels
SPARSE_RADIUS = 8
PASTEL_RADIUS = 6
EUCALYPTUS_RADIUS = 4
HUNTER_RADIUS = 2


# @classmethod
def initialize_land(cls, procedural_cells):
    rows, cols = procedural_cells.shape
    land = []

    for row in range(rows):
        row_land_parcels = []
        for col in range(cols):
            if procedural_cells[row, col] == 1:
                land_parcel = LandParcel(4,
                                         col * CELL_SIZE,
                                         row * CELL_SIZE,
                                         CELL_SIZE - 1)
                row_land_parcels.append(land_parcel)
            else:
                # Find the closest entry of value 1 in the procedural_cells within vicinity

                min_distance = float('inf')  # Initialize with a large value
                for i in range(-SPARSE_RADIUS, SPARSE_RADIUS + 1):
                    for j in range(-SPARSE_RADIUS, SPARSE_RADIUS + 1):
                        if i == 0 and j == 0:
                            continue  # Skip the current cell
                        new_row, new_col = row + i, col + j
                        if 0 <= new_row < rows and 0 <= new_col < cols \
                                and procedural_cells[new_row, new_col] == 1:
                            distance = (i ** 2 + j ** 2) ** (1 / 2)
                            if distance < min_distance:
                                min_distance = distance

                parcel_vegetation =\
                    random.choices([])

        land.append(row_land_parcels)

    return land


def iterate_within_radius(matrix, center_row, center_col, radius):
    rows, cols = matrix.shape

    row_indices = np.arange(max(0, center_row - radius), min(rows, center_row + radius + 1))
    col_indices = np.arange(max(0, center_col - radius), min(cols, center_col + radius + 1))

    for row in row_indices:
        for col in col_indices:
            distance = np.sqrt((row - center_row) ** 2 + (col - center_col) ** 2)
            if distance <= radius:
                yield row, col
