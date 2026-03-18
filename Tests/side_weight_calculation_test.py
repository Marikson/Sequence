import unittest
import tkinter as tk
from sequence import Sequence

class SideWeightCalculationTest(unittest.TestCase):
    # Pattern:
    # P: picked cell
    # I: inline cell
    # G: gap cell
    # E: empty cell
    def test_EEEIPEEEE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 3)
        test_game.model.set_color("Red")

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        self.assertEqual(minus_inline_weight, 1)
        self.assertEqual(plus_inline_weight, 100)
        self.assertEqual(minus_gap_weight, 100)
        self.assertEqual(plus_gap_weight, 100)
        self.assertEqual(minus_empty_weight, 3)
        self.assertEqual(plus_empty_weight, 4)
        
        self.assertLessEqual(minus_inline_weight, plus_inline_weight)
        self.assertLessEqual(minus_gap_weight, plus_gap_weight)
        self.assertLess(minus_empty_weight, plus_empty_weight)
        
    def test_EEIGPEEEE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 2)
        test_game.model.set_color("Red")

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)

        self.assertEqual(minus_inline_weight, 2)
        self.assertEqual(plus_inline_weight, 100)
        self.assertEqual(minus_gap_weight, 1)
        self.assertEqual(plus_gap_weight, 100)
        self.assertEqual(minus_empty_weight, 2)
        self.assertEqual(plus_empty_weight, 4)
        
        self.assertLessEqual(minus_inline_weight, plus_inline_weight)
        self.assertLessEqual(minus_gap_weight, plus_gap_weight)
        self.assertLess(minus_empty_weight, plus_empty_weight)
        
    def test_EEEIPGIEE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 3)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 6)
        test_game.model.set_color("Red")

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        self.assertEqual(minus_inline_weight, 1)
        self.assertEqual(plus_inline_weight, 2)
        self.assertEqual(minus_gap_weight, 100)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 3)
        self.assertEqual(plus_empty_weight, 2)
        
        self.assertLessEqual(minus_inline_weight, plus_inline_weight)
  
    def test_EEIIPGIEE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 3)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 2)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 6)
        test_game.model.set_color("Red")

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        self.assertEqual(minus_inline_weight, 1)
        self.assertEqual(plus_inline_weight, 2)
        self.assertEqual(minus_gap_weight, 100)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 2)
        self.assertEqual(plus_empty_weight, 2)
        
        self.assertLessEqual(minus_inline_weight, plus_inline_weight)

    def test_EIGIPGIIE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 3)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 1)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 6)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 7)
        test_game.model.set_color("Red")

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        self.assertEqual(minus_inline_weight, 1)
        self.assertEqual(plus_inline_weight, 3)
        self.assertEqual(minus_gap_weight, 2)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 1)
        self.assertEqual(plus_empty_weight, 1)
        
        self.assertLessEqual(minus_inline_weight, plus_inline_weight)

if __name__ == '__main__':
    unittest.main()