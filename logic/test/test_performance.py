from typing import Any
from logic.create_grid import (create_coef_matrix, create_grid,
                               fill_free_boxes, initialise_weights, iterate)
from logic.free_boxes import get_free_coords
from logic.get_groups import get_coords_in_box
from logic.types import CoefficientMatrix, Coords, Dimensions


def test_get_coords_in_box(benchmark: Any, box_dimensions: Dimensions):
    w, h = box_dimensions["w"], box_dimensions["h"]
    benchmark(get_coords_in_box, box_dimensions, (h - 1, w - 1))


def test_create_matrix(benchmark: Any, box_dimensions: Dimensions):
    size = box_dimensions["w"] * box_dimensions["h"]
    benchmark(create_coef_matrix, size)


def test_get_free_coords(benchmark: Any, box_dimensions: Dimensions):
    benchmark(get_free_coords, box_dimensions)


def test_fill_free_boxes(benchmark: Any,
                         coef_matrix_with_box_dimensions: tuple[CoefficientMatrix, Dimensions]):
    weights = initialise_weights(len(coef_matrix_with_box_dimensions[0]))
    collapsed: set[Coords] = set()
    benchmark(fill_free_boxes, coef_matrix_with_box_dimensions[0],
              coef_matrix_with_box_dimensions[1], weights, collapsed, seed=0)


def test_iterate(benchmark: Any,
                 coef_matrix_with_box_dimensions: tuple[CoefficientMatrix, Dimensions]):
    weights = initialise_weights(len(coef_matrix_with_box_dimensions[0]))
    collapsed: set[Coords] = set()
    benchmark(iterate, coef_matrix_with_box_dimensions[0],
              coef_matrix_with_box_dimensions[1], weights, collapsed, seed=0)


def test_create_grid(benchmark: Any, box_dimensions: Dimensions):
    result_grid, _ = benchmark(create_grid, box_dimensions, seed=0)
    assert len(result_grid) == box_dimensions["w"] * box_dimensions["h"]
