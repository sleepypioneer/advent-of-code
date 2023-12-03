from .challenge import create_grid, Cell, Grid, find_numbers_touching_symbols

TEST_SCHEMATIC = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_create_grid():
    grid = create_grid(TEST_SCHEMATIC)
    expected = Grid(
        items=[
            [
                Cell(0, 0, "4", False, True),
                Cell(1, 0, "6", False, True),
                Cell(2, 0, "7", False, True),
                Cell(3, 0, ".", False, False),
                Cell(4, 0, ".", False, False),
                Cell(5, 0, "1", False, True),
                Cell(6, 0, "1", False, True),
                Cell(7, 0, "4", False, True),
                Cell(8, 0, ".", False, False),
                Cell(9, 0, ".", False, False),
            ],
            [
                Cell(0, 1, ".", False, False),
                Cell(1, 1, ".", False, False),
                Cell(2, 1, ".", False, False),
                Cell(3, 1, "*", True, False),
                Cell(4, 1, ".", False, False),
                Cell(5, 1, ".", False, False),
                Cell(6, 1, ".", False, False),
                Cell(7, 1, ".", False, False),
                Cell(8, 1, ".", False, False),
                Cell(9, 1, ".", False, False),
            ],
        ]
    )

    assert isinstance(grid, Grid)
    assert compare_rows(grid.items[0], expected.items[0])
    assert compare_rows(grid.items[1], expected.items[1])


def test_find_numbers_touching_symbols():
    grid = create_grid(TEST_SCHEMATIC)
    numbers_touching_symbols = find_numbers_touching_symbols(grid)
    assert numbers_touching_symbols == [467, 35, 633, 617, 592, 755, 664, 598]


def test_challenges_one():
    expected = 4361
    grid = create_grid(TEST_SCHEMATIC)
    numbers_touching_symbols = find_numbers_touching_symbols(grid)
    sum_numbers = sum(numbers_touching_symbols)
    assert sum_numbers == expected


def compare_rows(row_1: list[Cell], row_2: list[Cell]) -> bool:
    return all([row_1[idx].compare(row_2[idx]) for idx in range(len(row_1))])
