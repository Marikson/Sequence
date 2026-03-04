from misc import Misc

class SequenceModel:

    class Cell:
        def __init__(self, row, col):
            self.row_index = row
            self.col_index = col

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


    def determine_inline(self, picked_cell: Cell, is_opened_minus, is_opened_plus,
                            inline_minus_indexes, inline_plus_indexes,
                            empty_middle_minus_indexes, empty_middle_plus_indexes,
                            empty_minus_indexes, empty_plus_indexes):
        
        inline_indexes = []
        inline_indexes.append(picked_cell)
        empty_indexes = []
        empty_middle_indexes = []
        
        minus_side_weight = len(inline_minus_indexes)
        plus_side_weight = len(inline_plus_indexes)
        minus_side_secondary_weight = len(empty_middle_minus_indexes)
        plus_side_secondary_weight = len(empty_middle_plus_indexes)


        # Plus side has more inline -> more potential on plus side
        if plus_side_weight > minus_side_weight:
            # If plus is dominant, minus should be part of inline
            if not empty_middle_indexes and minus_side_weight >= 1:
                if empty_middle_plus_indexes:
                    inline_indexes.extend(inline_minus_indexes)
                    empty_middle_indexes.extend(empty_middle_minus_indexes)
                    for i in range(0, plus_side_weight):
                        if picked_cell.are_neighbours(inline_plus_indexes[i]):
                            inline_indexes.append(inline_plus_indexes[i])
                    empty_indexes = self.get_empty_indexes(len(inline_indexes) + len(empty_middle_indexes), empty_minus_indexes, empty_middle_plus_indexes)

                else:
                    inline_indexes.extend(inline_plus_indexes)
                    empty_middle_indexes.extend(empty_middle_minus_indexes)

                    empty_indexes = self.get_empty_indexes(len(inline_indexes) + len(empty_middle_indexes), empty_middle_minus_indexes, empty_plus_indexes)
            
            else:
                inline_indexes.extend(inline_plus_indexes)
                empty_middle_indexes.extend(empty_middle_plus_indexes)
                if plus_side_weight == 3 and is_opened_plus and picked_cell.are_neighbours(empty_middle_minus_indexes[0]):
                    is_opened_minus = True
                
                empty_indexes = self.get_empty_indexes(len(inline_indexes) + len(empty_middle_indexes), empty_minus_indexes, empty_plus_indexes)

        
        

        # Minus side has more inline -> more potential on minus side
        elif plus_side_weight < minus_side_weight:
            if not empty_middle_indexes and plus_side_weight >= 1:
                if empty_middle_minus_indexes:
                    inline_indexes.extend(inline_plus_indexes)
                    empty_middle_indexes.extend(empty_middle_plus_indexes)
                    for i in range(0, minus_side_weight):
                        if picked_cell.are_neighbours(inline_minus_indexes[i]):
                            inline_indexes.append(inline_minus_indexes[i])
                    empty_indexes = self.get_empty_indexes(len(inline_indexes) + len(empty_middle_indexes), empty_middle_minus_indexes, empty_plus_indexes)

                else:
                    inline_indexes.extend(inline_minus_indexes)
                    empty_middle_indexes.extend(empty_middle_plus_indexes)

                    empty_indexes = self.get_empty_indexes(len(inline_indexes) + len(empty_middle_indexes), empty_minus_indexes, empty_middle_plus_indexes)
            
            else:
                inline_indexes.extend(inline_minus_indexes)
                empty_middle_indexes.extend(empty_middle_minus_indexes)
                if minus_side_weight == 3 and is_opened_minus and picked_cell.are_neighbours(empty_middle_plus_indexes[0]):
                    is_opened_plus = True
                
                empty_indexes = self.get_empty_indexes(len(inline_indexes) + len(empty_middle_indexes), empty_minus_indexes, empty_plus_indexes)

            

        # Equal inline on both sides -> check empty middle fields
        elif plus_side_weight == minus_side_weight:
            # More empty middle fields on the plus side -> inline on the minus side is more valuable
            if plus_side_secondary_weight > minus_side_secondary_weight:
                inline_indexes.extend(inline_minus_indexes)
                empty_middle_indexes.extend(empty_middle_minus_indexes)
                if empty_middle_indexes and picked_cell.are_neighbours(inline_plus_indexes[0]):
                    inline_indexes.append(inline_plus_indexes[0])
                
                empty_indexes = self.get_empty_indexes(len(inline_indexes) + len(empty_middle_indexes), empty_minus_indexes, empty_middle_plus_indexes)



            # More empty middle fields on the minus side -> inline on the plus side is more valuable
            elif plus_side_secondary_weight < minus_side_secondary_weight:
                inline_indexes.extend(inline_plus_indexes)
                empty_middle_indexes.extend(empty_middle_plus_indexes)
                if empty_middle_indexes and picked_cell.are_neighbours(inline_minus_indexes[0]):
                    inline_indexes.append(inline_minus_indexes[0])
                
                empty_indexes = self.get_empty_indexes(len(inline_indexes) + len(empty_middle_indexes), empty_middle_minus_indexes, empty_plus_indexes)



            # This scenario can be only 1 by 1 or 2 by 2
            elif plus_side_secondary_weight == minus_side_secondary_weight:
                inline_indexes.extend(inline_minus_indexes)
                inline_indexes.extend(inline_plus_indexes)
                empty_middle_indexes.extend(empty_middle_minus_indexes)
                empty_middle_indexes.extend(empty_middle_plus_indexes)


        inline_sum = len(inline_indexes) if len(inline_indexes) < Misc.INLINE_TO_WIN else 4
        empty_middle_counter = len(empty_middle_indexes)
        open_in_middle = empty_middle_counter > 0
        two_ended = (len(empty_minus_indexes) > 0 or is_opened_minus) and (len(empty_plus_indexes) > 0 or is_opened_plus)
        one_ended = not two_ended and inline_sum + empty_middle_counter < Misc.INLINE_TO_WIN and \
                    (len(empty_minus_indexes) > 0 or len(empty_plus_indexes) > 0 or is_opened_minus or is_opened_plus)
        
        return {"inline": inline_sum,
                "open_in_middle": open_in_middle, 
                "empty_middle_counter": empty_middle_counter, 
                "one_ended": one_ended, 
                "two_ended": two_ended,
                "inline_indexes": inline_indexes,
                "empty_indexes": empty_indexes,
                "empty_middle_indexes": empty_middle_indexes}


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
                            inline_minus_indexes, inline_plus_indexes,
                            empty_middle_minus_indexes, empty_middle_plus_indexes,
                            empty_minus_indexes, empty_plus_indexes):
        
        
        if len(inline_minus_indexes) + len(inline_plus_indexes) + 1 == 1:
            return          
            
        evaluated = self.determine_inline(cell, opened_minus, opened_plus,
                            inline_minus_indexes, inline_plus_indexes,
                            list(reversed(empty_middle_minus_indexes)), list(reversed(empty_middle_plus_indexes)),
                            empty_minus_indexes, empty_plus_indexes)
        
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
            self.inline_dict[color]["inline_indexes"] = evaluated["inline_indexes"]
            self.inline_dict[color]["empty_indexes"] = evaluated["empty_indexes"]
            self.inline_dict[color]["empty_middle_indexes"] = evaluated["empty_middle_indexes"]

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
        inline_minus_indexes = []
        inline_plus_indexes = []
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_minus_indexes = []
        empty_plus_indexes = []
        empty_middle_minus_indexes = []
        empty_middle_plus_indexes = []
        opened_minus = False
        opened_plus = False
        potentially_open_in_middle_minus = False
        potentially_open_in_middle_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # Left
            if picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_minus_indexes.append(self.Cell(picked_cell.row_index, picked_cell.col_index - i))
                        if potentially_open_in_middle_minus:
                            for j in range(1, empty_minus_counter + 1):
                                empty_middle_minus_indexes.append(self.Cell(picked_cell.row_index, picked_cell.col_index - i + j))
                                empty_minus_indexes = [cell for cell in empty_minus_indexes if not (cell.row_index == picked_cell.row_index and cell.col_index == picked_cell.col_index - i + j)]
                            potentially_open_in_middle_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_open_in_middle_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_minus_indexes.append(self.Cell(picked_cell.row_index, picked_cell.col_index - i))

                else:
                    other_color_inline_minus = True
                    potentially_open_in_middle_minus = False
                    opened_minus = False
 
            # Right
            if picked_cell.col_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_plus_indexes.append(self.Cell(picked_cell.row_index, picked_cell.col_index + i))
                        if potentially_open_in_middle_plus:
                            for j in range(1, empty_plus_counter + 1):
                                empty_middle_plus_indexes.append(self.Cell(picked_cell.row_index, picked_cell.col_index + i - j))
                                empty_plus_indexes = [cell for cell in empty_plus_indexes if not (cell.row_index == picked_cell.row_index and cell.col_index == picked_cell.col_index + i - j)]
                            potentially_open_in_middle_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_open_in_middle_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_plus_indexes.append(self.Cell(picked_cell.row_index, picked_cell.col_index + i))

                else:
                    other_color_inline_plus = True
                    potentially_open_in_middle_plus = False
                    opened_plus = False
                    

        self.set_inline_dict(color, picked_cell,
                            opened_minus, opened_plus,
                            inline_minus_indexes, inline_plus_indexes,
                            empty_middle_minus_indexes, empty_middle_plus_indexes,
                            empty_minus_indexes, empty_plus_indexes)

        
        # Vertical
        inline_minus_indexes = []
        inline_plus_indexes = []
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_minus_indexes = []
        empty_plus_indexes = []
        empty_middle_minus_indexes = []
        empty_middle_plus_indexes = []
        opened_minus = False
        opened_plus = False
        potentially_open_in_middle_minus = False
        potentially_open_in_middle_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # Up
            if picked_cell.row_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_minus_indexes.append(self.Cell(picked_cell.row_index - i, picked_cell.col_index))
                        if potentially_open_in_middle_minus:
                            for j in range(1, empty_minus_counter + 1):
                                empty_middle_minus_indexes.append(self.Cell(picked_cell.row_index - i + j, picked_cell.col_index))
                                empty_minus_indexes = [cell for cell in empty_minus_indexes if not (cell.row_index == picked_cell.row_index - i + j and cell.col_index == picked_cell.col_index)]
                            potentially_open_in_middle_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index]) == "White":
                    if not other_color_inline_minus:
                        potentially_open_in_middle_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_minus_indexes.append(self.Cell(picked_cell.row_index - i, picked_cell.col_index))

                else:
                    other_color_inline_minus = True
                    potentially_open_in_middle_minus = False
                    opened_minus = False

            # Down
            if picked_cell.row_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_plus_indexes.append(self.Cell(picked_cell.row_index + i, picked_cell.col_index))
                        if potentially_open_in_middle_plus:
                            for j in range(1, empty_plus_counter + 1):
                                empty_middle_plus_indexes.append(self.Cell(picked_cell.row_index + i - j, picked_cell.col_index))
                                empty_minus_indexes = [cell for cell in empty_minus_indexes if not (cell.row_index == picked_cell.row_index + i - j and cell.col_index == picked_cell.col_index)]
                            potentially_open_in_middle_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index]) == "White":
                    if not other_color_inline_plus:
                        potentially_open_in_middle_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_plus_indexes.append(self.Cell(picked_cell.row_index + i, picked_cell.col_index))

                else:
                    other_color_inline_plus = True
                    potentially_open_in_middle_plus = False
                    opened_plus = False

        # self.set_inline_dict(color, picked_cell,
        #                     opened_minus, opened_plus,
        #                     inline_minus_indexes, inline_plus_indexes,
        #                     empty_middle_minus_indexes, empty_middle_plus_indexes,
        #                     empty_minus_indexes, empty_plus_indexes)
        

        # Diagonal [0,0] to [9,9]
        inline_minus_indexes = []
        inline_plus_indexes = []
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_minus_indexes = []
        empty_plus_indexes = []
        empty_middle_minus_indexes = []
        empty_middle_plus_indexes = []
        opened_minus = False
        opened_plus = False
        potentially_open_in_middle_minus = False
        potentially_open_in_middle_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # up-left
            if picked_cell.row_index - i >= 0 and picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_minus_indexes.append(self.Cell(picked_cell.row_index - i, picked_cell.col_index - i))
                        if potentially_open_in_middle_minus:
                            for j in range(1, empty_minus_counter + 1):
                                empty_middle_minus_indexes.append(self.Cell(picked_cell.row_index - i + j, picked_cell.col_index - i + j))
                                empty_minus_indexes = [cell for cell in empty_minus_indexes if not (cell.row_index == picked_cell.row_index - i + j and cell.col_index == picked_cell.col_index - i + j)]
                            potentially_open_in_middle_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_open_in_middle_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_minus_indexes.append(self.Cell(picked_cell.row_index - i, picked_cell.col_index - i))
                else:
                    other_color_inline_minus = True
                    potentially_open_in_middle_minus = False
                    opened_minus = False
            
            # down-right
            if picked_cell.row_index + i < Misc.GRID_SIZE and picked_cell.col_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_plus_indexes.append(self.Cell(picked_cell.row_index + i, picked_cell.col_index + i))
                        if potentially_open_in_middle_plus:
                            for j in range(1, empty_plus_counter + 1):
                                empty_middle_plus_indexes.append(self.Cell(picked_cell.row_index + i - j, picked_cell.col_index + i - j))
                                empty_minus_indexes = [cell for cell in empty_minus_indexes if not (cell.row_index == picked_cell.row_index + i - j and cell.col_index == picked_cell.col_index + i - j)]
                            potentially_open_in_middle_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_open_in_middle_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_plus_indexes.append(self.Cell(picked_cell.row_index + i, picked_cell.col_index + i))
                else:
                    other_color_inline_plus = True
                    potentially_open_in_middle_plus = False
                    opened_plus = False

        # self.set_inline_dict(color, picked_cell,
        #                     opened_minus, opened_plus,
        #                     inline_minus_indexes, inline_plus_indexes,
        #                     empty_middle_minus_indexes, empty_middle_plus_indexes,
        #                     empty_minus_indexes, empty_plus_indexes)
        

        # Diagonal [0,9] to [9,0]
        inline_minus_indexes = []
        inline_plus_indexes = []
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_minus_indexes = []
        empty_plus_indexes = []
        empty_middle_minus_indexes = []
        empty_middle_plus_indexes = []
        opened_minus = False
        opened_plus = False
        potentially_open_in_middle_minus = False
        potentially_open_in_middle_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # up-right
            if picked_cell.row_index + i < Misc.GRID_SIZE and picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_minus_indexes.append(self.Cell(picked_cell.row_index + i, picked_cell.col_index - i))
                        if potentially_open_in_middle_minus:
                            for j in range(1, empty_minus_counter + 1):
                                empty_middle_minus_indexes.append(self.Cell(picked_cell.row_index + i - j, picked_cell.col_index - i + j))
                                empty_minus_indexes = [cell for cell in empty_minus_indexes if not (cell.row_index == picked_cell.row_index + i - j and cell.col_index == picked_cell.col_index - i + j)]
                            potentially_open_in_middle_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_open_in_middle_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                        empty_minus_indexes.append(self.Cell(picked_cell.row_index + i, picked_cell.col_index - i))
                else:
                    other_color_inline_minus = True
                    potentially_open_in_middle_minus = False
                    opened_minus = False
            
            # down-left
            if picked_cell.row_index - i >= 0 and picked_cell.col_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_plus_indexes.append(self.Cell(picked_cell.row_index - i, picked_cell.col_index + i))
                        if potentially_open_in_middle_plus:
                            for j in range(1, empty_plus_counter + 1):
                                empty_middle_plus_indexes.append(self.Cell(picked_cell.row_index - i + j, picked_cell.col_index + i - j))
                                empty_minus_indexes = [cell for cell in empty_minus_indexes if not (cell.row_index == picked_cell.row_index - i + j and cell.col_index == picked_cell.col_index + i - j)]
                            potentially_open_in_middle_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_open_in_middle_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                        empty_plus_indexes.append(self.Cell(picked_cell.row_index - i, picked_cell.col_index + i))
                else:
                    other_color_inline_plus = True
                    potentially_open_in_middle_plus = False
                    opened_plus = False

        # self.set_inline_dict(color, picked_cell,
        #                     opened_minus, opened_plus,
        #                     inline_minus_indexes, inline_plus_indexes,
        #                     empty_middle_minus_indexes, empty_middle_plus_indexes,
        #                     empty_minus_indexes, empty_plus_indexes)

        
        print(f"  Inline: {self.inline_dict[color]['inline']} " \
              f"\n  Open in middle: {self.inline_dict[color]['open_in_middle']} " \
              f"\n  Empty middle counter: {self.inline_dict[color]['empty_middle_counter']} " \
              f"\n  One ended: {self.inline_dict[color]['one_ended']} " \
              f"\n  Two ended: {self.inline_dict[color]['two_ended']} " \
              f"\n  Inline indexes: {[f'[{cell.row_index}][{cell.col_index}]' for cell in self.inline_dict[color]['inline_indexes']]} "
              f"\n  Empty middle indexes: {[f'[{cell.row_index}][{cell.col_index}]' for cell in self.inline_dict[color]['empty_middle_indexes']]} "
              f"\n  Empty indexes: {[f'[{cell.row_index}][{cell.col_index}]' for cell in self.inline_dict[color]['empty_indexes']]} "
              )
     