from unittest import result
from misc import Misc
from typing import Iterable, Dict, Any, List
from math import gcd

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
                int k     → valid relative position (negative on the opposite side of the canonical direction)
                None      → if not on the same directional line
            """
            dr = self.row_index - other_cell.row_index
            dc = self.col_index - other_cell.col_index

            # Invalid direction vector
            if dx == 0 and dy == 0:
                return None

            # --- Horizontal line (canonical: to the right is positive) ---
            if dx == 0:
                if dr != 0:
                    return None
                # Must be an integer multiple of the step size (abs(dy))
                step = abs(dy)
                if step == 0:
                    return None
                if dc % step != 0:
                    return None
                # Use canonical step to the right: k is columns moved
                return dc // step

            # --- Vertical line (canonical: downward is positive) ---
            if dy == 0:
                if dc != 0:
                    return None
                step = abs(dx)
                if step == 0:
                    return None
                if dr % step != 0:
                    return None
                # Use canonical step downward: k is rows moved
                return dr // step

            # --- General direction ---
            # Check collinearity with (dx, dy)
            if dr * dy != dc * dx:
                return None

            # Normalize direction to its minimal integer step (sx, sy)
            g = gcd(abs(dx), abs(dy))
            sx, sy = dx // g, dy // g

            # Canonical orientation: make the first non-zero component positive
            # (so sign of k reflects geometric side relative to this canonical direction)
            if sx < 0 or (sx == 0 and sy < 0):
                sx, sy = -sx, -sy

            # Now k must satisfy dr = k*sx and dc = k*sy
            if sx != 0:
                if dr % sx != 0:
                    return None
                k = dr // sx
            else:
                if sy == 0 or dc % sy != 0:
                    return None
                k = dc // sy

            return k


    def __init__(self):
        self.grid = None
        self.picked_cell = None
        
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
        if row < 0 or row >= Misc.GRID_SIZE or col < 0 or col >= Misc.GRID_SIZE:
            return
        self.picked_cell = self.Cell(row, col)


    def get_btn_color(self, btn):
        return btn.cget("bg")

    
    def check_winner(self):
        for r in range(Misc.GRID_SIZE):
            for c in range(Misc.GRID_SIZE):
                color = self.get_btn_color(self.grid[r][c])
                if color in ("White"):
                    continue

                # Right
                if c <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN:
                    if all(self.get_btn_color(self.grid[r][c + i]) in [color, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color
                    
                # Left
                if c >= 4:
                    if all(self.get_btn_color(self.grid[r][c - i]) in [color, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color

                # Down
                if r <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN:
                    if all(self.get_btn_color(self.grid[r + i][c]) in [color, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color
                    
                # Up
                if r >= 4:
                    if all(self.get_btn_color(self.grid[r - i][c]) in [color, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color

                # down-right
                if r <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN and c <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN:
                    if all(self.get_btn_color(self.grid[r + i][c + i]) in [color, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color

                # up-right
                if r >= 4 and c <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN:
                    if all(self.get_btn_color(self.grid[r - i][c + i]) in [color, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color
                    
                # down-left
                if r <= Misc.GRID_SIZE - Misc.INLINE_TO_WIN and c >= 4:
                    if all(self.get_btn_color(self.grid[r + i][c - i]) in [color, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color

                # up-left
                if r >= 4 and c >= 4:
                    if all(self.get_btn_color(self.grid[r - i][c - i]) in [color, "Black"] for i in range(Misc.INLINE_TO_WIN)):
                        return color    

        return False
    

    def set_color(self, color=None):
        if color:
            self.grid[self.picked_cell.row_index][self.picked_cell.col_index].config(bg=color)
            self.grid[self.picked_cell.row_index][self.picked_cell.col_index].config(state="disabled")

    
    def calculate_weights(self, inline_list, gap_list, empty_list):
            inline_count = len(inline_list)
            inline_rel_pos_prduct = 1
            for cell in inline_list:
                inline_rel_pos_prduct *= cell.relative_position_to_picked_cell
            inline_weight = int(abs(inline_rel_pos_prduct) / len(inline_list)) if inline_list else 100
            gap_rel_pos_prduct = 1
            for cell in gap_list:
                gap_rel_pos_prduct *= cell.relative_position_to_picked_cell
            gap_weight = int(abs(gap_rel_pos_prduct) / len(gap_list)) if gap_list else 100
            empty_weight = len(empty_list)
            
            return inline_count, inline_weight, gap_weight, empty_weight
    
    
    def determine_inline(self, cell,
        inline_minus_cells, inline_plus_cells,
        gap_minus_cells, gap_plus_cells,
        empty_minus_cells, empty_plus_cells):
        # --------------------------------
        # Helper methods
        # --------------------------------
        def get_direction_order(minus_count, plus_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight):
            if minus_count > plus_count:
                return ["minus", "plus"]
            elif plus_count > minus_count:
                return ["plus", "minus"]
            else:
                if minus_inline_weight < plus_inline_weight:
                    return ["minus", "plus"]
                elif plus_inline_weight < minus_inline_weight:
                    return ["plus", "minus"]
                else:
                    if minus_gap_weight < plus_gap_weight:
                        return ["minus", "plus"]
                    elif plus_gap_weight < minus_gap_weight:
                        return ["plus", "minus"]
                    else:
                        if minus_empty_weight > plus_empty_weight:
                            return ["minus", "plus"]
                        elif plus_empty_weight > minus_empty_weight:
                            return ["plus", "minus"]
                        else:
                            return ["minus", "plus"]
        
        
        def extend_sequence(inline_cells, gap_cells, sequence_pattern, sequence_cells, sequence_starting_side):
            sorted_extension_cells = sorted(inline_cells + gap_cells, key=lambda c: abs(c.relative_position_to_picked_cell), reverse=True)
            sorted_inline_cells = sorted(inline_cells, key=lambda c: abs(c.relative_position_to_picked_cell))            
            closet_inline_cell = sorted_inline_cells[0] if sorted_inline_cells else None
            closest_inline_cell_rel_pos = abs(closet_inline_cell.relative_position_to_picked_cell) if closet_inline_cell else -5
            
            
            sorted_sequence_cells = sorted(sequence_cells, key=lambda c: abs(c.relative_position_to_picked_cell))
            sequence_starting_cell = sorted_sequence_cells[-1] if sorted_sequence_cells else None
            sequence_starting_cell_rel_pos = sequence_starting_cell.relative_position_to_picked_cell if sequence_starting_cell else None
            extension_limit = abs(closest_inline_cell_rel_pos) - abs(sequence_starting_cell_rel_pos) if sequence_starting_cell_rel_pos is not None else 0
            
            empty_cells = []
            sorted_extension_cells_limited = sorted_extension_cells[-extension_limit:] if extension_limit > 0 else sorted_extension_cells
                
            
            was_inline = False
            for c in sorted_extension_cells_limited:
                if len(sequence_cells) < Misc.INLINE_TO_WIN:
                    if abs(c.relative_position_to_picked_cell) <= extension_limit:
                        if c in inline_cells:
                            sequence_pattern.append("inline")
                            sequence_cells.append(c)
                            was_inline = True
                        elif c in gap_cells and was_inline:
                            sequence_pattern.append("gap")
                            sequence_cells.append(c)
                        else:
                            empty_cells.append(c)         
            
            return sequence_pattern, sequence_cells, empty_cells
        
        
        def process_cells(inline_cells, gap_cells, sequence_pattern, sequence_cells):
            sorted_all_cells = sorted(inline_cells + gap_cells, key=lambda c: abs(c.relative_position_to_picked_cell))
            
            for c in sorted_all_cells:
                if len(sequence_cells) < Misc.INLINE_TO_WIN:
                    if c in inline_cells:
                        sequence_pattern.append("inline")
                        sequence_cells.append(c)
                    elif c in gap_cells:
                        sequence_pattern.append("gap")
                        sequence_cells.append(c)

            return sequence_pattern, sequence_cells
        
        # -------------------------------
        # Weight calculation and direction determination
        # -------------------------------
        
        minus_count, minus_inline_weight, minus_gap_weight, minus_empty_weight = self.calculate_weights(inline_minus_cells, gap_minus_cells, empty_minus_cells)
        plus_count, plus_inline_weight, plus_gap_weight, plus_empty_weight = self.calculate_weights(inline_plus_cells, gap_plus_cells, empty_plus_cells)
        
        direction_order = get_direction_order(minus_count, plus_count, minus_inline_weight, plus_inline_weight, minus_gap_weight, plus_gap_weight, minus_empty_weight, plus_empty_weight)
        
        
        # -------------------------------
        # Process cells from preferred direction first
        # -------------------------------
        sequence_pattern = ["inline"]
        sequence_cells = [cell]
        gaps_to_empty_cells = []
        
        if direction_order[0] == "minus":
            sequence_pattern, sequence_cells = process_cells(inline_minus_cells, gap_minus_cells, sequence_pattern, sequence_cells)
            sequence_pattern, sequence_cells, gaps_to_empty_cells = extend_sequence(inline_plus_cells, gap_plus_cells, sequence_pattern, sequence_cells, "minus")
            if gaps_to_empty_cells:
                empty_plus_cells = gaps_to_empty_cells
        else:
            sequence_pattern, sequence_cells = process_cells(inline_plus_cells, gap_plus_cells, sequence_pattern, sequence_cells)
            sequence_pattern, sequence_cells, gaps_to_empty_cells = extend_sequence(inline_minus_cells, gap_minus_cells, sequence_pattern, sequence_cells, "plus")
            if gaps_to_empty_cells:
                empty_minus_cells = gaps_to_empty_cells


        # -------------------------------
        # Evaluate sequence and return results
        # -------------------------------
        inline = 0
        inline_cells = []
        gap_counter = 0
        gap_cells = []
        
        for i in range(len(sequence_pattern)):
            if sequence_pattern[i] == "inline":
                inline_cells.append(sequence_cells[i])
                inline += 1
            elif sequence_pattern[i] == "gap":
                gap_cells.append(sequence_cells[i])
                gap_counter += 1

        empty_tails = []
        open_minus = False
        open_plus = False
        if len(sequence_cells) < Misc.INLINE_TO_WIN:
            limit = Misc.INLINE_TO_WIN - len(sequence_cells)
            for i in range(0, limit):
                if i < len(empty_minus_cells):
                    empty_tails.append(empty_minus_cells[i])
                    open_minus = True
                if i < len(empty_plus_cells):
                    empty_tails.append(empty_plus_cells[i])
                    open_plus = True
                
        
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



    def set_inline_dict(self, color, cell: Cell,
                            opened_minus, opened_plus,
                            inline_minus_cells, inline_plus_cells,
                            gap_minus_cells, gap_plus_cells,
                            empty_minus_cells, empty_plus_cells):
        
        
        if len(inline_minus_cells) == 0 and len(inline_plus_cells) == 0:
            return          

        evaluated = self.determine_inline(cell,inline_minus_cells, inline_plus_cells,
                                          list(reversed(gap_minus_cells)), list(reversed(gap_plus_cells)),
                                          empty_minus_cells, empty_plus_cells)

        
        self.update_inline_dict(color, evaluated)

        calculated_probability = self.calculate_win_probability(color)
        


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
            
            self.print_inline_dict(color)

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
        

    def check_inline_per_color(self, color):
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
        gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
                = self.check_inline_per_color_horizontal(color)
        self.set_inline_dict(color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells)
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
        gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
                = self.check_inline_per_color_vertical(color)
        self.set_inline_dict(color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells)
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
        gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
                = self.check_inline_per_color_diagonal(color)
        self.set_inline_dict(color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells)
        
        color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, \
        gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells \
                = self.check_inline_per_color_inverted_diagonal(color)
        self.set_inline_dict(color, picked_cell, opened_minus, opened_plus, inline_minus_cells, inline_plus_cells, gap_minus_cells, gap_plus_cells, empty_minus_cells, empty_plus_cells)
    
    

    def check_inline_per_color_horizontal(self, color):
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
            if self.picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[self.picked_cell.row_index][self.picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_cell = self.Cell(self.picked_cell.row_index, self.picked_cell.col_index - i, self.picked_cell, 0, -1)
                        inline_minus_cells.append(inline_cell)
                        if potentially_gap_minus:
                            for j in range(1, empty_minus_counter + 1):
                                gap_cell = self.Cell(self.picked_cell.row_index, self.picked_cell.col_index - i + j, self.picked_cell, 0, -1)
                                gap_minus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == self.picked_cell.row_index and cell.col_index == self.picked_cell.col_index - i + j)]
                            potentially_gap_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[self.picked_cell.row_index][self.picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_gap_minus = True
                        if (i==4 or self.picked_cell.col_index - i == 0) and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_cell = self.Cell(self.picked_cell.row_index, self.picked_cell.col_index - i, self.picked_cell, 0, -1)
                        empty_minus_cells.append(empty_cell)

                else:
                    other_color_inline_minus = True
                    potentially_gap_minus = False
                    opened_minus = False
 
            # Right
            if self.picked_cell.col_index + i <= Misc.GRID_MAX_INDEX:
                if self.get_btn_color(self.grid[self.picked_cell.row_index][self.picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_cell = self.Cell(self.picked_cell.row_index, self.picked_cell.col_index + i, self.picked_cell, 0, 1)
                        inline_plus_cells.append(inline_cell)
                        if potentially_gap_plus:
                            for j in range(1, empty_plus_counter + 1):
                                gap_cell = self.Cell(self.picked_cell.row_index, self.picked_cell.col_index + i - j, self.picked_cell, 0, 1)
                                gap_plus_cells.append(gap_cell)
                                empty_plus_cells = [cell for cell in empty_plus_cells if not (cell.row_index == self.picked_cell.row_index and cell.col_index == self.picked_cell.col_index + i - j)]
                            potentially_gap_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[self.picked_cell.row_index][self.picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_gap_plus = True
                        if (i==4 or self.picked_cell.col_index + i == Misc.GRID_MAX_INDEX) and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_cell = self.Cell(self.picked_cell.row_index, self.picked_cell.col_index + i, self.picked_cell, 0, 1)
                        empty_plus_cells.append(empty_cell)

                else:
                    other_color_inline_plus = True
                    potentially_gap_plus = False
                    opened_plus = False
                    
        return color, self.picked_cell,\
                opened_minus, opened_plus, \
                inline_minus_cells, inline_plus_cells, \
                gap_minus_cells, gap_plus_cells, \
                empty_minus_cells, empty_plus_cells
    

    def check_inline_per_color_vertical(self, color):
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
            if self.picked_cell.row_index - i >= 0:
                if self.get_btn_color(self.grid[self.picked_cell.row_index - i][self.picked_cell.col_index]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_cell = self.Cell(self.picked_cell.row_index - i, self.picked_cell.col_index, self.picked_cell, -1, 0)
                        inline_minus_cells.append(inline_cell)
                        if potentially_gap_minus:
                            for j in range(1, empty_minus_counter + 1):
                                gap_cell = self.Cell(self.picked_cell.row_index - i + j, self.picked_cell.col_index, self.picked_cell, -1, 0)
                                gap_minus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == self.picked_cell.row_index - i + j and cell.col_index == self.picked_cell.col_index)]
                            potentially_gap_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[self.picked_cell.row_index - i][self.picked_cell.col_index]) == "White":
                    if not other_color_inline_minus:
                        potentially_gap_minus = True
                        if (i==4 or self.picked_cell.row_index - i == 0) and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_cell = self.Cell(self.picked_cell.row_index - i, self.picked_cell.col_index, self.picked_cell, -1, 0)
                        empty_minus_cells.append(empty_cell)

                else:
                    other_color_inline_minus = True
                    potentially_gap_minus = False
                    opened_minus = False

            # Down
            if self.picked_cell.row_index + i <= Misc.GRID_MAX_INDEX:
                if self.get_btn_color(self.grid[self.picked_cell.row_index + i][self.picked_cell.col_index]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_cell = self.Cell(self.picked_cell.row_index + i, self.picked_cell.col_index, self.picked_cell, 1, 0)
                        inline_plus_cells.append(inline_cell)
                        if potentially_gap_plus:
                            for j in range(1, empty_plus_counter + 1):
                                gap_cell = self.Cell(self.picked_cell.row_index + i - j, self.picked_cell.col_index, self.picked_cell, 1, 0)
                                gap_plus_cells.append(gap_cell)
                                empty_plus_cells = [cell for cell in empty_plus_cells if not (cell.row_index == self.picked_cell.row_index + i - j and cell.col_index == self.picked_cell.col_index)]
                            potentially_gap_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[self.picked_cell.row_index + i][self.picked_cell.col_index]) == "White":
                    if not other_color_inline_plus:
                        potentially_gap_plus = True
                        if (i==4 or self.picked_cell.row_index + i == Misc.GRID_MAX_INDEX) and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_cell = self.Cell(self.picked_cell.row_index + i, self.picked_cell.col_index, self.picked_cell, 1, 0)
                        empty_plus_cells.append(empty_cell)

                else:
                    other_color_inline_plus = True
                    potentially_gap_plus = False
                    opened_plus = False

        return color, self.picked_cell,\
                opened_minus, opened_plus, \
                inline_minus_cells, inline_plus_cells, \
                gap_minus_cells, gap_plus_cells, \
                empty_minus_cells, empty_plus_cells

        
    def check_inline_per_color_diagonal(self, color):
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
            if self.picked_cell.row_index - i >= 0 and self.picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[self.picked_cell.row_index - i][self.picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_cell = self.Cell(self.picked_cell.row_index - i, self.picked_cell.col_index - i, self.picked_cell, -1, -1)
                        inline_minus_cells.append(inline_cell)
                        if potentially_gap_minus:
                            for j in range(1, empty_minus_counter + 1):
                                gap_cell = self.Cell(self.picked_cell.row_index - i + j, self.picked_cell.col_index - i + j, self.picked_cell, -1, -1)
                                gap_minus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == self.picked_cell.row_index - i + j and cell.col_index == self.picked_cell.col_index - i + j)]
                            potentially_gap_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[self.picked_cell.row_index - i][self.picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_gap_minus = True
                        if (i==4 or self.picked_cell.row_index - i == 0 or self.picked_cell.col_index - i == 0) \
                            and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_cell = self.Cell(self.picked_cell.row_index - i, self.picked_cell.col_index - i, self.picked_cell, -1, -1)
                        empty_minus_cells.append(empty_cell)
                else:
                    other_color_inline_minus = True
                    potentially_gap_minus = False
                    opened_minus = False
            
            # down-right
            if self.picked_cell.row_index + i <= Misc.GRID_MAX_INDEX and self.picked_cell.col_index + i <= Misc.GRID_MAX_INDEX:
                if self.get_btn_color(self.grid[self.picked_cell.row_index + i][self.picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_cell = self.Cell(self.picked_cell.row_index + i, self.picked_cell.col_index + i, self.picked_cell, 1, 1)
                        inline_plus_cells.append(inline_cell)
                        if potentially_gap_plus:
                            for j in range(1, empty_plus_counter + 1):
                                gap_cell = self.Cell(self.picked_cell.row_index + i - j, self.picked_cell.col_index + i - j, self.picked_cell, 1, 1)
                                gap_plus_cells.append(gap_cell)
                                empty_plus_cells = [cell for cell in empty_plus_cells if not (cell.row_index == self.picked_cell.row_index + i - j and cell.col_index == self.picked_cell.col_index + i - j)]
                            potentially_gap_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[self.picked_cell.row_index + i][self.picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_gap_plus = True
                        if (i==4 or self.picked_cell.row_index + i == Misc.GRID_MAX_INDEX or self.picked_cell.col_index + i == Misc.GRID_MAX_INDEX) \
                            and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_cell = self.Cell(self.picked_cell.row_index + i, self.picked_cell.col_index + i, self.picked_cell, 1, 1)
                        empty_plus_cells.append(empty_cell)
                else:
                    other_color_inline_plus = True
                    potentially_gap_plus = False
                    opened_plus = False

        return color, self.picked_cell,\
                opened_minus, opened_plus, \
                inline_minus_cells, inline_plus_cells, \
                gap_minus_cells, gap_plus_cells, \
                empty_minus_cells, empty_plus_cells

        
    def check_inline_per_color_inverted_diagonal(self, color):
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
            # down-left
            if self.picked_cell.row_index + i <= Misc.GRID_MAX_INDEX and self.picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[self.picked_cell.row_index + i][self.picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_cell = self.Cell(self.picked_cell.row_index + i, self.picked_cell.col_index - i, self.picked_cell, 1, -1)
                        inline_minus_cells.append(inline_cell)
                        if potentially_gap_minus:
                            for j in range(1, empty_minus_counter + 1):
                                gap_cell = self.Cell(self.picked_cell.row_index + i - j, self.picked_cell.col_index - i + j, self.picked_cell, 1, -1)
                                gap_minus_cells.append(gap_cell)
                                empty_minus_cells = [cell for cell in empty_minus_cells if not (cell.row_index == self.picked_cell.row_index + i - j and cell.col_index == self.picked_cell.col_index - i + j)]
                            potentially_gap_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[self.picked_cell.row_index + i][self.picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_gap_minus = True
                        if (i==4 or self.picked_cell.row_index + i == Misc.GRID_MAX_INDEX or self.picked_cell.col_index - i == 0) \
                            and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_cell = self.Cell(self.picked_cell.row_index + i, self.picked_cell.col_index - i, self.picked_cell, 1, -1)
                        empty_minus_cells.append(empty_cell)
                else:
                    other_color_inline_minus = True
                    potentially_gap_minus = False
                    opened_minus = False
            
            # up-right
            if self.picked_cell.row_index - i >= 0 and self.picked_cell.col_index + i <= Misc.GRID_MAX_INDEX:
                if self.get_btn_color(self.grid[self.picked_cell.row_index - i][self.picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_cell = self.Cell(self.picked_cell.row_index - i, self.picked_cell.col_index + i, self.picked_cell, -1, 1)
                        inline_plus_cells.append(inline_cell)
                        if potentially_gap_plus:
                            for j in range(1, empty_plus_counter + 1):
                                gap_cell = self.Cell(self.picked_cell.row_index - i + j, self.picked_cell.col_index + i - j, self.picked_cell, -1, 1)
                                gap_plus_cells.append(gap_cell)
                                empty_plus_cells = [cell for cell in empty_plus_cells if not (cell.row_index == self.picked_cell.row_index - i + j and cell.col_index == self.picked_cell.col_index + i - j)]
                            potentially_gap_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[self.picked_cell.row_index - i][self.picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_gap_plus = True
                        if (i==4 or self.picked_cell.row_index - i == 0 or self.picked_cell.col_index + i == Misc.GRID_MAX_INDEX) \
                            and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_cell = self.Cell(self.picked_cell.row_index - i, self.picked_cell.col_index + i, self.picked_cell, -1, 1)
                        empty_plus_cells.append(empty_cell)
                else:
                    other_color_inline_plus = True
                    potentially_gap_plus = False
                    opened_plus = False

        return color, self.picked_cell,\
                opened_minus, opened_plus, \
                inline_minus_cells, inline_plus_cells, \
                gap_minus_cells, gap_plus_cells, \
                empty_minus_cells, empty_plus_cells

        


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
     