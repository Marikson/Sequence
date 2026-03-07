import unittest
import tkinter as tk
from sequence import Sequence


class InlinePerColorHorizontalMinusNOGap(unittest.TestCase):
    def test_0_inline(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 4)
        self.assertEqual(len(empty_plus_cells), 4)
        
    def test_1_inline_minus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for col in range(4, 6):
            test_game.model.on_cell_click(4, col)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 1)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 3)
        self.assertEqual(len(empty_plus_cells), 4)
        
        
    def test_2_inline_minus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for col in range(4, 7):
            test_game.model.on_cell_click(4, col)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 6)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 2)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 2)
        self.assertEqual(len(empty_plus_cells), 3)
        
    
    def test_3_inline_minus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for col in range(4, 8):
            test_game.model.on_cell_click(4, col)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 7)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 3)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 1)
        self.assertEqual(len(empty_plus_cells), 2)
        
        
    def test_4_inline_minus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for col in range(4, 9):
            test_game.model.on_cell_click(4, col)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 8)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 4)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 1)
        
    
    def test_4_inline_minus_hitting_plus_side(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for col in range(5, 10):
            test_game.model.on_cell_click(4, col)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 9)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 4)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 0)
        
        
        
    # def test_4_inline_minus_picked_cell_to_first(self):
    #     test_field = tk.Tk()
    #     test_field.title("Test Field")
    
    #     test_game = Sequence()
    #     test_game.create_grid(test_field)

    #     for col in range(5, 9):
    #         test_game.model.on_cell_click(4, col)
    #         test_game.model.set_color("Red")
    #     test_game.model.on_cell_click(4, 4)
                    
    #     color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
    #         gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
    #         = test_game.model.check_inline_per_color_horizontal("Red")
    #     self.assertEqual(color, "Red")
    #     self.assertEqual(picked_cell.row_index, 4)
    #     self.assertEqual(picked_cell.col_index, 4)
    #     self.assertEqual(opened_minus, True)
    #     self.assertEqual(opened_plus, False)
    #     self.assertEqual(len(inline_minus_cells), 0)
    #     self.assertEqual(len(inline_plus_cells), 4)
    #     self.assertEqual(len(gap_minus_cells), 0)
    #     self.assertEqual(len(gap_plus_cells), 0)
    #     self.assertEqual(len(empty_minus_cells), 4)
    #     self.assertEqual(len(empty_plus_cells), 0)
        
    
   
   

class InlinePerColorHorizontalMinusGapped(unittest.TestCase):       
    def test_1_inline_minus_1_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for col in range(4, 7, 2):
            test_game.model.on_cell_click(4, col)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 6)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 1)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 1)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 2)
        self.assertEqual(len(empty_plus_cells), 3)
        
    def test_1_inline_minus_2_contiguous_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for col in range(4, 8, 3):
            test_game.model.on_cell_click(4, col)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 7)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 1)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 2)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 1)
        self.assertEqual(len(empty_plus_cells), 2)
        
        
    def test_1_inline_minus_2_chess_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for col in range(4, 9, 2):
            test_game.model.on_cell_click(4, col)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 8)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 2)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 2)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 1)
        
        
        
        
        
        
class InlinePerColorHorizontalPlusNOGap(unittest.TestCase):      
    def test_1_inline_plus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        # Simulate a horizontal inline of 2 cells
        for col in range(5, 3, -1):
            test_game.model.on_cell_click(4, col)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 1)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 4)
        self.assertEqual(len(empty_plus_cells), 3)  
    
    
if __name__ == '__main__':
    unittest.main()
        