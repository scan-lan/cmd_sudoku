from typing import TypeVar
from logic.types import BoxDimensions, Coords, Matrix

T = TypeVar("T")


def get_row(grid: Matrix[T], index: int) -> list[T]:
    return grid[index]


def get_col(grid: Matrix[T], index: int) -> list[T]:
    return [row[index] for row in grid]


def get_box_coords_from_matrix_coords(box_dimensions: BoxDimensions, coords: Coords) -> Coords:
    y, x = coords["y"], coords["x"]
    box_y, box_x = y % box_dimensions['h'], x % box_dimensions['w']
    return {'y': box_y, 'x': box_x}


def get_box_coords(box_dimensions: BoxDimensions, box_coords: Coords) -> list[Coords]:
    coords: list[Coords] = []
    box_offset_y = box_coords["y"] * box_dimensions["h"]
    box_offset_x = box_coords["x"] * box_dimensions["w"]
    for y in range(box_dimensions["h"]):
        for x in range(box_dimensions["w"]):
            coords.append({"y" : box_offset_y + y, "x": box_offset_x + x})
    return coords
