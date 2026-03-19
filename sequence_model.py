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

    
    def determine_inline(self, cell,
        inline_minus_cells, inline_plus_cells,
        gap_minus_cells, gap_plus_cells,
        empty_minus_cells, empty_plus_cells,
        opened_minus, opened_plus):
        """
        Determines the longest potential sequence that passes through `cell`,
        combining cells from both the minus (negative relative position) and
        plus (positive relative position) sides.

        Tries BOTH direction orders (minus-first and plus-first), builds a
        candidate sequence for each, and returns the better one.

        Parameters:
            opened_minus: bool - True if the minus side ends with empty fields
                          (sequence can potentially extend), False if blocked by
                          board edge or another color.
            opened_plus:  bool - True if the plus side ends with empty fields
                          (sequence can potentially extend), False if blocked by
                          board edge or another color.

        Quality ranking (higher priority first):
            1. More inline cells
            2. Two-ended > one-ended > closed
            3. Fewer gaps
        """

        # ----------------------------------------------------------------
        # Helper: build an ordered ribbon of cells from one side
        # ----------------------------------------------------------------
        def build_side_ribbon(inline_cells, gap_cells):
            """
            Walk outward from the picked cell along one side.
            Returns a list of (cell, type) tuples sorted by increasing
            abs(relative_position), where type is 'inline' or 'gap'.
            A gap cell is only included if a colored cell follows beyond it.
            """
            inline_set = set(id(c) for c in inline_cells)
            gap_set = set(id(c) for c in gap_cells)
            all_cells = inline_cells + gap_cells
            all_cells.sort(key=lambda c: abs(c.relative_position_to_picked_cell))

            ribbon = []
            pending_gaps = []

            for c in all_cells:
                if id(c) in inline_set:
                    ribbon.extend(pending_gaps)
                    pending_gaps = []
                    ribbon.append((c, "inline"))
                elif id(c) in gap_set:
                    pending_gaps.append((c, "gap"))
            return ribbon

        # ----------------------------------------------------------------
        # Helper: assemble a candidate sequence given a direction order
        # ----------------------------------------------------------------
        def build_candidate(primary_ribbon, secondary_ribbon,
                            primary_empty, secondary_empty,
                            primary_opened, secondary_opened):
            """
            Builds a sequence: primary side → picked cell → secondary side.
            Tries multiple stopping points on the secondary side (at each
            gap boundary) and returns the best sub-candidate.

            primary_opened / secondary_opened indicate whether that side of
            the sequence is open (ends with empty fields rather than being
            blocked by the board edge or another color).
            """

            # --- primary side (always fully consumed up to slot limit) ---
            base_sequence = [("inline", cell)]
            slots_left = Misc.INLINE_TO_WIN - 1

            primary_to_add = []
            for c, kind in primary_ribbon:
                if len(primary_to_add) < slots_left:
                    primary_to_add.append((kind, c))
            base_sequence = list(reversed(primary_to_add)) + base_sequence

            # --- determine all candidate stopping points on secondary ---
            # stopping point 0 = take nothing from secondary
            # stopping point i = take the first i entries from secondary
            # We always try the greedy (take as many as fit) AND every
            # position just before a gap entry starts.
            max_secondary = min(len(secondary_ribbon), Misc.INLINE_TO_WIN - len(base_sequence))
            stop_points = {0, max_secondary}  # always try taking none and taking all
            for idx in range(max_secondary):
                if secondary_ribbon[idx][1] == "gap":
                    stop_points.add(idx)       # stop right before this gap

            def evaluate(secondary_count):
                """Evaluate a candidate that takes `secondary_count` items from secondary."""
                seq = list(base_sequence)
                for i in range(secondary_count):
                    seq.append((secondary_ribbon[i][1], secondary_ribbon[i][0]))

                inline_count = 0
                inline_cells_result = []
                gap_counter = 0
                gap_cells_result = []
                for kind, c in seq:
                    if kind == "inline":
                        inline_count += 1
                        inline_cells_result.append(c)
                    elif kind == "gap":
                        gap_counter += 1
                        gap_cells_result.append(c)

                total_in_sequence = len(seq)
                open_primary = False
                open_secondary = False
                empty_tails = []

                if total_in_sequence < Misc.INLINE_TO_WIN:
                    remaining = Misc.INLINE_TO_WIN - total_in_sequence

                    # Primary side: can only be open if primary_opened is True
                    # (i.e., that side ends with empty fields, not blocked)
                    primary_ribbon_used = len(primary_to_add)
                    if primary_opened and primary_ribbon_used >= len(primary_ribbon) and len(primary_empty) > 0:
                        for i in range(min(remaining, len(primary_empty))):
                            empty_tails.append(primary_empty[i])
                            open_primary = True

                    remaining = Misc.INLINE_TO_WIN - total_in_sequence - len(empty_tails)

                    # Secondary side: can only be open if secondary_opened is True
                    if secondary_opened and secondary_count >= len(secondary_ribbon) and len(secondary_empty) > 0 and remaining > 0:
                        for i in range(min(remaining, len(secondary_empty))):
                            empty_tails.append(secondary_empty[i])
                            open_secondary = True
                    elif secondary_count < len(secondary_ribbon):
                        # We stopped early on secondary; the next ribbon cell
                        # is a gap, meaning the physical board cell is empty —
                        # so the secondary end is open through that gap cell.
                        # This is still within the ribbon, so it's not blocked
                        # by the edge or another color — it's inherently open.
                        gap_cell_as_empty = secondary_ribbon[secondary_count][0]
                        empty_tails.append(gap_cell_as_empty)
                        open_secondary = True

                one_ended = open_primary or open_secondary
                two_ended = open_primary and open_secondary
                open_in_middle = gap_counter > 0

                return {
                    "inline": inline_count,
                    "open_in_middle": open_in_middle,
                    "gap_counter": gap_counter,
                    "one_ended": one_ended,
                    "two_ended": two_ended,
                    "inline_cells": inline_cells_result,
                    "empty_cells": empty_tails,
                    "gap_cells": gap_cells_result,
                    "_open_primary": open_primary,
                    "_open_secondary": open_secondary,
                }

            best_sub = None
            for sp in sorted(stop_points):
                candidate = evaluate(sp)
                if best_sub is None or is_better(candidate, best_sub):
                    best_sub = candidate
            return best_sub

        # ----------------------------------------------------------------
        # Helper: compare two candidates, return True if a is better than b
        # ----------------------------------------------------------------
        def is_better(a, b):
            """
            Quality ranking (higher priority first):
                1. More inline cells
                2. Two-ended > one-ended > closed
                3. Fewer gaps (gap_counter)
            """
            if a["inline"] != b["inline"]:
                return a["inline"] > b["inline"]

            a_open = (2 if a["two_ended"] else (1 if a["one_ended"] else 0))
            b_open = (2 if b["two_ended"] else (1 if b["one_ended"] else 0))
            if a_open != b_open:
                return a_open > b_open

            if a["gap_counter"] != b["gap_counter"]:
                return a["gap_counter"] < b["gap_counter"]

            return False  # equal quality

        # ----------------------------------------------------------------
        # Build ribbons from both sides
        # ----------------------------------------------------------------
        minus_ribbon = build_side_ribbon(inline_minus_cells, gap_minus_cells)
        plus_ribbon = build_side_ribbon(inline_plus_cells, gap_plus_cells)

        # ----------------------------------------------------------------
        # Try BOTH direction orders and pick the better candidate
        # ----------------------------------------------------------------
        # Candidate 1: minus-first (primary=minus, secondary=plus)
        candidate_minus_first = build_candidate(
            minus_ribbon, plus_ribbon,
            empty_minus_cells, empty_plus_cells,
            opened_minus, opened_plus
        )

        # Candidate 2: plus-first (primary=plus, secondary=minus)
        candidate_plus_first = build_candidate(
            plus_ribbon, minus_ribbon,
            empty_plus_cells, empty_minus_cells,
            opened_plus, opened_minus
        )

        if is_better(candidate_minus_first, candidate_plus_first):
            best = candidate_minus_first
        else:
            best = candidate_plus_first

        # Remove internal flags before returning
        best.pop("_open_primary", None)
        best.pop("_open_secondary", None)

        return best


    def set_inline_dict(self, color, cell: Cell,
                            opened_minus, opened_plus,
                            inline_minus_cells, inline_plus_cells,
                            gap_minus_cells, gap_plus_cells,
                            empty_minus_cells, empty_plus_cells):
        
        
        # if len(inline_minus_cells) == 0 and len(inline_plus_cells) == 0:
        #     return          

        evaluated = self.determine_inline(cell,inline_minus_cells, inline_plus_cells,
                                          list(reversed(gap_minus_cells)), list(reversed(gap_plus_cells)),
                                          empty_minus_cells, empty_plus_cells,
                                          opened_minus, opened_plus)

        
        self.update_inline_dict(color, evaluated)
        self.check_if_picked_cell_blocks_opponents(cell, color)
        self.calculate_win_probability(color)
     
    
    def check_if_picked_cell_blocks_opponents(self, cell, color):
        for opponent_color in Misc.turn:
            if opponent_color == color:
                continue
            
            opponent_data = Misc.inline_dict[opponent_color]
            for gap_cell in opponent_data["gap_cells"]:
                if cell.row_index == gap_cell.row_index and cell.col_index == gap_cell.col_index:
                    opponent_data["inline"] = 0
                    opponent_data["one_ended"] = False
                    opponent_data["two_ended"] = False
                    opponent_data["open_in_middle"] = False
                    opponent_data["gap_counter"] = 0
                    opponent_data["inline_cells"] = []
                    opponent_data["gap_cells"] = []
                    opponent_data["empty_cells"] = []
                    opponent_data["winning_probability"] = 0
                    break
                    
            for empty_cell in opponent_data["empty_cells"]:
                if cell.row_index == empty_cell.row_index and cell.col_index == empty_cell.col_index:
                    opponent_data["empty_cells"].remove(empty_cell)
                    break
            


    def update_inline_dict(self, color, evaluated):
        to_update = False
        if evaluated["inline"] > Misc.inline_dict[color]["inline"]:
            to_update = True
        elif evaluated["inline"] == Misc.inline_dict[color]["inline"]:
            if evaluated["two_ended"] and not Misc.inline_dict[color]["two_ended"]:
                to_update = True
            elif evaluated["gap_counter"] < Misc.inline_dict[color]["gap_counter"]:
                to_update = True


        if to_update:
            Misc.inline_dict[color]["inline"] = evaluated["inline"]
            Misc.inline_dict[color]["open_in_middle"] = evaluated["open_in_middle"]
            Misc.inline_dict[color]["gap_counter"] = evaluated["gap_counter"]
            Misc.inline_dict[color]["one_ended"] = evaluated["one_ended"]
            Misc.inline_dict[color]["two_ended"] = evaluated["two_ended"]
            Misc.inline_dict[color]["inline_cells"] = evaluated["inline_cells"]
            Misc.inline_dict[color]["empty_cells"] = evaluated["empty_cells"]
            Misc.inline_dict[color]["gap_cells"] = evaluated["gap_cells"]

        Misc.inline_dict[color]["round_to_come_again"] = 2
        color_index = Misc.turn.index(color)
        next_color_index = (color_index + 1) if color_index < len(Misc.turn) - 1 else 0
        last_color_index = (color_index - 1) if color_index > 0 else len(Misc.turn) - 1
        
        next_color = Misc.turn[next_color_index]
        last_color = Misc.turn[last_color_index]
        
        Misc.inline_dict[next_color]["round_to_come_again"] = 0
        Misc.inline_dict[last_color]["round_to_come_again"] = 1
        

    def calculate_dynamic_blocking_willingness(self, inline, one_ended, two_ended, open_in_middle):
        """
        Dynamically calculate blocking willingness based on threat level.
        
        Key insight: If a player has a two-ended potential sequence (e.g., 4 inline open on both sides),
        BOTH upcoming players must coordinate to block at least one side each, otherwise the threat
        player will win on their next turn.
        
        Returns:
            tuple: (block_attempt_prob, coordination_factor)
                - block_attempt_prob: How likely each opponent is to attempt blocking
                - coordination_factor: Multiplier for coordinated blocking (two-ended threats)
        """
        base_willingness = Misc.WILLING_TO_BLOCK_PROBABILITY  # 0.20
        
        if inline >= 4:
            if two_ended:
                # CRITICAL THREAT: Two-ended 4-inline = guaranteed win unless BOTH opponents block
                # Both players MUST block (one each side) or lose
                # Willingness approaches 1.0 (survival mode)
                block_attempt_prob = min(0.95, base_willingness * 5.0)
                # Coordination factor: both players need to succeed
                # If either fails to block their side, threat player wins
            elif one_ended:
                # HIGH THREAT: One-ended 4-inline = can win with one placement
                # At least one opponent should block
                block_attempt_prob = min(0.85, base_willingness * 4.0)
            elif open_in_middle:
                # MEDIUM-HIGH THREAT: 4-inline with gap
                block_attempt_prob = min(0.80, base_willingness * 4.0)
            else:
                # Blocked on both ends, only middle gaps matter
                block_attempt_prob = base_willingness * 1.5
        elif inline == 3:
            if two_ended:
                # MEDIUM THREAT: Could become critical next turn
                block_attempt_prob = min(0.60, base_willingness * 3.0)
            elif one_ended:
                block_attempt_prob = base_willingness * 1.5
            else:
                block_attempt_prob = base_willingness
        elif inline == 2:
            # LOW THREAT: Early game, low priority to block
            block_attempt_prob = base_willingness * 0.5
        else:
            # MINIMAL THREAT
            block_attempt_prob = base_willingness * 0.25
        
        return block_attempt_prob


    def calculate_win_probability(self, color_who_picked):
        """
        Calculate win probability for ALL colors based on:
        - inline: number of contiguous same-colored fields
        - open_in_middle: whether there's a gap in the sequence
        - gap_counter: number of gaps
        - one_ended: sequence open on one end
        - two_ended: sequence open on both ends (doubles chance to complete)
        - round_to_come_again: how many rounds until this color plays again
          (0 = next turn, 1 = one round away, 2 = two rounds away)
        
        Also factors in blocking: with 3 players, if a player has 4 inline,
        the other 2 players (who play before this player's next turn) will
        try to block. Dynamic blocking willingness based on threat level.
        
        CRITICAL: For two-ended sequences, BOTH opponents must block (one each side)
        or the threat player wins.
        """
        for color in Misc.inline_dict:
            data = Misc.inline_dict[color]
            inline = data["inline"]
            open_in_middle = data["open_in_middle"]
            gap_counter = data["gap_counter"]
            one_ended = data["one_ended"]
            two_ended = data["two_ended"]
            round_to_come_again = data["round_to_come_again"]
            
            # Base probability to place a field
            p = Misc.PROBABILITY_TO_COLOR_FIELD  # 16/104 ≈ 0.154
            
            # How many fields needed to complete the sequence
            missing_cells = Misc.INLINE_TO_WIN - inline
            
            # If already won or no progress
            if missing_cells <= 0:
                Misc.inline_dict[color]["winning_probability"] = 1.0
                continue
            if inline == 0:
                Misc.inline_dict[color]["winning_probability"] = 0.0
                continue
            
            # --- Round delay factor ---
            # The more rounds until this color plays again, the more chance
            # opponents have to block or advance their own sequences.
            # round_to_come_again: 0 = plays next, 1 = one round away, 2 = two rounds away
            round_delay_factor = 1.0 / (1.0 + round_to_come_again * 0.3)
            
            # --- Open-ended multiplier ---
            # Two-ended sequence with 4 inline: 2 ways to complete (either end)
            # P(complete) = 2p - p^2 ≈ 2p for small p
            if two_ended and inline == 4:
                completion_multiplier = 2.0
            elif one_ended:
                completion_multiplier = 1.0
            else:
                # Sequence is blocked on both ends - can only win via middle gaps
                completion_multiplier = 0.5 if open_in_middle else 0.0
            
            # --- Gap penalty ---
            # Gaps in the middle require additional placements
            gap_penalty = (1 - p) ** gap_counter if gap_counter > 0 else 1.0
            
            # --- Base win probability ---
            # Probability to place the required missing cells
            base_probability = (p ** missing_cells) * completion_multiplier * gap_penalty
            
            # --- Dynamic Blocking factor (3 players) ---
            num_players = len(Misc.turn) if len(Misc.turn) > 1 else 3
            
            # Number of opponents who get to play before this color's next turn
            # round_to_come_again tells us how far away our next turn is
            # More rounds = more opponents get chances to block
            opponents_before_next_turn = min(round_to_come_again + 1, num_players - 1)
            
            # Get dynamic blocking parameters based on threat level
            block_attempt_prob = self.calculate_dynamic_blocking_willingness(
                inline, one_ended, two_ended, open_in_middle
            )
            
            if inline >= 3 and (one_ended or two_ended or open_in_middle):
                # Block success probability = willingness * chance to have right card
                block_success_prob = p
                
                if two_ended and inline >= 4:
                    # SPECIAL CASE: Two-ended threat requires BOTH opponents to block
                    # Player 1 blocks side A, Player 2 blocks side B
                    # Probability both succeed = P(player1 blocks) * P(player2 blocks)
                    single_block_success = block_attempt_prob * block_success_prob
                    
                    # With more rounds to wait, opponents have more attempts to block
                    # Effective block probability increases with round_to_come_again
                    effective_block_prob = 1.0 - (1.0 - single_block_success) ** (1 + round_to_come_again)
                    
                    # For threat player to survive: at least one side must remain unblocked
                    # P(both sides blocked) = P(side A blocked) * P(side B blocked)
                    prob_both_sides_blocked = effective_block_prob ** 2
                    
                    # Threat player wins if at least one side is NOT blocked
                    blocking_survival = 1 - prob_both_sides_blocked
                else:
                    # Standard blocking: any opponent can block the single open position
                    single_opponent_blocks = block_attempt_prob * block_success_prob
                    # More opponents before next turn = higher chance of being blocked
                    prob_no_one_blocks = (1 - single_opponent_blocks) ** opponents_before_next_turn
                    blocking_survival = prob_no_one_blocks
            else:
                # Low threat: unlikely to be blocked, but round delay still matters
                blocking_survival = 1.0
            
            # Final probability incorporating round delay
            win_probability = base_probability * blocking_survival * round_delay_factor
            
            # Clamp to [0, 1]
            win_probability = max(0.0, min(1.0, win_probability))
            
            # Store in dict
            Misc.inline_dict[color]["winning_probability"] = win_probability
        
        
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

        
   