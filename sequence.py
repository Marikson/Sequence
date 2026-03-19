import tkinter as tk

from sequence_model import SequenceModel as SM
from misc import Misc
import termplotlib as tpl

class Sequence:
    def __init__(self):
        self.model = SM()


    def create_grid(self, sequence_field):
        cells = []
        for r in range(Misc.GRID_SIZE):
            row = []
            for c in range(Misc.GRID_SIZE):
                if (r == 0 and c == 0) or (r == 0 and c == Misc.GRID_MAX_INDEX) or \
                    (r == Misc.GRID_MAX_INDEX and c == 0) or (r == Misc.GRID_MAX_INDEX and c == Misc.GRID_MAX_INDEX):
                    btn = tk.Button(
                        sequence_field,
                        width=4, height=2,
                        bg="Black",
                        state="disabled"
                    )
                else:
                    btn = tk.Button(
                        sequence_field,
                        width=4, height=2,
                        bg="White",
                        command=lambda r=r, c=c: self.model.on_cell_click(r, c),
                        # text="[{}][{}]".format(r, c)
                    )
                btn.grid(row=r, column=c, sticky="nsew")
                row.append(btn)
            cells.append(row)
        self.model.grid = cells

        # Make rows and columns resize properly
        for i in range(Misc.GRID_MAX_INDEX):
            sequence_field.grid_rowconfigure(i, weight=1)
            sequence_field.grid_columnconfigure(i, weight=1)
    

    def delete_grid(self):
        for row in self.model.grid:
            for btn in row:
                btn.destroy()
        self.model.grid = []


    def cell_picking(self):
        while self.model.picked_cell is None:
            self.model.grid[0][0].winfo_toplevel().update()
    

    def reset_picked_cell(self):
        self.model.picked_cell = None
    
    
    def represent_probability(self, inline_dict):
        values = [round(inline_dict["Green"]["winning_probability"]*100, 1), 
                  round(inline_dict["Blue"]["winning_probability"]*100, 1), 
                  round(inline_dict["Red"]["winning_probability"]*100, 1)]
        fig = tpl.figure()
        fig.barh(values, force_ascii=False, max_width=50)
        
        all_charts = fig.get_string()
        split_chart = all_charts.split("\n")

        for color in Misc.turn:
            color_code = Misc.colors_selection[color]
            line = split_chart[Misc.turn.index(color)]
            if len(line.split(']')[0]) <= 4:
                line = line.replace("]", "%]  ")
            else:
                line = line.replace("]", "%] ")
            Misc.print_hex_color(f"{line}", color_code)


    def start_game(self):
        color_index = 0
        while any(btn["state"] != "disabled" for row in self.model.grid for btn in row):
            current_color = Misc.turn[color_index]
            print(f"Current turn: {current_color}")
            
            self.cell_picking()
            self.model.set_color(current_color)
            self.model.check_inline_per_color(current_color)
            
            self.represent_probability(Misc.inline_dict)
            # Misc.print_inline_dict(current_color)
   
            color_index = (color_index + 1) if color_index < len(Misc.turn) - 1 else 0

            winner_color = self.model.check_winner()
            if winner_color:
                winner_color_code = Misc.colors_selection[winner_color]
                Misc.print_hex_color(f"Winner: {winner_color}", winner_color_code)
                for row in self.model.grid:
                    for btn in row:
                        btn.config(bg=winner_color_code, state="disabled")
                self.delete_grid()
                break
            
            self.reset_picked_cell()


def main():
    field_template = tk.Tk()
    field_template.title("Sequence Field")
    

    sequence_game = Sequence()
    sequence_game.create_grid(field_template)
    sequence_game.start_game()

    field_template.mainloop()


if __name__ == "__main__":
    main()