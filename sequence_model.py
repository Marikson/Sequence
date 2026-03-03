from misc import Misc

class SequenceModel:

    class Cell:
        def __init__(self, row, col):
            self.row_index = row
            self.col_index = col

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
                "empty_indexes_for_inline": [],
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
                "empty_indexes_for_inline": [],
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
                "empty_indexes_for_inline": [],
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


    def even_in_line(self, cell: Cell, inline_sum, inline_counter_minus, inline_counter_plus, 
                        is_open_in_middle_minus, is_open_in_middle_plus, is_opened_minus, is_opened_plus,
                        empty_minus_counter, empty_plus_counter, empty_middle_minus_counter, empty_middle_plus_counter):
        
        if inline_sum >= Misc.INLINE_TO_WIN:
            inline_sum = Misc.INLINE_TO_WIN - 1


        if inline_counter_minus > inline_counter_plus:
            open_in_middle = is_open_in_middle_minus
            empty_middle_counter = empty_middle_minus_counter
   
        elif inline_counter_plus > inline_counter_minus:
            open_in_middle = is_open_in_middle_plus
            empty_middle_counter = empty_middle_plus_counter
        
        two_ended = (empty_minus_counter > 0 or is_opened_minus) and (empty_plus_counter > 0 or is_opened_plus)
        one_ended = not two_ended and inline_sum + empty_middle_counter < Misc.INLINE_TO_WIN and \
                    (empty_minus_counter > 0 or empty_plus_counter > 0 or is_opened_minus or is_opened_plus)
        
        inline_indexes = []


        return {"inline": inline_sum,
                "open_in_middle": open_in_middle, 
                "empty_middle_counter": empty_middle_counter, 
                "one_ended": one_ended, 
                "two_ended": two_ended}


    def odd_in_line(self, cell: Cell, inline_sum, inline_counter_minus, inline_counter_plus, 
                        is_open_in_middle_minus, is_open_in_middle_plus, is_opened_minus, is_opened_plus,
                        empty_minus_counter, empty_plus_counter, empty_middle_minus_counter, empty_middle_plus_counter):
        
        if inline_sum >= Misc.INLINE_TO_WIN:
            inline_sum = Misc.INLINE_TO_WIN - 1

        if inline_counter_minus > inline_counter_plus:
            open_in_middle = is_open_in_middle_minus
            empty_middle_counter = empty_middle_minus_counter 
                
        elif inline_counter_plus > inline_counter_minus:
            open_in_middle = is_open_in_middle_plus
            empty_middle_counter = empty_middle_plus_counter
            
        elif inline_counter_plus == inline_counter_minus:
            open_in_middle = is_open_in_middle_minus or is_open_in_middle_plus
            empty_middle_counter = empty_middle_minus_counter + empty_middle_plus_counter
        
        two_ended = (empty_minus_counter > 0 or is_opened_minus) and (empty_plus_counter > 0 or is_opened_plus)
        one_ended = not two_ended and inline_sum + empty_middle_counter < Misc.INLINE_TO_WIN and \
                    (empty_minus_counter > 0 or empty_plus_counter > 0 or is_opened_minus or is_opened_plus)
                        
        
        return {"inline": inline_sum,
                "open_in_middle": open_in_middle, 
                "empty_middle_counter": empty_middle_counter, 
                "one_ended": one_ended, 
                "two_ended": two_ended}


    def set_inline_dict(self, color, cell: Cell, inline_counter_minus, inline_counter_plus, 
                        is_open_in_middle_minus, is_open_in_middle_plus, is_opened_minus, is_opened_plus,
                        empty_minus_counter, empty_plus_counter,
                        empty_middle_minus_counter, empty_middle_plus_counter):
        
        inline_sum = 1 + inline_counter_minus + inline_counter_plus
        if inline_sum == 1:
            return          
            
        if inline_sum % 2 == 0:
            evaluated = self.even_in_line(cell, inline_sum, inline_counter_minus, inline_counter_plus,
                            is_open_in_middle_minus, is_open_in_middle_plus, is_opened_minus, is_opened_plus,
                            empty_minus_counter, empty_plus_counter,
                            empty_middle_minus_counter, empty_middle_plus_counter)
        
        elif inline_sum % 2 == 1:
            evaluated = self.odd_in_line(cell, inline_sum, inline_counter_minus, inline_counter_plus,
                            is_open_in_middle_minus, is_open_in_middle_plus, is_opened_minus, is_opened_plus,
                            empty_minus_counter, empty_plus_counter,
                            empty_middle_minus_counter, empty_middle_plus_counter)
        
        if evaluated["inline"] > self.inline_dict[color]["inline"]:
            self.inline_dict[color]["inline"] = evaluated["inline"]
            self.inline_dict[color]["open_in_middle"] = evaluated["open_in_middle"]
            self.inline_dict[color]["empty_middle_counter"] = evaluated["empty_middle_counter"]
            self.inline_dict[color]["one_ended"] = evaluated["one_ended"]
            self.inline_dict[color]["two_ended"] = evaluated["two_ended"]
        
        elif evaluated["inline"] == self.inline_dict[color]["inline"]:
            if evaluated["two_ended"] and not self.inline_dict[color]["two_ended"]:
                self.inline_dict[color]["inline"] = evaluated["inline"]
                self.inline_dict[color]["open_in_middle"] = evaluated["open_in_middle"]
                self.inline_dict[color]["empty_middle_counter"] = evaluated["empty_middle_counter"]
                self.inline_dict[color]["one_ended"] = evaluated["one_ended"]
                self.inline_dict[color]["two_ended"] = evaluated["two_ended"]

        self.inline_dict[color]["round_to_come_again"] = len(Misc.turn) - 1

        calculated_probability = self.calculate_win_probability(color)


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
        inline_counter_minus = 0
        inline_counter_plus = 0
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_middle_minus_counter = 0
        empty_middle_plus_counter = 0
        opened_minus = False
        opened_plus = False
        is_open_in_middle_minus = False
        is_open_in_middle_plus = False
        potentially_open_in_middle_minus = False
        potentially_open_in_middle_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # Left
            if picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_counter_minus += 1
                        if potentially_open_in_middle_minus:
                            empty_middle_minus_counter = empty_middle_minus_counter + empty_minus_counter
                            is_open_in_middle_minus = True
                            potentially_open_in_middle_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_open_in_middle_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                else:
                    other_color_inline_minus = True
                    potentially_open_in_middle_minus = False
                    opened_minus = False
 
            # Right
            if picked_cell.col_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_counter_plus += 1
                        if potentially_open_in_middle_plus:
                            empty_middle_plus_counter = empty_middle_plus_counter + empty_plus_counter
                            is_open_in_middle_plus = True
                            potentially_open_in_middle_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index][picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_open_in_middle_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                else:
                    other_color_inline_plus = True
                    potentially_open_in_middle_plus = False
                    opened_plus = False
                    

        self.set_inline_dict(color, picked_cell, inline_counter_minus, inline_counter_plus,
                            is_open_in_middle_minus, is_open_in_middle_plus, 
                            opened_minus, opened_plus,
                            empty_minus_counter, empty_plus_counter,
                            empty_middle_minus_counter, empty_middle_plus_counter)

        
        # Vertical
        inline_counter_minus = 0
        inline_counter_plus = 0
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_middle_plus_counter = 0
        empty_middle_minus_counter = 0
        opened_minus = False
        opened_plus = False
        is_open_in_middle_minus = False
        is_open_in_middle_plus = False
        potentially_open_in_middle_minus = False
        potentially_open_in_middle_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # Up
            if picked_cell.row_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_counter_minus += 1
                        if potentially_open_in_middle_minus:
                            empty_middle_minus_counter = empty_middle_minus_counter + empty_minus_counter
                            is_open_in_middle_minus = True
                            potentially_open_in_middle_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index]) == "White":
                    if not other_color_inline_minus:
                        potentially_open_in_middle_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                else:
                    other_color_inline_minus = True
                    potentially_open_in_middle_minus = False
                    opened_minus = False

            # Down
            if picked_cell.row_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_counter_plus += 1
                        if potentially_open_in_middle_plus:
                            empty_middle_plus_counter = empty_middle_plus_counter + empty_plus_counter
                            is_open_in_middle_plus = True
                            potentially_open_in_middle_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index]) == "White":
                    if not other_color_inline_plus:
                        potentially_open_in_middle_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                else:
                    other_color_inline_plus = True
                    potentially_open_in_middle_plus = False
                    opened_plus = False

        self.set_inline_dict(color, picked_cell, inline_counter_minus, inline_counter_plus,
                            is_open_in_middle_minus, is_open_in_middle_plus, 
                            opened_minus, opened_plus,
                            empty_minus_counter, empty_plus_counter,
                            empty_middle_minus_counter, empty_middle_plus_counter)
        

        # Diagonal [0,0] to [9,9]
        inline_counter_minus = 0
        inline_counter_plus = 0
        empty_minus_counter = 0
        empty_plus_counter = 0
        empty_middle_plus_counter = 0
        empty_middle_minus_counter = 0
        opened_minus = False
        opened_plus = False
        is_open_in_middle_minus = False
        is_open_in_middle_plus = False
        potentially_open_in_middle_minus = False
        potentially_open_in_middle_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # up-left
            if picked_cell.row_index - i >= 0 and picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_counter_minus += 1
                        if potentially_open_in_middle_minus:
                            empty_middle_minus_counter = empty_middle_minus_counter + empty_minus_counter
                            is_open_in_middle_minus = True
                            potentially_open_in_middle_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_open_in_middle_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                else:
                    other_color_inline_minus = True
                    potentially_open_in_middle_minus = False
                    opened_minus = False
            
            # down-right
            if picked_cell.row_index + i < Misc.GRID_SIZE and picked_cell.col_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_counter_plus += 1
                        if potentially_open_in_middle_plus:
                            empty_middle_plus_counter = empty_middle_plus_counter + empty_plus_counter
                            is_open_in_middle_plus = True
                            potentially_open_in_middle_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_open_in_middle_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                else:
                    other_color_inline_plus = True
                    potentially_open_in_middle_plus = False
                    opened_plus = False

        self.set_inline_dict(color, picked_cell, inline_counter_minus, inline_counter_plus,
                            is_open_in_middle_minus, is_open_in_middle_plus, 
                            opened_minus, opened_plus,
                            empty_minus_counter, empty_plus_counter,
                            empty_middle_minus_counter, empty_middle_plus_counter)
        

        # Diagonal [0,9] to [9,0]
        inline_counter_minus = 0
        inline_counter_plus = 0
        empty_minus_counter = 0
        empty_plus_counter = 0
        opened_minus = False
        opened_plus = False
        is_open_in_middle_minus = False
        is_open_in_middle_plus = False
        potentially_open_in_middle_minus = False
        potentially_open_in_middle_plus = False
        other_color_inline_minus = False
        other_color_inline_plus = False
        for i in range(1, Misc.INLINE_TO_WIN):
            # up-right
            if picked_cell.row_index + i < Misc.GRID_SIZE and picked_cell.col_index - i >= 0:
                if self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index - i]) in [color, "Black"]:
                    if not other_color_inline_minus:
                        inline_counter_minus += 1
                        if potentially_open_in_middle_minus:
                            empty_middle_minus_counter = empty_middle_minus_counter + empty_minus_counter
                            is_open_in_middle_minus = True
                            potentially_open_in_middle_minus = False
                            empty_minus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index + i][picked_cell.col_index - i]) == "White":
                    if not other_color_inline_minus:
                        potentially_open_in_middle_minus = True
                        if i==4 and not other_color_inline_minus:
                            opened_minus = True
                        else:
                            empty_minus_counter += 1
                else:
                    other_color_inline_minus = True
                    potentially_open_in_middle_minus = False
                    opened_minus = False
            
            # down-left
            if picked_cell.row_index - i >= 0 and picked_cell.col_index + i < Misc.GRID_SIZE:
                if self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index + i]) in [color, "Black"]:
                    if not other_color_inline_plus:
                        inline_counter_plus += 1
                        if potentially_open_in_middle_plus:
                            empty_middle_plus_counter = empty_middle_plus_counter + empty_plus_counter
                            is_open_in_middle_plus = True
                            potentially_open_in_middle_plus = False
                            empty_plus_counter = 0
                elif self.get_btn_color(self.grid[picked_cell.row_index - i][picked_cell.col_index + i]) == "White":
                    if not other_color_inline_plus:
                        potentially_open_in_middle_plus = True
                        if i==4 and not other_color_inline_plus:
                            opened_plus = True
                        else:
                            empty_plus_counter += 1
                else:
                    other_color_inline_plus = True
                    potentially_open_in_middle_plus = False
                    opened_plus = False

        self.set_inline_dict(color, picked_cell, inline_counter_minus, inline_counter_plus,
                            is_open_in_middle_minus, is_open_in_middle_plus, 
                            opened_minus, opened_plus,
                            empty_minus_counter, empty_plus_counter,
                            empty_middle_minus_counter, empty_middle_plus_counter)

        
        # print(f"  Inline: {self.inline_dict[color]['inline']} " \
        #       f"\n  Open in middle: {self.inline_dict[color]['open_in_middle']} " \
        #       f"\n  Empty middle counter: {self.inline_dict[color]['empty_middle_counter']} " \
        #       f"\n  One ended: {self.inline_dict[color]['one_ended']} " \
        #       f"\n  Two ended: {self.inline_dict[color]['two_ended']} ")
     
