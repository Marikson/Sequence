from misc import Misc

class SequenceModel:
    def __init__(self):
        self.grid = None
        self.clicked_cell = {"r": None, "c": None}


    def on_cell_click(self, row, col):
        self.clicked_cell["r"] = row
        self.clicked_cell["c"] = col


    def get_btn_color(self, btn):
        return btn.cget("bg")

    
    def check_winner(self):
        for r in range(Misc.GRID_SIZE):
            for c in range(Misc.GRID_SIZE):
                color_code = self.get_btn_color(self.grid[r][c])
                if color_code in ("white"):
                    continue

                # Check horizontal
                if c <= Misc.GRID_SIZE - 5:
                    if all(self.get_btn_color(self.grid[r][c + i]) in [color_code, "black"] for i in range(5)):
                        return color_code

                # Check vertical
                if r <= Misc.GRID_SIZE - 5:
                    if all(self.get_btn_color(self.grid[r + i][c]) in [color_code, "black"] for i in range(5)):
                        return color_code

                # Check diagonal down-right
                if r <= Misc.GRID_SIZE - 5 and c <= Misc.GRID_SIZE - 5:
                    if all(self.get_btn_color(self.grid[r + i][c + i]) in [color_code, "black"] for i in range(5)):
                        return color_code

                # Check diagonal up-right
                if r >= 4 and c <= Misc.GRID_SIZE - 5:
                    if all(self.get_btn_color(self.grid[r - i][c + i]) in [color_code, "black"] for i in range(5)):
                        return color_code
                    
                # Check diagonal down-left
                if r <= Misc.GRID_SIZE - 5 and c >= 4:
                    if all(self.get_btn_color(self.grid[r + i][c - i]) in [color_code, "black"] for i in range(5)):
                        return color_code

                # Check diagonal up-left
                if r >= 4 and c >= 4:
                    if all(self.get_btn_color(self.grid[r - i][c - i]) in [color_code, "black"] for i in range(5)):
                        return color_code    

        return None
    

    def set_color(self, color=None):
        if color:
            r, c = self.clicked_cell["r"], self.clicked_cell["c"]
            self.grid[r][c].config(bg=color)
            self.grid[r][c].config(state="disabled")
