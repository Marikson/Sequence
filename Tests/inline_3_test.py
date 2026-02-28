import unittest
import tkinter as tk
from sequence import Sequence


class Inline3TestHorizontalMinus(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 3):
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(2, 4):
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(3, 5):
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 0, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 0, "c": 4}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_even_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(2, 5):
            if c % 2 == 0:
                test_game.model.clicked_cell = {"r": 0, "c": c}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_odd_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 4):
            if c % 2 == 1:
                test_game.model.clicked_cell = {"r": 0, "c": c}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(2, 5):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(2, 4):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 1, "c": 5}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for c in range(3, 5):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(2, 4):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 1, "c": 6}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_NOT_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)
        
        test_game.model.clicked_cell = {"r": 1, "c": 2}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for c in range(5, 7):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_chess_pattern_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 6):
            if c % 2 == 1:
                test_game.model.clicked_cell = {"r": 1, "c": c}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

 
class Inline3TestHorizontalPlus(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 6, -1):
            test_game.model.clicked_cell = {"r": 9, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(7,5, -1):
            test_game.model.clicked_cell = {"r": 9, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(6, 4, -1):
            test_game.model.clicked_cell = {"r": 9, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
            test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 9, "c": 8}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 9, "c": 5}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_even_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 5, -1):
            if c % 2 == 0:
                test_game.model.clicked_cell = {"r": 9, "c": c}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_on_odd_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(7, 4, -1):
            if c % 2 == 1:
                test_game.model.clicked_cell = {"r": 9, "c": c}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    
    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(7, 4, -1):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)
    
    def test_1_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(7, 5, -1):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 1, "c": 4}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 7}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for c in range(5, 3, -1):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(7, 5, -1):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 1, "c": 3}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_NOT_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)
        
        test_game.model.clicked_cell = {"r": 1, "c": 7}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for c in range(4, 2, -1):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_chess_pattern_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(7, 2, -1):
            if c % 2 == 1:
                test_game.model.clicked_cell = {"r": 1, "c": c}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


class Inline3TestVerticalMinus(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 3):
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(2, 4):
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(3, 5):
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 0}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 4, "c": 0}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_even_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(2, 5):
            if r % 2 == 0:
                test_game.model.clicked_cell = {"r": r, "c": 0}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_odd_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 4):
            if r % 2 == 1:
                test_game.model.clicked_cell = {"r": r, "c": 0}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 4):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for r in range(3, 5):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 3):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 4, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for r in range(4, 6):
            if r % 2 == 0:
                test_game.model.clicked_cell = {"r": r, "c": 1}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)
    
    def test_2_empty_only_middle_NOT_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)
        
        
        for r in range(1, 3):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 5, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_chess_pattern_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 6):
            if r % 2 == 1:
                test_game.model.clicked_cell = {"r": r, "c": 1}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

 
class Inline3TestVerticalPlus(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(8, 6, -1):
            test_game.model.clicked_cell = {"r": r, "c": 9}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(7, 5, -1):
            test_game.model.clicked_cell = {"r": r, "c": 9}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(6, 4, -1):
            test_game.model.clicked_cell = {"r": r, "c": 9}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
            test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 8, "c": 9}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 5, "c": 9}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_1_empty_one_ended_on_even_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(8, 5, -1):
            if r % 2 == 0:
                test_game.model.clicked_cell = {"r": r, "c": 9}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_on_odd_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(7, 4, -1):
            if r % 2 == 1:
                test_game.model.clicked_cell = {"r": r, "c": 0}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    
    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(7, 4, -1):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)
    
    def test_1_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(7, 5, -1):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 4, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 7, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for r in range(5, 3, -1):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(7, 5, -1):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 3, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_NOT_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)
        
        test_game.model.clicked_cell = {"r": 7, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for r in range(4, 2, -1):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_chess_pattern_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(7, 2, -1):
            if r % 2 == 1:
                test_game.model.clicked_cell = {"r": r, "c": 1}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    
class Inline3TestUpLeft(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 3):
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(2, 4):
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(3, 5):
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 4, "c": 4}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_even_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(2, 5):
            if i % 2 == 0:
                test_game.model.clicked_cell = {"r": i, "c": i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_odd_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 4):
            if i % 2 == 1:
                test_game.model.clicked_cell = {"r": i, "c": i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 4):
            test_game.model.clicked_cell = {"r": i, "c": 2+i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 3):
            test_game.model.clicked_cell = {"r": i, "c": 2+i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 4, "c": 6}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 3}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for i in range(3, 5):
            test_game.model.clicked_cell = {"r": i, "c": 2+i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 3):
            test_game.model.clicked_cell = {"r": i, "c": 2+i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 5, "c": 7}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


    def test_2_empty_only_middle_NOT_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 3}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for i in range(4, 6):
            test_game.model.clicked_cell = {"r": i, "c": 2+i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_chess_pattern_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i % 2 == 1:
                test_game.model.clicked_cell = {"r": i, "c": 2+i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)



class Inline3TestUpRight(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 6, -1):
            test_game.model.clicked_cell = {"r": 9-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(7, 5, -1):
            test_game.model.clicked_cell = {"r": 9-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(6, 4, -1):
            test_game.model.clicked_cell = {"r": 9-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 8}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 4, "c": 5}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_even_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 5, -1):
            if i % 2 == 0:
                test_game.model.clicked_cell = {"r": 9-i, "c": i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_on_odd_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 4, -1):
            if i % 2 == 1:
                test_game.model.clicked_cell = {"r": 9-i, "c": i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 4):
            test_game.model.clicked_cell = {"r": 7-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 3):
            test_game.model.clicked_cell = {"r": i, "c": 7-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 4, "c": 3}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 6}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for i in range(3, 5):
            test_game.model.clicked_cell = {"r": i, "c": 7-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 3):
            test_game.model.clicked_cell = {"r": i, "c": 7-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 5, "c": 2}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


    def test_2_empty_only_middle_NOT_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 1, "c": 6}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for i in range(4, 6):
            test_game.model.clicked_cell = {"r": i, "c": 7-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_chess_pattern_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i % 2 == 1:
                test_game.model.clicked_cell = {"r": i, "c": 7-i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


class Inline3TestDownLeft(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 6, -1):
            test_game.model.clicked_cell = {"r": i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(7, 5, -1):
            test_game.model.clicked_cell = {"r": i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(6, 4, -1):
            test_game.model.clicked_cell = {"r": i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 8, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 5, "c": 4}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_even_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 5, -1):
            if i % 2 == 0:
                test_game.model.clicked_cell = {"r": i, "c": 9-i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_on_odd_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 4, -1):
            if i % 2 == 1:
                test_game.model.clicked_cell = {"r": i, "c": 9-i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 4):
            test_game.model.clicked_cell = {"r": 7-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 3):
            test_game.model.clicked_cell = {"r": 7-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 3, "c": 4}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 6, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for i in range(3, 5):
            test_game.model.clicked_cell = {"r": 7-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 3):
            test_game.model.clicked_cell = {"r": 7-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 2, "c": 5}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


    def test_2_empty_only_middle_NOT_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 6, "c": 1}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for i in range(4, 6):
            test_game.model.clicked_cell = {"r": 7-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_chess_pattern_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i % 2 == 1:
                test_game.model.clicked_cell = {"r": 7-i, "c": i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)
         

class Inline3TestDownRight(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 6, -1):
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(7, 5, -1):
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(6, 4, -1):
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 5, "c": 5}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 8, "c": 8}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_2_empty_only_middle_on_even_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 5, -1):
            if i % 2 == 0:
                test_game.model.clicked_cell = {"r": i, "c": i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_on_odd_fields(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(7, 4, -1):
            if i % 2 == 1:
                test_game.model.clicked_cell = {"r": i, "c": i}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 5, -1):
            test_game.model.clicked_cell = {"r": i, "c": i-1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 6, -1):
            test_game.model.clicked_cell = {"r": i, "c": i-1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 5, "c": 4}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 8, "c": 7}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for i in range(6, 4, -1):
            test_game.model.clicked_cell = {"r": i, "c": i-1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_2_empty_only_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 6, -1):
            test_game.model.clicked_cell = {"r": i, "c": i-1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.clicked_cell = {"r": 4, "c": 3}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)


    def test_2_empty_only_middle_NOT_two_ended_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        test_game.model.clicked_cell = {"r": 8, "c": 7}
        r, c = test_game.pick_cell()
        test_game.model.set_color("Red")
        for i in range(5, 3, -1):
            test_game.model.clicked_cell = {"r": i, "c": i-1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

    def test_chess_pattern_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")

        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(8, 3, -1):
            if i % 2 == 0:
                test_game.model.clicked_cell = {"r": i, "c": i-1}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 3)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 2)

if __name__ == '__main__':
    unittest.main()