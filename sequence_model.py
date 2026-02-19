from misc import Misc

class SequenceModel:
    def __init__(self):
        self.grid = None
        self.clicked_cell = {"r": None, "c": None}
        self.inline_dict = {
            "Red": {
                "inline": 0,
                "two_ended": True,
                "open_in_middle": False,
                "one_ended": False,
                "round_to_come_again": len(Misc.turn) - 1
            }
            , 
            "Green": {
                "inline": 0,
                "two_ended": True,
                "open_in_middle": False,
                "one_ended": False,
                "round_to_come_again": len(Misc.turn) - 1
            }
            , 
            "Blue": {
                "inline": 0,
                "two_ended": True,
                "open_in_middle": False,
                "one_ended": False,
                "round_to_come_again": len(Misc.turn) - 1
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
                if c <= Misc.GRID_SIZE - 5:
                    if all(self.get_btn_color(self.grid[r][c + i]) in [color_code, "Black"] for i in range(5)):
                        return color_code
                    
                # Up
                if c >= 4:
                    if all(self.get_btn_color(self.grid[r][c - i]) in [color_code, "Black"] for i in range(5)):
                        return color_code

                # Right
                if r <= Misc.GRID_SIZE - 5:
                    if all(self.get_btn_color(self.grid[r + i][c]) in [color_code, "Black"] for i in range(5)):
                        return color_code
                    
                # Left
                if r >= 4:
                    if all(self.get_btn_color(self.grid[r - i][c]) in [color_code, "Black"] for i in range(5)):
                        return color_code

                # down-right
                if r <= Misc.GRID_SIZE - 5 and c <= Misc.GRID_SIZE - 5:
                    if all(self.get_btn_color(self.grid[r + i][c + i]) in [color_code, "Black"] for i in range(5)):
                        return color_code

                # up-right
                if r >= 4 and c <= Misc.GRID_SIZE - 5:
                    if all(self.get_btn_color(self.grid[r - i][c + i]) in [color_code, "Black"] for i in range(5)):
                        return color_code
                    
                # down-left
                if r <= Misc.GRID_SIZE - 5 and c >= 4:
                    if all(self.get_btn_color(self.grid[r + i][c - i]) in [color_code, "Black"] for i in range(5)):
                        return color_code

                # up-left
                if r >= 4 and c >= 4:
                    if all(self.get_btn_color(self.grid[r - i][c - i]) in [color_code, "Black"] for i in range(5)):
                        return color_code    

        return None
    

    def set_color(self, color=None):
        if color:
            r, c = self.clicked_cell["r"], self.clicked_cell["c"]
            self.grid[r][c].config(bg=color)
            self.grid[r][c].config(state="disabled")
        self.check_inline_per_color(color, r, c)


    def set_inline_dict(self, color, inline_counter, is_open_in_middle, is_one_ended):
        self.inline_dict[color]["inline"] = max(self.inline_dict[color]["inline"], inline_counter)
        self.inline_dict[color]["open_in_middle"] = self.inline_dict[color]["open_in_middle"] or is_open_in_middle
        self.inline_dict[color]["one_ended"] = self.inline_dict[color]["one_ended"] or is_one_ended
        self.inline_dict[color]["two_ended"] = not self.inline_dict[color]["one_ended"] and not self.inline_dict[color]["open_in_middle"]


    def check_inline_per_color(self, color, row, col):
        inline_counter = 1
        is_open_in_middle = False
        is_one_ended = False
        is_two_ended = False
        

        # Horizontal
        for i in range(1, 5):
            # Left
            if col - i >= 0 and self.get_btn_color(self.grid[row][col - i]) in [color, "Black"]:
                inline_counter += 1
            elif col - i >= 0 and self.get_btn_color(self.grid[row][col - i]) == "White":
                for j in range(1, 5-i):
                    if col - i - j >= 0 and self.get_btn_color(self.grid[row][col - i - j]) in [color, "Black"]: 
                        inline_counter += 1
                        is_open_in_middle = True
                    else:
                        break
                break
            else:
                is_one_ended = True
                is_two_ended = False
                break
        for i in range(1, 5):
            # Right
            if col + i < Misc.GRID_SIZE and self.get_btn_color(self.grid[row][col + i]) in [color, "Black"]:
                inline_counter += 1
            elif col + i < Misc.GRID_SIZE and self.get_btn_color(self.grid[row][col + i]) == "White":
                for j in range(1, 5-i):
                    if col + i + j < Misc.GRID_SIZE and self.get_btn_color(self.grid[row][col + i + j]) in [color, "Black"]: 
                        inline_counter += 1
                        is_open_in_middle = True
                    else:
                        break
                break
            else:
                is_one_ended = True
                is_two_ended = False
                break
        self.set_inline_dict(color, inline_counter, is_open_in_middle, is_one_ended)

        # Vertical
        inline_counter = 1
        for i in range(1, 5):
            # Up
            if row - i >= 0 and self.get_btn_color(self.grid[row - i][col]) in [color, "Black"]:
                inline_counter += 1
            elif row - i >= 0 and self.get_btn_color(self.grid[row - i][col]) == "White":
                for j in range(1, 5-i):
                    if row - i - j >= 0 and self.get_btn_color(self.grid[row - i - j][col]) in [color, "Black"]: 
                        inline_counter += 1
                        is_open_in_middle = True
                    else:
                        break
                break
            else:
                is_one_ended = True
                is_two_ended = False
                break
        for i in range(1, 5):
            # Down
            if row + i < Misc.GRID_SIZE and self.get_btn_color(self.grid[row + i][col]) in [color, "Black"]:
                inline_counter += 1
            elif row + i < Misc.GRID_SIZE and self.get_btn_color(self.grid[row + i][col]) == "White":
                for j in range(1, 5-i):
                    if row + i + j < Misc.GRID_SIZE and self.get_btn_color(self.grid[row + i + j][col]) in [color, "Black"]: 
                        inline_counter += 1
                        is_open_in_middle = True
                    else:
                        break
                break
            else:
                is_one_ended = True
                is_two_ended = False
                break
        self.set_inline_dict(color, inline_counter, is_open_in_middle, is_one_ended)

        # Diagonal [0,0] to [9,9]
        inline_counter = 1
        for i in range(1, 5):
            # up-left
            if row - i >= 0 and col - i >= 0 and self.get_btn_color(self.grid[row - i][col - i]) in [color, "Black"]:
                inline_counter += 1
            elif row - i >= 0 and col - i >= 0 and self.get_btn_color(self.grid[row - i][col - i]) == "White":
                for j in range(1, 5-i):
                    if row - i - j >= 0 and col - i - j >= 0 and self.get_btn_color(self.grid[row - i - j][col - i - j]) in [color, "Black"]: 
                        inline_counter += 1
                        is_open_in_middle = True
                    else:
                        break
                break
            else:
                is_one_ended = True
                is_two_ended = False
                break
        for i in range(1, 5):
            # down-right
            if row + i < Misc.GRID_SIZE and col + i < Misc.GRID_SIZE and self.get_btn_color(self.grid[row + i][col + i]) in [color, "Black"]:
                inline_counter += 1
            elif row + i < Misc.GRID_SIZE and col + i < Misc.GRID_SIZE and self.get_btn_color(self.grid[row + i][col + i]) == "White":
                for j in range(1, 5-i):
                    if row + i + j < Misc.GRID_SIZE and col + i + j < Misc.GRID_SIZE and self.get_btn_color(self.grid[row + i + j][col + i + j]) in [color, "Black"]: 
                        inline_counter += 1
                        is_open_in_middle = True
                    else:
                        break
                break
            else:
                is_one_ended = True
                is_two_ended = False
                break
        self.set_inline_dict(color, inline_counter, is_open_in_middle, is_one_ended)        

        # Diagonal [0,9] to [9,0]
        inline_counter = 1
        for i in range(1, 5):
            # up-right
            if row + i < Misc.GRID_SIZE and col - i >= 0 and self.get_btn_color(self.grid[row + i][col - i]) in [color, "Black"]:
                inline_counter += 1
            elif row + i < Misc.GRID_SIZE and col - i >= 0 and self.get_btn_color(self.grid[row + i][col - i]) == "White":
                for j in range(1, 5-inline_counter):
                    if row + i + j < Misc.GRID_SIZE and col - i - j >= 0 and self.get_btn_color(self.grid[row + i + j][col - i - j]) in [color, "Black"]: 
                        inline_counter += 1
                        is_open_in_middle = True
                    else:
                        break
                break
            else:
                is_one_ended = True
                is_two_ended = False
                break
        for i in range(1, 5):
            # down-left
            if row - i >= 0 and col + i < Misc.GRID_SIZE and self.get_btn_color(self.grid[row - i][col + i]) in [color, "Black"]:
                inline_counter += 1
            elif row - i >= 0 and col + i < Misc.GRID_SIZE and self.get_btn_color(self.grid[row - i][col + i]) == "White":
                for j in range(1, 5-inline_counter):
                    if row - i - j >= 0 and col + i + j < Misc.GRID_SIZE and self.get_btn_color(self.grid[row - i - j][col + i + j]) in [color, "Black"]: 
                        inline_counter += 1
                        is_open_in_middle = True
                    else:
                        break
                break
            else:
                is_one_ended = True
                is_two_ended = False
                break
        self.set_inline_dict(color, inline_counter, is_open_in_middle, is_one_ended)
        print(self.inline_dict[color]["inline"],self.inline_dict[color]["open_in_middle"])
     
