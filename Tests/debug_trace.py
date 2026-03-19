"""Debug trace for the [3][2] corner case."""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import tkinter as tk
from sequence import Sequence

test_field = tk.Tk()
test_field.title("Debug")

test_game = Sequence()
test_game.create_grid(test_field)

# Set up the board:
# Colored cells: [3][1], [3][3], [3][4], [3][6]
for col in [1, 3, 4, 6]:
    test_game.model.on_cell_click(3, col)
    test_game.model.set_color("Green")

# Now pick [3][2]
test_game.model.on_cell_click(3, 2)
test_game.model.set_color("Green")

# Run horizontal check
color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
    gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
    = test_game.model.check_inline_per_color_horizontal("Green")

print("=== RAW DATA FROM check_inline_per_color_horizontal ===")
print(f"Picked cell: [{picked_cell.row_index}][{picked_cell.col_index}]")
print(f"opened_minus: {opened_minus}, opened_plus: {opened_plus}")
print(f"inline_minus_cells: {[(c.row_index, c.col_index, c.relative_position_to_picked_cell) for c in inline_minus_cells]}")
print(f"inline_plus_cells: {[(c.row_index, c.col_index, c.relative_position_to_picked_cell) for c in inline_plus_cells]}")
print(f"gap_minus_cells: {[(c.row_index, c.col_index, c.relative_position_to_picked_cell) for c in gap_minus_cells]}")
print(f"gap_plus_cells: {[(c.row_index, c.col_index, c.relative_position_to_picked_cell) for c in gap_plus_cells]}")
print(f"empty_minus_cells: {[(c.row_index, c.col_index, c.relative_position_to_picked_cell) for c in empty_minus_cells]}")
print(f"empty_plus_cells: {[(c.row_index, c.col_index, c.relative_position_to_picked_cell) for c in empty_plus_cells]}")

# Now call determine_inline directly
cell = test_game.model.picked_cell
result = test_game.model.determine_inline(
    cell,
    inline_minus_cells, inline_plus_cells,
    list(reversed(gap_minus_cells)), list(reversed(gap_plus_cells)),
    empty_minus_cells, empty_plus_cells
)

print("\n=== RESULT FROM determine_inline ===")
print(f"Inline: {result['inline']}")
print(f"Open in middle: {result['open_in_middle']}")
print(f"Empty middle counter: {result['empty_middle_counter']}")
print(f"One ended: {result['one_ended']}")
print(f"Two ended: {result['two_ended']}")
print(f"Inline cells: {[f'[{c.row_index}][{c.col_index}]' for c in result['inline_cells']]}")
print(f"Empty middle cells: {[f'[{c.row_index}][{c.col_index}]' for c in result['empty_middle_cells']]}")
print(f"Empty cells: {[f'[{c.row_index}][{c.col_index}]' for c in result['empty_cells']]}")

print("\n=== EXPECTED ===")
print("Inline: 4")
print("Open in middle: False")
print("Empty middle counter: 0")
print("One ended: False")
print("Two ended: True")
print("Inline cells: ['[3][1]', '[3][2]', '[3][3]', '[3][4]']")
print("Empty middle cells: []")
print("Empty cells: ['[3][0]', '[3][5]']")

test_field.destroy()
