from unittest import result
from misc import Misc
from typing import Iterable, Dict, Any, List

class SequenceModel:

    
    class Cell:
        def __init__(self, row, col, other_cell=None, dx=0, dy=0):
            self.row_index = row
            self.col_index = col
            self.relative_position_to_picked_cell = self.get_relative_position(other_cell, dx, dy) if other_cell else 0

        def get_relative_position(self, other_cell, dx, dy):
            """
            Computes relative position k such that:
            self = picked_cell + k * (dx, dy)

            Returns:
                int k     → valid relative position
                None      → if not on the same directional line
            """
            dr = self.row_index - other_cell.row_index
            dc = self.col_index - other_cell.col_index

            # Invalid direction vector
            if dx == 0 and dy == 0:
                return None

            # Horizontal line
            if dx == 0:
                if dr != 0:
                    return None
                if dc % dy != 0:
                    return None
                return dc // dy

            # Vertical line
            if dy == 0:
                if dc != 0:
                    return None
                if dr % dx != 0:
                    return None
                return dr // dx

            # Diagonal or general direction
            if dr % dx != 0 or dc % dy != 0:
                return None

            k1 = dr // dx
            k2 = dc // dy

            if k1 != k2:
                return None

            return k1


        def are_neighbours(self, other_cell):
            for i in range(self.row_index - 1, self.row_index + 2):
                if i < 0 or i >= Misc.GRID_SIZE:
                    continue
                for j in range(self.col_index - 1, self.col_index + 2):
                    if j < 0 or j >= Misc.GRID_SIZE:
                        continue
                    if i == other_cell.row_index and j == other_cell.col_index:
                        return True
            return False

    def __init__(self):
        self.grid = None
        self.clicked_cell = {"r": None, "c": None}
        
        self.inline_dict = {
            "Green": {
                "inline": 0,
                "two_ended": False,
                "open_in_middle": False,
                "empty_middle_counter": 0,
                "one_ended": False,
                "round_to_come_again": 0,
                "inline_indexes": [],
                "empty_middle_indexes": [],
                "empty_indexes": [],
                "winning_probability": 0
            }
            , 
            "Blue": {
                "inline": 0,
                "two_ended": False,
                "open_in_middle": False,
                "empty_middle_counter": 0,
                "one_ended": False,
                "round_to_come_again": 0,
                "inline_indexes": [],
                "empty_middle_indexes": [],
                "empty_indexes": [],
                "winning_probability": 0
            },
            "Red": {
                "inline": 0,
                "two_ended": False,
                "open_in_middle": False,
                "empty_middle_counter": 0,
                "one_ended": False,
                "round_to_come_again": 0,
                "inline_indexes": [],
                "empty_middle_indexes": [],
                "empty_indexes": [],
                "winning_probability": 0
            }
        }


    def on_cell_click(self, row, col):
        self.clicked_cell["r"] = row
        self.clicked_cell["c"] = col


    def get_btn_color(self, btn):
        return btn.cget("bg")

    
    def check_winner(self):
        for r in range(Misc.GRID_SIZE):
            for c in range(Misc.GRID_SIZE):
                color_code = self.get_btn_color(self.grid[r][c])
                if color_code in ("White"):
                    continue

                # Down
                if c <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN:
                    if all(self.get_btn_color(self.grid[r][c + i]) in [color_code, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color_code
                    
                # Up
                if c >= 4:
                    if all(self.get_btn_color(self.grid[r][c - i]) in [color_code, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color_code

                # Right
                if r <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN:
                    if all(self.get_btn_color(self.grid[r + i][c]) in [color_code, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color_code
                    
                # Left
                if r >= 4:
                    if all(self.get_btn_color(self.grid[r - i][c]) in [color_code, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color_code

                # down-right
                if r <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN and c <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN:
                    if all(self.get_btn_color(self.grid[r + i][c + i]) in [color_code, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color_code

                # up-right
                if r >= 4 and c <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN:
                    if all(self.get_btn_color(self.grid[r - i][c + i]) in [color_code, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color_code
                    
                # down-left
                if r <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN and c >= 4:
                    if all(self.get_btn_color(self.grid[r + i][c - i]) in [color_code, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color_code

                # up-left
                if r >= 4 and c >= 4:
                    if all(self.get_btn_color(self.grid[r - i][c - i]) in [color_code, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color_code    

        return None
    

    def set_color(self, color=None):
        if color:
            r, c = self.clicked_cell["r"], self.clicked_cell["c"]
            self.grid[r][c].config(bg=color)
            self.grid[r][c].config(state="disabled")
        # return r, c, color


    
    
    
    def determine_inline(self, cell,
        inline_minus_cells, inline_plus_cells,
        gap_minus_cells, gap_plus_cells,
        empty_minus_cells, empty_plus_cells):
        # -------------------------------
        # Weight calculation for direction
        # -------------------------------
        def calculate_weights(inline_list, gap_list, empty_list):
            inline_weight = len(inline_list)
            gap_weight = len(gap_list) 
            empty_weight = len(empty_list)

            return inline_weight, gap_weight, empty_weight

        minus_inline_weight, minus_gap_weight, minus_empty_weight = calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_inline_weight, plus_gap_weight, plus_empty_weight = calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)

        # -------------------------------
        # Decide preferred processing order
        # -------------------------------

        if minus_inline_weight > plus_inline_weight:
            direction_order = ["minus", "plus"]
        elif plus_inline_weight > minus_inline_weight:
            direction_order = ["plus", "minus"]
        else:
            if minus_gap_weight < plus_gap_weight:
                direction_order = ["minus", "plus"]
            elif plus_gap_weight < minus_gap_weight:
                direction_order = ["plus", "minus"]
            else:
                if minus_empty_weight < plus_empty_weight:
                    direction_order = ["minus", "plus"]
                elif plus_empty_weight < minus_empty_weight:
                    direction_order = ["plus", "minus"]
                else:
                    direction_order = ["minus", "plus"]
            


        def process_cells(inline_cells, gap_cells, sequence_pattern, sequence_cells):
            sorted_all_cells = sorted(inline_cells + gap_cells, key=lambda c: c.relative_position_to_picked_cell)
            for c in sorted_all_cells:
                if len(sequence_cells) < Misc.INLINE_TO_WIN:
                    if c in inline_cells:
                        sequence_pattern.append("inline")
                        sequence_cells.append(c)
                    elif c in gap_cells:
                        sequence_pattern.append("gap")
                        sequence_cells.append(c)
                    # elif c in empty_cells:
                    #     sequence_pattern.append("empty")
                    #     sequence_cells.append(c)

            return sequence_pattern, sequence_cells
            
        # -------------------------------
        # Process cells from preferred direction first
        # -------------------------------
        sequence_pattern = ["inline"]
        sequence_cells = [cell]
        if direction_order[0] == "minus":
            sequence_pattern, sequence_cells = process_cells(inline_minus_cells, gap_minus_cells, sequence_pattern, sequence_cells)
            sequence_pattern, sequence_cells = process_cells(inline_plus_cells, gap_plus_cells, sequence_pattern, sequence_cells)
        else:
            sequence_pattern, sequence_cells = process_cells(inline_plus_cells, gap_plus_cells, sequence_pattern, sequence_cells)
            sequence_pattern, sequence_cells = process_cells(inline_minus_cells, gap_minus_cells, sequence_pattern, sequence_cells)
        

        inline = 1
        inline_cells = []
        gap_counter = 0
        gap_cells = []
        empty_tails = []
        for i in range(len(sequence_pattern)):
            if sequence_pattern[i] == "inline":
                inline_cells.append(sequence_cells[i])
                inline =+ 1
            elif sequence_pattern[i] == "gap":
                gap_cells.append(sequence_cells[i])
                gap_counter += 1

        
        open_minus = False
        open_plus = False
        if len(sequence_cells) < Misc.INLINE_TO_WIN:
            limit = Misc.INLINE_TO_WIN - len(sequence_cells)
            i = 0
            while (empty_plus_cells or empty_minus_cells) and limit:
                if direction_order[0] == "minus":
                    if i < len(empty_minus_cells):
                        empty_cell = empty_minus_cells[i]
                        open_minus = True
                    elif i < len(empty_plus_cells):
                        empty_cell = empty_plus_cells[i]
                        open_plus = True
                else:
                    if i < len(empty_plus_cells):
                        empty_cell = empty_plus_cells[i]
                        open_plus = True
                    elif i < len(empty_minus_cells):
                        empty_cell = empty_minus_cells[i]
                        open_minus = True
                empty_tails.append(empty_cell)
                limit -= 1
                i += 1
        
        one_ended = open_minus or open_plus
        two_ended = open_minus and open_plus
        open_in_middle = gap_counter > 0
                



        return {
            "inline": inline,
            "open_in_middle": open_in_middle,
            "empty_middle_counter": gap_counter,
            "one_ended": one_ended,
            "two_ended": two_ended,
            "inline_cells": inline_cells,
            "empty_cells": empty_tails,
            "empty_middle_cells": gap_cells
        }






    def get_empty_indexes(self, indexes_tracked, empty_minus_indexes, empty_plus_indexes):
        i = 0
        empty_indexes = []
        while indexes_tracked <= Misc.INLINE_TO_WIN:
            if i < len(empty_minus_indexes):
                empty_indexes.append(empty_minus_indexes[i])
                indexes_tracked += 1
            if i < len(empty_plus_indexes):
                empty_indexes.append(empty_plus_indexes[i])
                indexes_tracked += 1
            i += 1
        return empty_indexes


    def set_inline_dict(self, color, cell: Cell,
                            opened_minus, opened_plus,
                            inline_minus_cells, inline_plus_cells,
                            gap_minus_cells, gap_plus_cells,
                            empty_minus_cells, empty_plus_cells):
        
        
        if len(inline_minus_cells) + len(inline_plus_cells) + 1 == 1:
            return          
        merged_cells = [cell] + inline_minus_cells + inline_plus_cells + gap_minus_cells + gap_plus_cells
        sorted_cells = sorted(merged_cells, key=lambda c: (c.relative_position_to_picked_cell))
        evaluated = self.determine_inline(cell,inline_minus_cells, inline_plus_cells,
                                          list(reversed(gap_minus_cells)), list(reversed(gap_plus_cells)),
                                          empty_minus_cells, empty_plus_cells)

        
        self.update_inline_dict(color, evaluated)

        calculated_probability = self.calculate_win_probability(color)
        self.print_inline_dict(color)


    def update_inline_dict(self, color, evaluated):
        to_update = False
        if evaluated["inline"] > self.inline_dict[color]["inline"]:
            to_update = True
        elif evaluated["inline"] == self.inline_dict[color]["inline"]:
            if evaluated["two_ended"] and not self.inline_dict[color]["two_ended"]:
                to_update = True
            elif evaluated["empty_middle_counter"] < self.inline_dict[color]["empty_middle_counter"]:
                to_update = True


        if to_update:
            self.inline_dict[color]["inline"] = evaluated["inline"]
            self.inline_dict[color]["open_in_middle"] = evaluated["open_in_middle"]
            self.inline_dict[color]["empty_middle_counter"] = evaluated["empty_middle_counter"]
            self.inline_dict[color]["one_ended"] = evaluated["one_ended"]
            self.inline_dict[color]["two_ended"] = evaluated["two_ended"]
            self.inline_dict[color]["inline_cells"] = evaluated["inline_cells"]
            self.inline_dict[color]["empty_cells"] = evaluated["empty_cells"]
            self.inline_dict[color]["empty_middle_cells"] = evaluated["empty_middle_cells"]

        # self.inline_dict[color]["round_to_come_again"] = len(Misc.turn) - 1




    def calculate_win_probability(self, color_who_picked):
        pass

        # if self.inline_dict[color_who_picked]["two_ended"] and self.inline_dict[color_who_picked]["inline"] == 4:
        #     probability_multiplyer = 2
        # else:
        #     probability_multiplyer = 1
        # color_who_picked_missing_cells_to_win = Misc.INLINE_TO_WIN - self.inline_dict[color_who_picked]["inline"]
        # probability_other_color_willing_to_block = color_who_picked_missing_cells_to_win * Misc.WILLING_TO_BLOCK_PROBABILITY * probability_multiplyer


        # color_who_picked_probability = (1 - color_who_picked_missing_cells_to_win * Misc.PROBABILITY_TO_COLOR_FIELD) * probability_multiplyer  \
        #                                 * probability_other_color_willing_to_block * self.inline_dict[color_who_picked]["round_to_come_again"]
        
        # return color_who_picked_probability
        


    def check_inline_per_color(self, color, picked_cell: Cell):
        # Horizontal
        inline_minus_cells = []
        inline_plus_cells = []
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_minus_cells = []
        empty_plus_cells = []
        gap_minus_cells = []
        gap_plus_cells = []
        opened_minus = False
        opened_plus = False
        potentially_gap_minus = False
        potentially_gap_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # Left
            if picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_cell = self.Cell(picked_cell.row_index, picked_cell.col_index - i, picked_cell, 0, -1)
                        inline_minus_cells.append(inline_cell)
                        if potentially_gap_minus:
                            for j in range(1, empty_minus_counter + 1):
                                gap_cell = self.Cell(picked_cell.row_index, picked_cell.col_index - i + j, picked_cell, 0, -1)
                                gap_minus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == picked_cell.row_index and cell.col_index == picked_cell.col_index - i + j)]
                            potentially_gap_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_gap_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_cell = self.Cell(picked_cell.row_index, picked_cell.col_index - i, picked_cell, 0, -1)
                        empty_minus_cells.append(empty_cell)

                else:
                    other_color_inline_minus = True
                    potentially_gap_minus = False
                    opened_minus = False
 
            # Right
            if picked_cell.col_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_cell = self.Cell(picked_cell.row_index, picked_cell.col_index + i, picked_cell, 0, 1)
                        inline_plus_cells.append(inline_cell)
                        if potentially_gap_plus:
                            for j in range(1, empty_plus_counter + 1):
                                gap_cell = self.Cell(picked_cell.row_index, picked_cell.col_index + i - j, picked_cell, 0, 1)
                                gap_plus_cells.append(gap_cell)
                                empty_plus_cells = [cell for cell in empty_plus_cells if not (cell.row_index == picked_cell.row_index and cell.col_index == picked_cell.col_index + i - j)]
                            potentially_gap_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_gap_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_cell = self.Cell(picked_cell.row_index, picked_cell.col_index + i, picked_cell, 0, 1)
                        empty_plus_cells.append(empty_cell)

                else:
                    other_color_inline_plus = True
                    potentially_gap_plus = False
                    opened_plus = False
                    

        self.set_inline_dict(color, picked_cell,
                            opened_minus, opened_plus,
                            inline_minus_cells, inline_plus_cells,
                            gap_minus_cells, gap_plus_cells,
                            empty_minus_cells, empty_plus_cells)

        
        # Vertical
        inline_minus_cells = []
        inline_plus_cells = []
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_minus_cells = []
        empty_plus_cells = []
        gap_minus_cells = []
        gap_plus_cells = []
        opened_minus = False
        opened_plus = False
        potentially_gap_minus = False
        potentially_gap_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # Up
            if picked_cell.row_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_cell = self.Cell(picked_cell.row_index - i, picked_cell.col_index, picked_cell, -1, 0)
                        inline_minus_cells.append(inline_cell)
                        if potentially_gap_minus:
                            for j in range(1, empty_minus_counter + 1):
                                gap_cell = self.Cell(picked_cell.row_index - i + j, picked_cell.col_index, picked_cell, -1, 0)
                                gap_minus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == picked_cell.row_index - i + j and cell.col_index == picked_cell.col_index)]
                            potentially_gap_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index]) == "White":
                    if not other_color_inline_minus:
                        potentially_gap_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_cell = self.Cell(picked_cell.row_index - i, picked_cell.col_index, picked_cell, -1, 0)
                        empty_minus_cells.append(empty_cell)

                else:
                    other_color_inline_minus = True
                    potentially_gap_minus = False
                    opened_minus = False

            # Down
            if picked_cell.row_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_cell = self.Cell(picked_cell.row_index + i, picked_cell.col_index, picked_cell, 1, 0)
                        inline_plus_cells.append(inline_cell)
                        if potentially_gap_plus:
                            for j in range(1, empty_plus_counter + 1):
                                gap_cell = self.Cell(picked_cell.row_index + i - j, picked_cell.col_index, picked_cell, 1, 0)
                                gap_plus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == picked_cell.row_index + i - j and cell.col_index == picked_cell.col_index)]
                            potentially_gap_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index]) == "White":
                    if not other_color_inline_plus:
                        potentially_gap_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_cell = self.Cell(picked_cell.row_index + i, picked_cell.col_index, picked_cell, 1, 0)
                        empty_plus_cells.append(empty_cell)

                else:
                    other_color_inline_plus = True
                    potentially_gap_plus = False
                    opened_plus = False

        self.set_inline_dict(color, picked_cell,
                            opened_minus, opened_plus,
                            inline_minus_cells, inline_plus_cells,
                            gap_minus_cells, gap_plus_cells,
                            empty_minus_cells, empty_plus_cells)

        

        # Diagonal [0,0] to [9,9]
        inline_minus_cells = []
        inline_plus_cells = []
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_minus_cells = []
        empty_plus_cells = []
        gap_minus_cells = []
        gap_plus_cells = []
        opened_minus = False
        opened_plus = False
        potentially_gap_minus = False
        potentially_gap_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # up-left
            if picked_cell.row_index - i >= 0 and picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_cell = self.Cell(picked_cell.row_index - i, picked_cell.col_index - i, picked_cell, -1, -1)
                        inline_minus_cells.append(inline_cell)
                        if potentially_gap_minus:
                            for j in range(1, empty_minus_counter + 1):
                                gap_cell = self.Cell(picked_cell.row_index - i + j, picked_cell.col_index - i + j, picked_cell, -1, -1)
                                gap_minus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == picked_cell.row_index - i + j and cell.col_index == picked_cell.col_index - i + j)]
                            potentially_gap_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_gap_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_cell = self.Cell(picked_cell.row_index - i, picked_cell.col_index - i, picked_cell, -1, -1)
                        empty_minus_cells.append(empty_cell)
                else:
                    other_color_inline_minus = True
                    potentially_gap_minus = False
                    opened_minus = False
            
            # down-right
            if picked_cell.row_index + i < Misc.GRID_SIZE and picked_cell.col_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_cell = self.Cell(picked_cell.row_index + i, picked_cell.col_index + i, picked_cell, 1, 1)
                        inline_plus_cells.append(inline_cell)
                        if potentially_gap_plus:
                            for j in range(1, empty_plus_counter + 1):
                                gap_cell = self.Cell(picked_cell.row_index + i - j, picked_cell.col_index + i - j, picked_cell, 1, 1)
                                gap_plus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == picked_cell.row_index + i - j and cell.col_index == picked_cell.col_index + i - j)]
                            potentially_gap_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_gap_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_cell = self.Cell(picked_cell.row_index + i, picked_cell.col_index + i, picked_cell, 1, 1)
                        empty_plus_cells.append(empty_cell)
                else:
                    other_color_inline_plus = True
                    potentially_gap_plus = False
                    opened_plus = False

        self.set_inline_dict(color, picked_cell,
                            opened_minus, opened_plus,
                            inline_minus_cells, inline_plus_cells,
                            gap_minus_cells, gap_plus_cells,
                            empty_minus_cells, empty_plus_cells)

        

        # Diagonal [0,9] to [9,0]
        inline_minus_cells = []
        inline_plus_cells = []
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_minus_cells = []
        empty_plus_cells = []
        gap_minus_cells = []
        gap_plus_cells = []
        opened_minus = False
        opened_plus = False
        potentially_gap_minus = False
        potentially_gap_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # up-right
            if picked_cell.row_index + i < Misc.GRID_SIZE and picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_cell = self.Cell(picked_cell.row_index + i, picked_cell.col_index - i, picked_cell, 1, -1)
                        inline_minus_cells.append(inline_cell)
                        if potentially_gap_minus:
                            for j in range(1, empty_minus_counter + 1):
                                gap_cell = self.Cell(picked_cell.row_index + i - j, picked_cell.col_index - i + j, picked_cell, 1, -1)
                                gap_minus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == picked_cell.row_index + i - j and cell.col_index == picked_cell.col_index - i + j)]
                            potentially_gap_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_gap_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_cell = self.Cell(picked_cell.row_index + i, picked_cell.col_index - i, picked_cell, 1, -1)
                        empty_minus_cells.append(empty_cell)
                else:
                    other_color_inline_minus = True
                    potentially_gap_minus = False
                    opened_minus = False
            
            # down-left
            if picked_cell.row_index - i >= 0 and picked_cell.col_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_cell = self.Cell(picked_cell.row_index - i, picked_cell.col_index + i, picked_cell, -1, 1)
                        inline_plus_cells.append(inline_cell)
                        if potentially_gap_plus:
                            for j in range(1, empty_plus_counter + 1):
                                gap_cell = self.Cell(picked_cell.row_index - i + j, picked_cell.col_index + i - j, picked_cell, -1, 1)
                                gap_plus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == picked_cell.row_index - i + j and cell.col_index == picked_cell.col_index + i - j)]
                            potentially_gap_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_gap_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_cell = self.Cell(picked_cell.row_index - i, picked_cell.col_index + i, picked_cell, -1, 1)
                        empty_plus_cells.append(empty_cell)
                else:
                    other_color_inline_plus = True
                    potentially_gap_plus = False
                    opened_plus = False

        self.set_inline_dict(color, picked_cell,
                            opened_minus, opened_plus,
                            inline_minus_cells, inline_plus_cells,
                            gap_minus_cells, gap_plus_cells,
                            empty_minus_cells, empty_plus_cells)

        


    def print_inline_dict(self, color):
        print(f"  Inline: {self.inline_dict[color]['inline']} " \
              f"\n  Open in middle: {self.inline_dict[color]['open_in_middle']} " \
              f"\n  Empty middle counter: {self.inline_dict[color]['empty_middle_counter']} " \
              f"\n  One ended: {self.inline_dict[color]['one_ended']} " \
              f"\n  Two ended: {self.inline_dict[color]['two_ended']} " \
            #   f"\n  Inline cells: {self.inline_dict[color]['inline_cells']} " \
            #   f"\n  Empty middle cells: {self.inline_dict[color]['empty_middle_cells']} " \
            #   f"\n  Empty cells: {self.inline_dict[color]['empty_cells']} "
                
              f"\n  Inline cells: {[f'[{cell.row_index}][{cell.col_index}]' for cell in self.inline_dict[color]['inline_cells']]} "
              f"\n  Empty middle cells: {[f'[{cell.row_index}][{cell.col_index}]' for cell in self.inline_dict[color]['empty_middle_cells']]} "
              f"\n  Empty cells: {[f'[{cell.row_index}][{cell.col_index}]' for cell in self.inline_dict[color]['empty_cells']]} "
              )
     