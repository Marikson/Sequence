class Misc:
    GRID_SIZE = 10
    GRID_MAX_INDEX = GRID_SIZE - 1
    
    colors_selection = {"Red": "#ff0000", "Green": "#006400", "Blue": "#0000ff", "Black": "#000000", "White": "#ffffff"}
    turn = ["Green", "Blue", "Red"]
    
    inline_dict = {
            "Green": {
                "inline": 0,
                "two_ended": False,
                "open_in_middle": False,
                "gap_counter": 0,
                "one_ended": False,
                "round_to_come_again": 0,
                "inline_cells": [],
                "gap_cells": [],
                "empty_cells": [],
                "winning_probability": 0
            }, 
            "Blue": {
                "inline": 0,
                "two_ended": False,
                "open_in_middle": False,
                "gap_counter": 0,
                "one_ended": False,
                "round_to_come_again": 0,
                "inline_cells": [],
                "gap_cells": [],
                "empty_cells": [],
                "winning_probability": 0
            },
            "Red": {
                "inline": 0,
                "two_ended": False,
                "open_in_middle": False,
                "gap_counter": 0,
                "one_ended": False,
                "round_to_come_again": 0,
                "inline_cells": [],
                "gap_cells": [],
                "empty_cells": [],
                "winning_probability": 0
            }
        }


    def print_hex_color(text, hex_color):
        # Remove '#' if present
        hex_color = hex_color.lstrip('#')
        # Convert hex to RGB
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        # ANSI escape for 24-bit color
        print(f"\033[38;2;{r};{g};{b}m{text}\033[0m")
        
    
    @staticmethod
    def print_inline_dict(color):
        print(f"  Inline: {Misc.inline_dict[color]['inline']} " \
              f"\n  Open in middle: {Misc.inline_dict[color]['open_in_middle']} " \
              f"\n  Empty middle counter: {Misc.inline_dict[color]['empty_middle_counter']} " \
              f"\n  One ended: {Misc.inline_dict[color]['one_ended']} " \
              f"\n  Two ended: {Misc.inline_dict[color]['two_ended']} " \
              f"\n  Inline cells: {[f'[{cell.row_index}][{cell.col_index}]' for cell in Misc.inline_dict[color]['inline_cells']]} " \
              f"\n  Empty middle cells: {[f'[{cell.row_index}][{cell.col_index}]' for cell in Misc.inline_dict[color]['empty_middle_cells']]} " \
              f"\n  Empty cells: {[f'[{cell.row_index}][{cell.col_index}]' for cell in Misc.inline_dict[color]['empty_cells']]} " \
              f"\n  Winning probability: {round(Misc.inline_dict[color]['winning_probability']*100, 1)}%" \
              f"\n Round to come again: {Misc.inline_dict[color]['round_to_come_again']}"
              )
        
