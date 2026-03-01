import unittest
import tkinter as tk
from sequence import Sequence

class Inline4TestHorizontalMinus(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 4):
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 5):
            if c == 1:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 5):
            if c == 3:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 5):
            if c == 2:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 5):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 6):
            if c == 2:
                continue
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 6):
            if c == 4:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(1, 6):
            if c == 3:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


class Inline4TestHorizontalPlus(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 5, -1):
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 4, -1):
            if c == 8:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 4, -1):
            if c == 6:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 4, -1):
            if c == 7:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 4, -1):
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 3, -1):
            if c == 7:
                continue
            test_game.model.clicked_cell = {"r": 1, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 3, -1):
            if c == 5:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for c in range(8, 3, -1):
            if c == 6:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": c}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)    


class Inline4TestVerticalMinus(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 4):
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 5):
            if r == 1:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 5):
            if r == 3:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 5):
            if r == 2:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 5):
            test_game.model.clicked_cell = {"r": 1, "c": r}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 6):
            if r == 1:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_mirrored_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 5):
            if r == 3:
                continue
            test_game.model.clicked_cell = {"r": 0, "c": r}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(1, 5):
            if r == 2:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


class Inline4TestVerticalPlus(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(8, 5, -1):
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(8, 4, -1):
            if r == 8:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(8, 4, -1):
            if r == 6:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(8, 4, -1):
            if r == 7:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 0}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(8, 4, -1):
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(8, 3, -1):
            if r == 8:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_mirrored_NOT_two_ended(self):    
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for r in range(8, 3, -1):
            if r == 6:
                continue
            test_game.model.clicked_cell = {"r": r, "c": 1}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle_NOT_two_ended(self):
            test_field = tk.Tk()
            test_field.title("Test Field")
            
            test_game = Sequence()
            test_game.create_grid(test_field)

            for r in range(8, 3, -1):
                if r == 7:
                    continue
                test_game.model.clicked_cell = {"r": r, "c": 1}
                r, c = test_game.pick_cell()
                test_game.model.set_color("Red")
            test_game.model.check_inline_per_color("Red", r, c)
            self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
            self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
            self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
            self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
            self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)
    

class Inline4TestDiagonalUpLeft(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 4):
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 1:
                continue
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 3:
                continue
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 2:
                continue
            test_game.model.clicked_cell = {"r": i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            test_game.model.clicked_cell = {"r": 2+i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 2:
                continue
            test_game.model.clicked_cell = {"r": 2+i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 4:
                continue
            test_game.model.clicked_cell = {"r": 2+i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 3:
                continue
            test_game.model.clicked_cell = {"r": 2+i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


class Inline4TestDiagonalUpRight(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 4):
            test_game.model.clicked_cell = {"r": i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 1:
                continue
            test_game.model.clicked_cell = {"r": i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 3:
                continue
            test_game.model.clicked_cell = {"r": i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 2:
                continue
            test_game.model.clicked_cell = {"r": i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            test_game.model.clicked_cell = {"r": 2+i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 2:
                continue
            test_game.model.clicked_cell = {"r": 2+i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 4:
                continue
            test_game.model.clicked_cell = {"r": 2+i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 3:
                continue
            test_game.model.clicked_cell = {"r": 2+i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    
class Inline4TestDiagonalDownLeft(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 4):
            test_game.model.clicked_cell = {"r": 9-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 1:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 3:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 2:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            test_game.model.clicked_cell = {"r": 9-i, "c": 2+i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 2:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": 2+i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 4:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": 2+i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 3:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": 2+i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


class Inline4TestDiagonalDownRight(unittest.TestCase):
    def test_0_empty_one_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            test_game.model.clicked_cell = {"r": 9-i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 1:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored(self):  
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 3:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            if i == 2:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": 9-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)


    def test_0_empty_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 5):
            test_game.model.clicked_cell = {"r": 9-i, "c": 8-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 0)

    def test_1_empty_in_middle_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 2:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": 8-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_middle_mirrored_NOT_two_ended(self):
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 4:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": 8-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)

    def test_1_empty_in_exact_middle_NOT_two_ended(self):        
        test_field = tk.Tk()
        test_field.title("Test Field")
        
        test_game = Sequence()
        test_game.create_grid(test_field)

        for i in range(1, 6):
            if i == 3:
                continue
            test_game.model.clicked_cell = {"r": 9-i, "c": 8-i}
            r, c = test_game.pick_cell()
            test_game.model.set_color("Red")
        test_game.model.check_inline_per_color("Red", r, c)
        self.assertEqual(test_game.model.inline_dict["Red"]["inline"], 4)
        self.assertEqual(test_game.model.inline_dict["Red"]["two_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["one_ended"], False)
        self.assertEqual(test_game.model.inline_dict["Red"]["open_in_middle"], True)
        self.assertEqual(test_game.model.inline_dict["Red"]["empty_middle_counter"], 1)



if __name__ == '__main__':
    unittest.main()