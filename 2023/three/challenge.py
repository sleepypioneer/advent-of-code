from dataclasses import dataclass


@dataclass
class Cell:
    """
    Cell class
    """

    x: int
    y: int
    value: str
    is_symbol: bool = False
    is_number: bool = False
    checked: bool = False

    def compare(self, other: object) -> bool:
        try:
            return (
                self.x == other.x
                and self.y == other.y
                and self.value == other.value
                and self.is_symbol == other.is_symbol
                and self.is_number == other.is_number
            )
        except AttributeError:
            return NotImplemented


@dataclass
class Grid:
    """
    Grid class
    """

    items: list[list[Cell]]

    def get_number_cells(self) -> list[Cell]:
        return [cell for row in self.items for cell in row if cell.is_number]

    def get_symbol_cells(self) -> list[Cell]:
        return [cell for row in self.items for cell in row if cell.is_symbol]


def create_grid(schematic: str) -> Grid:
    """
    returns a grid of rows of cells
    example schematic = "467..114..\n...*......\n..35..633."
    expected grid = [
        ["4", "6", "7", ".", ".", "1", "1", "4", "."],
        [".", ".", ".", "*", ".", ".", ".", ".", "."],
        [".", ".", "3", "5", ".", ".", "6", "3", "3"],
    ]

    :param schematic: schematic
    :type schematic: str
    :return: list
    :rtype: list
    """
    return Grid(
        items=[
            [
                Cell(
                    x,
                    y,
                    value,
                    is_symbol(value),
                    value.isdigit(),
                )
                for x, value in enumerate(list(row))
            ]
            for y, row in enumerate(schematic.splitlines())
        ]
    )


def is_symbol(value: str) -> bool:
    return value != "." and not value.isdigit()


def find_numbers_touching_symbols(grid: Grid) -> list[int]:
    numbers_touching_symbols = []

    for cell in grid.get_number_cells():
        if cell.checked or not cell.is_number:
            continue

        neighbors = []
        number_value = int(cell.value)
        cell.checked = True

        left_neighbor = get_left_neighbor(cell, grid)
        if left_neighbor is not None:
            # add left neighbor and the ones above it and below it (diagonal matches)
            top_left_neighbor = get_top_neighbor(left_neighbor, grid)
            bottom_left_neighbor = get_bottom_neighbor(left_neighbor, grid)
            neighbors.extend([left_neighbor, top_left_neighbor, bottom_left_neighbor])

        top_neighbor = get_top_neighbor(cell, grid)
        bottom_neighbor = get_bottom_neighbor(cell, grid)
        neighbors.extend([top_neighbor, bottom_neighbor])

        right_neighbor = get_right_neighbor(cell, grid)
        while right_neighbor is not None and right_neighbor.is_number:
            right_neighbor.checked = True

            top_neighbor = get_top_neighbor(right_neighbor, grid)
            bottom_neighbor = get_bottom_neighbor(right_neighbor, grid)
            neighbors.extend([top_neighbor, bottom_neighbor])

            number_value = int(f"{number_value}{right_neighbor.value}")
            right_neighbor = get_right_neighbor(right_neighbor, grid)

        if right_neighbor is not None:
            # add last right neighbor and the ones above it and below it (diagonal matches)
            top_right_neighbor = get_top_neighbor(right_neighbor, grid)
            bottom_right_neighbor = get_bottom_neighbor(right_neighbor, grid)
            neighbors.extend(
                [
                    top_right_neighbor,
                    bottom_right_neighbor,
                    right_neighbor,
                ]
            )

        for neighbor in neighbors:
            if neighbor is None:
                continue
            if neighbor.is_symbol:
                numbers_touching_symbols.append(number_value)
                break

    return numbers_touching_symbols


def get_left_neighbor(cell: Cell, grid: Grid) -> Cell:
    if cell.x == 0:
        return None
    return grid.items[cell.y][cell.x - 1]


def get_right_neighbor(cell: Cell, grid: Grid) -> Cell:
    if cell.x == len(grid.items[cell.y]) - 1:
        return None
    return grid.items[cell.y][cell.x + 1]


def get_top_neighbor(cell: Cell, grid: Grid) -> Cell:
    if cell.y == 0:
        return None
    return grid.items[cell.y - 1][cell.x]


def get_bottom_neighbor(cell: Cell, grid: Grid) -> Cell:
    if cell.y == len(grid.items) - 1:
        return None
    return grid.items[cell.y + 1][cell.x]
