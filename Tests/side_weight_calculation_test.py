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
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 1)
        self.assertEqual(plus_inline_count, 0)
        self.assertEqual(minus_inline_weight, 1)
        self.assertEqual(plus_inline_weight, 100)
        self.assertEqual(minus_gap_weight, 100)
        self.assertEqual(plus_gap_weight, 100)
        self.assertEqual(minus_empty_weight, 3)
        self.assertEqual(plus_empty_weight, 4)
        
        self.assertEqual(process_order, ["minus", "plus"])
     
     
    def test_EEEEPIEEE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 5)
        test_game.model.set_color("Red")

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 0)
        self.assertEqual(plus_inline_count, 1)
        self.assertEqual(minus_inline_weight, 100)
        self.assertEqual(plus_inline_weight, 1)
        self.assertEqual(minus_gap_weight, 100)
        self.assertEqual(plus_gap_weight, 100)
        self.assertEqual(minus_empty_weight, 4)
        self.assertEqual(plus_empty_weight, 3)
        
        self.assertEqual(process_order, ["plus", "minus"])    
    
    
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
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)

        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)

        self.assertEqual(minus_inline_count, 1)
        self.assertEqual(plus_inline_count, 0)
        self.assertEqual(minus_inline_weight, 2)
        self.assertEqual(plus_inline_weight, 100)
        self.assertEqual(minus_gap_weight, 1)
        self.assertEqual(plus_gap_weight, 100)
        self.assertEqual(minus_empty_weight, 2)
        self.assertEqual(plus_empty_weight, 4)
        
        self.assertEqual(process_order, ["minus", "plus"])
        
    
    def test_EEEEPGIEE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 6)
        test_game.model.set_color("Red")

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 0)
        self.assertEqual(plus_inline_count, 1)
        self.assertEqual(minus_inline_weight, 100)
        self.assertEqual(plus_inline_weight, 2)
        self.assertEqual(minus_gap_weight, 100)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 4)
        self.assertEqual(plus_empty_weight, 2)
        
        self.assertEqual(process_order, ["plus", "minus"])
     
        
    def test_EEEIPIEEE(self):
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
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 1)
        self.assertEqual(plus_inline_count, 1)
        self.assertEqual(minus_inline_weight, 1)
        self.assertEqual(plus_inline_weight, 1)
        self.assertEqual(minus_gap_weight, 100)
        self.assertEqual(plus_gap_weight, 100)
        self.assertEqual(minus_empty_weight, 3)
        self.assertEqual(plus_empty_weight, 3)
        
        self.assertEqual(process_order, ["minus", "plus"])
        
            
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
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 1)
        self.assertEqual(plus_inline_count, 1)
        self.assertEqual(minus_inline_weight, 1)
        self.assertEqual(plus_inline_weight, 2)
        self.assertEqual(minus_gap_weight, 100)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 3)
        self.assertEqual(plus_empty_weight, 2)
        
        self.assertEqual(process_order, ["minus", "plus"])
      
      
    def test_EEIGPIEEE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 2)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 5)
        test_game.model.set_color("Red")

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 1)
        self.assertEqual(plus_inline_count, 1)
        self.assertEqual(minus_inline_weight, 2)
        self.assertEqual(plus_inline_weight, 1)
        self.assertEqual(minus_gap_weight, 1)
        self.assertEqual(plus_gap_weight, 100)
        self.assertEqual(minus_empty_weight, 2)
        self.assertEqual(plus_empty_weight, 3)
        
        self.assertEqual(process_order, ["plus", "minus"])
    
    
    def test_EEIGPGIEE(self):
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
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 1)
        self.assertEqual(plus_inline_count, 1)
        self.assertEqual(minus_inline_weight, 2)
        self.assertEqual(plus_inline_weight, 2)
        self.assertEqual(minus_gap_weight, 1)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 2)
        self.assertEqual(plus_empty_weight, 2)
        
        self.assertEqual(process_order, ["minus", "plus"])    
  
  
    def test_EEIGPGGIE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 2)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 7)
        test_game.model.set_color("Red")

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 1)
        self.assertEqual(plus_inline_count, 1)
        self.assertEqual(minus_inline_weight, 2)
        self.assertEqual(plus_inline_weight, 3)
        self.assertEqual(minus_gap_weight, 1)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 2)
        self.assertEqual(plus_empty_weight, 1)
        
        self.assertEqual(process_order, ["minus", "plus"])
  
 
    def test_EEIGPGGII(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 2)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 7)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 8)
        test_game.model.set_color("Red")
        

        test_game.model.on_cell_click(4, 4)
        test_game.model.set_color("Red")
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
            gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
            = test_game.model.check_inline_per_color_horizontal("Red")
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 1)
        self.assertEqual(plus_inline_count, 2)
        self.assertEqual(minus_inline_weight, 2)
        self.assertEqual(plus_inline_weight, 6)
        self.assertEqual(minus_gap_weight, 1)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 2)
        self.assertEqual(plus_empty_weight, 0)
        
        self.assertEqual(process_order, ["plus", "minus"])
    
  
    # def test_EIGIPGIIE(self):
    #     test_field = tk.Tk()
    #     test_field.title("Test Field")
    
    #     test_game = Sequence()
    #     test_game.create_grid(test_field)

    #     test_game.model.on_cell_click(4, 3)
    #     test_game.model.set_color("Red")
    #     test_game.model.on_cell_click(4, 1)
    #     test_game.model.set_color("Red")
    #     test_game.model.on_cell_click(4, 6)
    #     test_game.model.set_color("Red")
    #     test_game.model.on_cell_click(4, 7)
    #     test_game.model.set_color("Red")
        

    #     test_game.model.on_cell_click(4, 4)
    #     test_game.model.set_color("Red")
    #     color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
    #         gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
    #         = test_game.model.check_inline_per_color_horizontal("Red")
        
        
    #     minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
    #     plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
    #     process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
    #     self.assertEqual(minus_inline_count, 2)
    #     self.assertEqual(plus_inline_count, 2)
    #     self.assertEqual(minus_inline_weight, 2)
    #     self.assertEqual(plus_inline_weight, 3)
    #     self.assertEqual(minus_gap_weight, 2)
    #     self.assertEqual(plus_gap_weight, 1)
    #     self.assertEqual(minus_empty_weight, 1)
    #     self.assertEqual(plus_empty_weight, 1)
        
    #     self.assertEqual(process_order, ["plus", "minus"])
  
  
    def test_IGIGPGIIE(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.on_cell_click(4, 0)
        test_game.model.set_color("Red")
        test_game.model.on_cell_click(4, 2)
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
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 2)
        self.assertEqual(plus_inline_count, 2)
        self.assertEqual(minus_inline_weight, 4)
        self.assertEqual(plus_inline_weight, 3)
        self.assertEqual(minus_gap_weight, 1)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 0)
        self.assertEqual(plus_empty_weight, 1)
        
        self.assertEqual(process_order, ["plus", "minus"])
  
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
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 2)
        self.assertEqual(plus_inline_count, 1)
        self.assertEqual(minus_inline_weight, 1)
        self.assertEqual(plus_inline_weight, 2)
        self.assertEqual(minus_gap_weight, 100)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 2)
        self.assertEqual(plus_empty_weight, 2)
        
        self.assertEqual(process_order, ["minus", "plus"])
        

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
        
        
        minus_inline_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = test_game.model.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = test_game.model.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        process_order = test_game.model.get_direction_order(minus_inline_count, plus_inline_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        self.assertEqual(minus_inline_count, 2)
        self.assertEqual(plus_inline_count, 2)
        self.assertEqual(minus_inline_weight, 1)
        self.assertEqual(plus_inline_weight, 3)
        self.assertEqual(minus_gap_weight, 2)
        self.assertEqual(plus_gap_weight, 1)
        self.assertEqual(minus_empty_weight, 1)
        self.assertEqual(plus_empty_weight, 1)
        
        self.assertEqual(process_order, ["minus", "plus"])
        

    def test_EIPGIIE(self):
        pass



if __name__ == '__main__':
    unittest.main()