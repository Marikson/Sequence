import unittest
import tkinter as tk
from sequence import Sequence


class InlinePerColorDiagonalMinusNOGap(unittest.TestCase):
    def test_0_inline(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(5, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 5)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 4)
        self.assertEqual(len(empty_plus_cells), 4)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_1_inline_minus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 2):
            test_game.model.on_cell_click(5 + i, 4 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 6)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 1)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 3)
        self.assertEqual(len(empty_plus_cells), 3)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
           
    def test_2_inline_minus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 3):
            test_game.model.on_cell_click(5 + i, 4 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 7)
        self.assertEqual(picked_cell.col_index, 6)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 2)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 2)
        self.assertEqual(len(empty_plus_cells), 2)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_3_inline_minus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 4):
            test_game.model.on_cell_click(5 + i, 4 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 8)
        self.assertEqual(picked_cell.col_index, 7)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 3)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 1)
        self.assertEqual(len(empty_plus_cells), 1)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_4_inline_minus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 5):
            test_game.model.on_cell_click(4 + i, 3 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 8)
        self.assertEqual(picked_cell.col_index, 7)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 4)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 1)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, "Red")
        
    def test_4_inline_minus_hitting_plus_side(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 5):
            test_game.model.on_cell_click(5 + i, 4 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 9)
        self.assertEqual(picked_cell.col_index, 8)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 4)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 0)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, "Red")
   
    def test_inline_minus_with_corner_as_4(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 4):
            test_game.model.on_cell_click(5 + i, 5 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 8)
        self.assertEqual(picked_cell.col_index, 8)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 3)
        self.assertEqual(len(inline_plus_cells), 1)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 1)
        self.assertEqual(len(empty_plus_cells), 0)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, "Red")          
   
   
class InlinePerColorDiagonalMinusGapped(unittest.TestCase):       
    def test_1_inline_minus_1_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 3, 2):
            test_game.model.on_cell_click(5 + i, 4 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 7)
        self.assertEqual(picked_cell.col_index, 6)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 1)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 1)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 2)
        self.assertEqual(len(empty_plus_cells), 2)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_1_inline_minus_2_contiguous_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 4, 3):
            test_game.model.on_cell_click(5 + i, 4 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 8)
        self.assertEqual(picked_cell.col_index, 7)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 1)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 2)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 1)
        self.assertEqual(len(empty_plus_cells), 1)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_1_inline_minus_3_contiguous_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 5, 4):
            test_game.model.on_cell_click(4 + i, 3 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 8)
        self.assertEqual(picked_cell.col_index, 7)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 1)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 3)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 1)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_2_inline_minus_2_contiguous_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 3)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(7, 6)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(8, 7)
        test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 8)
        self.assertEqual(picked_cell.col_index, 7)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 2)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 2)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 1)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_2_inline_minus_2_contiguous_gap_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)


        test_game.model.on_cell_click(4, 6)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(5, 7)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(8, 9)
        test_game.model.set_color("Red")
        
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 8)
        self.assertEqual(picked_cell.col_index, 9)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 2)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 2)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 1)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_2_inline_minus_2_chess_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 5, 2):
            test_game.model.on_cell_click(4 + i, 3 + i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 8)
        self.assertEqual(picked_cell.col_index, 7)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 2)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 2)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 1)
    
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)   
          
             
class InlinePerColorDiagonalPlusNOGap(unittest.TestCase):          
    def test_0_inline(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(3, 5)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 3)
        self.assertEqual(picked_cell.col_index, 5)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 0)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 3)
        self.assertEqual(len(empty_plus_cells), 4)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_1_inline_plus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)
        
        for i in range(0, 2):
            test_game.model.on_cell_click(5 - i, 7 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 4)
        self.assertEqual(picked_cell.col_index, 6)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 1)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 4)
        self.assertEqual(len(empty_plus_cells), 2)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
           
    def test_2_inline_plus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 3):
            test_game.model.on_cell_click(5 - i, 3 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 3)
        self.assertEqual(picked_cell.col_index, 1)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 2)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 1)
        self.assertEqual(len(empty_plus_cells), 2)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_3_inline_plus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 4):
            test_game.model.on_cell_click(5 - i, 7 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 2)
        self.assertEqual(picked_cell.col_index, 4)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 3)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 2)
        self.assertEqual(len(empty_plus_cells), 1)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_4_inline_plus(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 5):
            test_game.model.on_cell_click(5 - i, 7 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 1)
        self.assertEqual(picked_cell.col_index, 3)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 4)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 1)
        self.assertEqual(len(empty_plus_cells), 0)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, "Red")
        
    def test_4_inline_plus_hitting_minus_side(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 5):
            test_game.model.on_cell_click(4 - i, 6 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 0)
        self.assertEqual(picked_cell.col_index, 2)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 4)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 0)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, "Red")
        
    def test_inline_minus_with_corner_as_4(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 4):
            test_game.model.on_cell_click(4 - i, 4 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 1)
        self.assertEqual(picked_cell.col_index, 1)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 1)
        self.assertEqual(len(inline_plus_cells), 3)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 0)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 1)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, "Red")


class InlinePerColorDiagonalPlusGapped(unittest.TestCase):       
    def test_1_inline_minus_1_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 3, 2):
            test_game.model.on_cell_click(5 - i, 4 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 3)
        self.assertEqual(picked_cell.col_index, 2)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 1)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 1)
        self.assertEqual(len(empty_minus_cells), 2)
        self.assertEqual(len(empty_plus_cells), 2)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_1_inline_minus_2_contiguous_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 4, 3):
            test_game.model.on_cell_click(5 - i, 4 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 2)
        self.assertEqual(picked_cell.col_index, 1)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, True)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 1)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 2)
        self.assertEqual(len(empty_minus_cells), 1)
        self.assertEqual(len(empty_plus_cells), 1)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_1_inline_minus_3_contiguous_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 5, 4):
            test_game.model.on_cell_click(5 - i, 4 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 1)
        self.assertEqual(picked_cell.col_index, 0)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 1)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 3)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 0)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_2_inline_minus_2_contiguous_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(5, 4)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(2, 1)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(1, 0)
        test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 1)
        self.assertEqual(picked_cell.col_index, 0)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 2)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 2)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 0)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_2_inline_minus_2_contiguous_gap_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)


        test_game.model.on_cell_click(6, 5)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(5, 4)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(2, 1)
        test_game.model.set_color("Red")
        
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 2)
        self.assertEqual(picked_cell.col_index, 1)
        self.assertEqual(opened_minus, True)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 2)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 2)
        self.assertEqual(len(empty_minus_cells), 1)
        self.assertEqual(len(empty_plus_cells), 0)
        
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)
        
    def test_2_inline_minus_2_chess_gap(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(0, 5, 2):
            test_game.model.on_cell_click(4 - i, 6 - i)
            test_game.model.set_color("Red")
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_diagonal("Red")
        self.assertEqual(color, "Red")
        self.assertEqual(picked_cell.row_index, 0)
        self.assertEqual(picked_cell.col_index, 2)
        self.assertEqual(opened_minus, False)
        self.assertEqual(opened_plus, False)
        self.assertEqual(len(inline_minus_cells), 0)
        self.assertEqual(len(inline_plus_cells), 2)
        self.assertEqual(len(gap_minus_cells), 0)
        self.assertEqual(len(gap_plus_cells), 2)
        self.assertEqual(len(empty_minus_cells), 0)
        self.assertEqual(len(empty_plus_cells), 0)
    
        winner = test_game.model.check_winner()
        self.assertEqual(winner, False)   
          
    
if __name__ == '__main__':
    unittest.main()
        