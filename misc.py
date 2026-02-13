class Misc:
    GRID_SIZE = 10   # 10x10 grid
    CELL_SIZE = 40   # pixel size of each cell
    PROBABILITY_PER_MOVE = 16 / 104

    colors_selection = {"Red": "#ff0000", "Green": "#006400", "Blue": "#0000ff", "Black": "#000000", "White": "#ffffff"}
    turn = ["Green"] #, "Blue", "Red"]
    win_probability_per_color = {"Red": 0, "Green": 0, "Blue": 0}

    @staticmethod
    def get_color_name(color_code):
        for color, code in vars.colors_selection.items():
            if code == color_code:
                return color
        return None
    

    def print_hex_color(text, hex_color):
        # Remove '#' if present
        hex_color = hex_color.lstrip('#')
        # Convert hex to RGB
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        # ANSI escape for 24-bit color
        print(f"\033[38;2;{r};{g};{b}m{text}\033[0m")
