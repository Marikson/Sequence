import unittest
import tkinter as tk
from sequence import Sequence

class SequenceTest(unittest.TestCase):
    def test_grid_creation(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.grid
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
        test_game.model.clicked_cell = {"r": 2, "c": 3}
        r, c = test_game.pick_cell()
        self.assertEqual(r, 2)
        self.assertEqual(c, 3)
    
    def test_coloring_cell(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        # Simulate a cell click and color change
        test_game.model.clicked_cell = {"r": 2, "c": 3}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        self.assertEqual(test_game.model.grid[r][c]["bg"], "Red")


if __name__ == '__main__':
    unittest.main()