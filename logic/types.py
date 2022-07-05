from typing import Literal, TypeAlias, TypeVar

DimensionsKey: TypeAlias = Literal["w", "h"]
Dimensions: TypeAlias = dict[DimensionsKey, int]

Coords: TypeAlias = tuple[int, int]

Cell: TypeAlias = str
Grid: TypeAlias = list[list[Cell]]

T = TypeVar("T")
Matrix: TypeAlias = list[list[T]]

Coefficients: TypeAlias = set[Cell]
CoefficientMatrix: TypeAlias = Matrix[Coefficients]

Weights: TypeAlias = dict[Cell, int]
Collapsed: TypeAlias = set[Coords]

GroupName: TypeAlias = Literal["row", "col", "box"]
GroupConstraints: TypeAlias = dict[GroupName, Coefficients]

HistoryEntry: TypeAlias = tuple[Collapsed, Weights, CoefficientMatrix]
History: TypeAlias = list[HistoryEntry]




