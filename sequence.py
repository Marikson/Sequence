import tkinter as tk

from sequence_model import SequenceModel as SM
from misc import Misc

class Sequence:
    def __init__(self):
        self.model = SM()

    def create_grid(self, sequence_field):
        cells = []
        for r in range(Misc.GRID_SIZE):
            row = []
            for c in range(Misc.GRID_SIZE):
                if (r == 0 and c == 0) or (r == 0 and c == Misc.GRID_SIZE - 1) or (r == Misc.GRID_SIZE - 1 and c == 0) or (r == Misc.GRID_SIZE - 1 and c == Misc.GRID_SIZE - 1):
                    btn = tk.Button(
                        sequence_field,
                        width=4, height=2,
                        bg="black",
                        state="disabled"
                    )
                else:
                    btn = tk.Button(
                        sequence_field,
                        width=4, height=2,
                        bg="white",
                        command=lambda r=r, c=c: self.model.on_cell_click(r, c)
                    )
                btn.grid(row=r, column=c, sticky="nsew")
                row.append(btn)
            cells.append(row)
        self.model.grid = cells

        # Make rows and columns resize properly
        for i in range(Misc.GRID_SIZE):
            sequence_field.grid_rowconfigure(i, weight=1)
            sequence_field.grid_columnconfigure(i, weight=1)



    def pick_cell(self):
        while self.model.clicked_cell["r"] is None or self.model.clicked_cell["c"] is None:
            self.model.grid[0][0].winfo_toplevel().update()

        r, c = self.model.clicked_cell["r"], self.model.clicked_cell["c"]
        return r, c


    def start_game(self):
        while any(btn["state"] != "disabled" for row in self.model.grid for btn in row):
            current_color = Misc.turn[0]
            print(f"Current turn: {current_color}")
            self.model.clicked_cell = {"r": None, "c": None}
            self.pick_cell()
            self.model.set_color(current_color)
            
            Misc.turn = Misc.turn[1:] + [Misc.turn[0]]

            winner_color = self.model.check_winner()
            if winner_color:
                winner_color_code = Misc.colors_selection[winner_color]
                Misc.print_hex_color(f"Winner: {winner_color}", winner_color_code)
                break



def main():
    field_template = tk.Tk()
    field_template.title("Sequence Field")
    

    sequence_game = Sequence()
    sequence_game.create_grid(field_template)
    sequence_game.start_game()

    field_template.mainloop()


if __name__ == "__main__":
    main()