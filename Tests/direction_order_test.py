import unittest
import tkinter as tk
from sequence import Sequence

class DirectionOrderTest(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 0, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        