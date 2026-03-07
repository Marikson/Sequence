import unittest
import tkinter as tk
from sequence import Sequence

class SequenceTest(unittest.TestCase):
    def test_grid_creation(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    

        test_game = Sequence()
        test_game.create_grid(test_field)

        self.assertEqual(len(test_game.model.grid), 10)
        for row in test_game.model.grid:
            self.assertEqual(len(row), 10)
        
        for r in range(10):
            for c in range(10):
                btn = test_game.model.grid[r][c]
                if (r == 0 and c == 0) or (r == 0 and c == 9) or (r == 9 and c == 0) or (r == 9 and c == 9):
                    self.assertEqual(btn["bg"], "Black")
                    self.assertEqual(btn["state"], "disabled")
                else:
                    self.assertEqual(btn["bg"], "White")
                    self.assertEqual(btn["state"], "normal")
    
    def test_grid_deletion(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)
        test_game.delete_grid()

        self.assertEqual(test_game.model.grid, [])

    def test_pick_cell(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        # Simulate a cell click
        test_game.model.on_cell_click(2, 3)
        test_game.model.picked_cell.row_index = 2
        test_game.model.picked_cell.col_index = 3
    
    def test_coloring_cell(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        # Simulate a cell click and color change
        test_game.model.on_cell_click(2, 3)
        test_game.model.set_color("Red")
        self.assertEqual(test_game.model.grid[2][3]["bg"], "Red")


if __name__ == '__main__':
    unittest.main()