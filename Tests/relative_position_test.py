import unittest
import tkinter as tk
from sequence import Sequence


class TestRelativePositionHorizontal(unittest.TestCase):
    def test_rel_pos_1(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 3)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 5)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(inline_minus_cells[0].row_index, 4)
        self.assertEqual(inline_minus_cells[0].col_index, 3)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -1)
        self.assertEqual(inline_plus_cells[0].row_index, 4)
        self.assertEqual(inline_plus_cells[0].col_index, 5)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 1)
        
    def test_rel_pos_2(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 2)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 6)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(inline_minus_cells[0].row_index, 4)
        self.assertEqual(inline_minus_cells[0].col_index, 2)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -2)
        self.assertEqual(inline_plus_cells[0].row_index, 4)
        self.assertEqual(inline_plus_cells[0].col_index, 6)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 2)
        
    def test_rel_pos_3(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 1)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 7)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(inline_minus_cells[0].row_index, 4)
        self.assertEqual(inline_minus_cells[0].col_index, 1)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -3)
        self.assertEqual(inline_plus_cells[0].row_index, 4)
        self.assertEqual(inline_plus_cells[0].col_index, 7)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 3)
        
    def test_rel_pos_4(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 0)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 8)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(inline_minus_cells[0].row_index, 4)
        self.assertEqual(inline_minus_cells[0].col_index, 0)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -4)
        self.assertEqual(inline_plus_cells[0].row_index, 4)
        self.assertEqual(inline_plus_cells[0].col_index, 8)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 4)
    
    
class TestRelativePositionVertical(unittest.TestCase):
    def test_rel_pos_1(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(3, 4)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(5, 4)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_vertical("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(inline_minus_cells[0].row_index, 3)
        self.assertEqual(inline_minus_cells[0].col_index, 4)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -1)
        self.assertEqual(inline_plus_cells[0].row_index, 5)
        self.assertEqual(inline_plus_cells[0].col_index, 4)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 1)
        
    def test_rel_pos_2(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(2, 4)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(6, 4)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_vertical("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(inline_minus_cells[0].row_index, 2)
        self.assertEqual(inline_minus_cells[0].col_index, 4)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -2)
        self.assertEqual(inline_plus_cells[0].row_index, 6)
        self.assertEqual(inline_plus_cells[0].col_index, 4)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 2)
        
    def test_rel_pos_3(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(1, 4)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(7, 4)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_vertical("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(inline_minus_cells[0].row_index, 1)
        self.assertEqual(inline_minus_cells[0].col_index, 4)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -3)
        self.assertEqual(inline_plus_cells[0].row_index, 7)
        self.assertEqual(inline_plus_cells[0].col_index, 4)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 3)
        
    def test_rel_pos_4(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(0, 4)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(8, 4)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_vertical("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(inline_minus_cells[0].row_index, 0)
        self.assertEqual(inline_minus_cells[0].col_index, 4)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -4)
        self.assertEqual(inline_plus_cells[0].row_index, 8)
        self.assertEqual(inline_plus_cells[0].col_index, 4)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 4)
    
    
class TestRelativePositionDiagonal(unittest.TestCase):
    def test_rel_pos_1(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(3, 4)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(5, 6)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 5)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(inline_minus_cells[0].row_index, 3)
        self.assertEqual(inline_minus_cells[0].col_index, 4)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -1)
        self.assertEqual(inline_plus_cells[0].row_index, 5)
        self.assertEqual(inline_plus_cells[0].col_index, 6)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 1)
        
    def test_rel_pos_2(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(2, 3)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(6, 7)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 5)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(inline_minus_cells[0].row_index, 2)
        self.assertEqual(inline_minus_cells[0].col_index, 3)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -2)
        self.assertEqual(inline_plus_cells[0].row_index, 6)
        self.assertEqual(inline_plus_cells[0].col_index, 7)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 2)
        
    def test_rel_pos_3(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(1, 2)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(7, 8)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 5)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(inline_minus_cells[0].row_index, 1)
        self.assertEqual(inline_minus_cells[0].col_index, 2)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -3)
        self.assertEqual(inline_plus_cells[0].row_index, 7)
        self.assertEqual(inline_plus_cells[0].col_index, 8)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 3)
        
    def test_rel_pos_4(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(0, 1)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(8, 9)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(4, 5)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(inline_minus_cells[0].row_index, 0)
        self.assertEqual(inline_minus_cells[0].col_index, 1)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, -4)
        self.assertEqual(inline_plus_cells[0].row_index, 8)
        self.assertEqual(inline_plus_cells[0].col_index, 9)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, 4)
    

class TestRelativePositionInvertedDiagonal(unittest.TestCase):
    def test_rel_pos_1(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 6)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(6, 4)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(5, 5)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_inverted_diagonal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 5)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(inline_minus_cells[0].row_index, 6)
        self.assertEqual(inline_minus_cells[0].col_index, 4)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, 1)
        self.assertEqual(inline_plus_cells[0].row_index, 4)
        self.assertEqual(inline_plus_cells[0].col_index, 6)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, -1)
        
    def test_rel_pos_2(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(3, 7)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(7, 3)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(5, 5)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_inverted_diagonal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 5)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(inline_minus_cells[0].row_index, 7)
        self.assertEqual(inline_minus_cells[0].col_index, 3)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, 2)
        self.assertEqual(inline_plus_cells[0].row_index, 3)
        self.assertEqual(inline_plus_cells[0].col_index, 7)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, -2)
        
    def test_rel_pos_3(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(2, 8)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(8, 2)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(5, 5)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_inverted_diagonal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 5)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(inline_minus_cells[0].row_index, 8)
        self.assertEqual(inline_minus_cells[0].col_index, 2)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, 3)
        self.assertEqual(inline_plus_cells[0].row_index, 2)
        self.assertEqual(inline_plus_cells[0].col_index, 8)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, -3)
        
    def test_rel_pos_4(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(1, 9)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(9, 1)
        test_game.model.set_color("Red")
        
        test_game.model.on_cell_click(5, 5)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_inverted_diagonal("Red")
            
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 5)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(inline_minus_cells[0].row_index, 9)
        self.assertEqual(inline_minus_cells[0].col_index, 1)
        self.assertEqual(inline_minus_cells[0].relative_position_to_picked_cell, 4)
        self.assertEqual(inline_plus_cells[0].row_index, 1)
        self.assertEqual(inline_plus_cells[0].col_index, 9)
        self.assertEqual(inline_plus_cells[0].relative_position_to_picked_cell, -4)

    
if __name__ == '__main__':
    unittest.main()
        