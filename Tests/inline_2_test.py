import unittest
import tkinter as tk
from sequence import Sequence


class Inline2Test(unittest.TestCase):
    def test_2_inline_minus_horizontal_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 0, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 2)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    
    def test_2_inline_minus_horizontal_1_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 0, "c": 2}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 2)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_2_inline_minus_horizontal_2_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 0, "c": 3}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 2)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    
    def test_2_inline_minus_horizontal_3_empty_NOT_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 0, "c": 4}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 2)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 3)


    def test_2_inline_minus_horizontal_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 2}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 1, "c": 3}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 2)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_2_inline_minus_horizontal_1_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 2}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 1, "c": 4}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 2)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    
    def test_2_inline_minus_horizontal_2_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 2}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 1, "c": 5}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 2)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


    def test_2_inline_minus_horizontal_3_empty_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
    
        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 2}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 1, "c": 6}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 2)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 3)

if __name__ == '__main__':
    unittest.main()