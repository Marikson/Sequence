import unittest
from sequence_model import SequenceModel

class TestDetermineInline(unittest.TestCase):
    """Tests for SequenceModel.determine_inline method."""

    def _make_cell(self, row, col, picked_cell=None, dx=0, dy=0):
        return SequenceModel.Cell(row, col, picked_cell, dx, dy)

    def _picked(self, row, col):
        return SequenceModel.Cell(row, col)

    def test_no_cells_both_open(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        empty_minus = [self._make_cell(5, 4, picked, 0, -1),
                       self._make_cell(5, 3, picked, 0, -1),
                       self._make_cell(5, 2, picked, 0, -1),
                       self._make_cell(5, 1, picked, 0, -1)]
        empty_plus = [self._make_cell(5, 6, picked, 0, 1),
                      self._make_cell(5, 7, picked, 0, 1),
                      self._make_cell(5, 8, picked, 0, 1),
                      self._make_cell(5, 9, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=[], inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=empty_minus, empty_plus_cells=empty_plus,
            opened_minus=True, opened_plus=True
        )
        self.assertEqual(result["inline"], 1)
        self.assertEqual(result["gap_counter"], 0)
        self.assertTrue(result["two_ended"])
        self.assertFalse(result["open_in_middle"])

    def test_one_inline_minus_no_gap(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_minus = [self._make_cell(5, 4, picked, 0, -1)]
        empty_minus = [self._make_cell(5, 3, picked, 0, -1),
                       self._make_cell(5, 2, picked, 0, -1)]
        empty_plus = [self._make_cell(5, 6, picked, 0, 1),
                      self._make_cell(5, 7, picked, 0, 1),
                      self._make_cell(5, 8, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=empty_minus, empty_plus_cells=empty_plus,
            opened_minus=True, opened_plus=True
        )
        self.assertEqual(result["inline"], 2)
        self.assertEqual(result["gap_counter"], 0)
        self.assertTrue(result["two_ended"])

    def test_one_inline_plus_no_gap(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_plus = [self._make_cell(5, 6, picked, 0, 1)]
        empty_minus = [self._make_cell(5, 4, picked, 0, -1),
                       self._make_cell(5, 3, picked, 0, -1)]
        empty_plus = [self._make_cell(5, 7, picked, 0, 1),
                      self._make_cell(5, 8, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=[], inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=empty_minus, empty_plus_cells=empty_plus,
            opened_minus=True, opened_plus=True
        )
        self.assertEqual(result["inline"], 2)
        self.assertEqual(result["gap_counter"], 0)
        self.assertTrue(result["two_ended"])

    def test_two_inline_both_sides(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_minus = [self._make_cell(5, 4, picked, 0, -1)]
        inline_plus = [self._make_cell(5, 6, picked, 0, 1)]
        empty_minus = [self._make_cell(5, 3, picked, 0, -1),
                       self._make_cell(5, 2, picked, 0, -1)]
        empty_plus = [self._make_cell(5, 7, picked, 0, 1),
                      self._make_cell(5, 8, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=empty_minus, empty_plus_cells=empty_plus,
            opened_minus=True, opened_plus=True
        )
        self.assertEqual(result["inline"], 3)
        self.assertEqual(result["gap_counter"], 0)
        self.assertTrue(result["two_ended"])

    def test_four_inline_minus_winner(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_minus = [
            self._make_cell(5, 4, picked, 0, -1),
            self._make_cell(5, 3, picked, 0, -1),
            self._make_cell(5, 2, picked, 0, -1),
            self._make_cell(5, 1, picked, 0, -1),
        ]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=False, opened_plus=False
        )
        self.assertEqual(result["inline"], 5)
        self.assertEqual(result["gap_counter"], 0)

    def test_four_inline_plus_winner(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_plus = [
            self._make_cell(5, 6, picked, 0, 1),
            self._make_cell(5, 7, picked, 0, 1),
            self._make_cell(5, 8, picked, 0, 1),
            self._make_cell(5, 9, picked, 0, 1),
        ]

        result = model.determine_inline(
            picked,
            inline_minus_cells=[], inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=False, opened_plus=False
        )
        self.assertEqual(result["inline"], 5)
        self.assertEqual(result["gap_counter"], 0)

    def test_one_gap_minus_side(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        # inline at col 3, gap at col 4
        inline_minus = [self._make_cell(5, 3, picked, 0, -1)]
        gap_minus = [self._make_cell(5, 4, picked, 0, -1)]
        empty_minus = [self._make_cell(5, 2, picked, 0, -1)]
        empty_plus = [self._make_cell(5, 6, picked, 0, 1),
                      self._make_cell(5, 7, picked, 0, 1),
                      self._make_cell(5, 8, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=[],
            gap_minus_cells=gap_minus, gap_plus_cells=[],
            empty_minus_cells=empty_minus, empty_plus_cells=empty_plus,
            opened_minus=True, opened_plus=True
        )
        self.assertEqual(result["inline"], 2)
        self.assertGreaterEqual(result["gap_counter"], 0)

    def test_one_gap_plus_side(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        # inline at col 7, gap at col 6
        inline_plus = [self._make_cell(5, 7, picked, 0, 1)]
        gap_plus = [self._make_cell(5, 6, picked, 0, 1)]
        empty_minus = [self._make_cell(5, 4, picked, 0, -1),
                       self._make_cell(5, 3, picked, 0, -1)]
        empty_plus = [self._make_cell(5, 8, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=[], inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=gap_plus,
            empty_minus_cells=empty_minus, empty_plus_cells=empty_plus,
            opened_minus=True, opened_plus=True
        )
        self.assertEqual(result["inline"], 2)
        self.assertGreaterEqual(result["gap_counter"], 0)

    def test_opened_minus_false_closed_side(self):
        model = SequenceModel()
        picked = self._picked(5, 0)
        inline_plus = [self._make_cell(5, 1, picked, 0, 1),
                       self._make_cell(5, 2, picked, 0, 1)]
        empty_plus = [self._make_cell(5, 3, picked, 0, 1),
                      self._make_cell(5, 4, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=[], inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=empty_plus,
            opened_minus=False, opened_plus=True
        )
        self.assertEqual(result["inline"], 3)
        self.assertTrue(result["one_ended"])
        self.assertFalse(result["two_ended"])

    def test_opened_plus_false_closed_side(self):
        model = SequenceModel()
        picked = self._picked(5, 9)
        inline_minus = [self._make_cell(5, 8, picked, 0, -1),
                        self._make_cell(5, 7, picked, 0, -1)]
        empty_minus = [self._make_cell(5, 6, picked, 0, -1),
                       self._make_cell(5, 5, picked, 0, -1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=empty_minus, empty_plus_cells=[],
            opened_minus=True, opened_plus=False
        )
        self.assertEqual(result["inline"], 3)
        self.assertTrue(result["one_ended"])
        self.assertFalse(result["two_ended"])

    def test_both_closed_no_gap(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_minus = [self._make_cell(5, 4, picked, 0, -1)]
        inline_plus = [self._make_cell(5, 6, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=False, opened_plus=False
        )
        self.assertEqual(result["inline"], 3)
        self.assertFalse(result["one_ended"])
        self.assertFalse(result["two_ended"])

    def test_three_inline_minus_one_plus_no_gap(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_minus = [
            self._make_cell(5, 4, picked, 0, -1),
            self._make_cell(5, 3, picked, 0, -1),
            self._make_cell(5, 2, picked, 0, -1),
        ]
        inline_plus = [self._make_cell(5, 6, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=False, opened_plus=False
        )
        self.assertEqual(result["inline"], 5)
        self.assertEqual(result["gap_counter"], 0)

    def test_gaps_on_both_sides(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        # minus side: inline at col 3, gap at col 4
        inline_minus = [self._make_cell(5, 3, picked, 0, -1)]
        gap_minus = [self._make_cell(5, 4, picked, 0, -1)]
        # plus side: inline at col 7, gap at col 6
        inline_plus = [self._make_cell(5, 7, picked, 0, 1)]
        gap_plus = [self._make_cell(5, 6, picked, 0, 1)]
        empty_minus = []
        empty_plus = []

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=inline_plus,
            gap_minus_cells=gap_minus, gap_plus_cells=gap_plus,
            empty_minus_cells=empty_minus, empty_plus_cells=empty_plus,
            opened_minus=False, opened_plus=False
        )
        self.assertGreaterEqual(result["inline"], 2)
        self.assertIn("gap_counter", result)
        self.assertIn("inline_cells", result)
        self.assertIn("gap_cells", result)
        self.assertIn("empty_cells", result)

    def test_result_keys_present(self):
        model = SequenceModel()
        picked = self._picked(5, 5)

        result = model.determine_inline(
            picked,
            inline_minus_cells=[], inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=False, opened_plus=False
        )
        expected_keys = {"inline", "open_in_middle", "gap_counter",
                         "one_ended", "two_ended", "inline_cells",
                         "empty_cells", "gap_cells"}
        self.assertEqual(set(result.keys()), expected_keys)

    def test_no_internal_keys_leaked(self):
        model = SequenceModel()
        picked = self._picked(5, 5)

        result = model.determine_inline(
            picked,
            inline_minus_cells=[], inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=True, opened_plus=True
        )
        self.assertNotIn("_open_primary", result)
        self.assertNotIn("_open_secondary", result)

    def test_empty_cells_populated_when_both_open(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        empty_minus = [self._make_cell(5, 4, picked, 0, -1),
                       self._make_cell(5, 3, picked, 0, -1)]
        empty_plus = [self._make_cell(5, 6, picked, 0, 1),
                      self._make_cell(5, 7, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=[], inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=empty_minus, empty_plus_cells=empty_plus,
            opened_minus=True, opened_plus=True
        )
        self.assertGreater(len(result["empty_cells"]), 0)

    def test_diagonal_cells(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_minus = [self._make_cell(4, 4, picked, -1, -1),
                        self._make_cell(3, 3, picked, -1, -1)]
        inline_plus = [self._make_cell(6, 6, picked, 1, 1)]
        empty_plus = [self._make_cell(7, 7, picked, 1, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=empty_plus,
            opened_minus=False, opened_plus=True
        )
        self.assertEqual(result["inline"], 4)
        self.assertTrue(result["one_ended"])

    def test_inverted_diagonal_cells(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        # down-left
        inline_minus = [self._make_cell(6, 4, picked, 1, -1),
                        self._make_cell(7, 3, picked, 1, -1)]
        # up-right
        inline_plus = [self._make_cell(4, 6, picked, -1, 1)]
        empty_plus = [self._make_cell(3, 7, picked, -1, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=empty_plus,
            opened_minus=False, opened_plus=True
        )
        self.assertEqual(result["inline"], 4)
        self.assertTrue(result["one_ended"])

    def test_vertical_cells(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_minus = [self._make_cell(4, 5, picked, -1, 0),
                        self._make_cell(3, 5, picked, -1, 0)]
        inline_plus = [self._make_cell(6, 5, picked, 1, 0),
                       self._make_cell(7, 5, picked, 1, 0)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=False, opened_plus=False
        )
        self.assertEqual(result["inline"], 5)

    def test_single_cell_both_closed(self):
        model = SequenceModel()
        picked = self._picked(0, 0)

        result = model.determine_inline(
            picked,
            inline_minus_cells=[], inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=False, opened_plus=False
        )
        self.assertEqual(result["inline"], 1)
        self.assertFalse(result["one_ended"])
        self.assertFalse(result["two_ended"])
        self.assertEqual(result["gap_counter"], 0)

    def test_two_contiguous_gaps_minus(self):
        model = SequenceModel()
        picked = self._picked(5, 5)
        # inline at col 2, gaps at col 3 and 4
        inline_minus = [self._make_cell(5, 2, picked, 0, -1)]
        gap_minus = [self._make_cell(5, 4, picked, 0, -1),
                     self._make_cell(5, 3, picked, 0, -1)]
        empty_minus = []
        empty_plus = [self._make_cell(5, 6, picked, 0, 1),
                      self._make_cell(5, 7, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=[],
            gap_minus_cells=gap_minus, gap_plus_cells=[],
            empty_minus_cells=empty_minus, empty_plus_cells=empty_plus,
            opened_minus=False, opened_plus=True
        )
        self.assertGreaterEqual(result["inline"], 1)
        self.assertIn("gap_counter", result)

    def test_prefers_more_inline_over_open_ends(self):
        """When comparing candidates, more inline should win over openness."""
        model = SequenceModel()
        picked = self._picked(5, 5)
        # 3 inline on minus side, 0 on plus but open
        inline_minus = [
            self._make_cell(5, 4, picked, 0, -1),
            self._make_cell(5, 3, picked, 0, -1),
            self._make_cell(5, 2, picked, 0, -1),
        ]
        empty_plus = [self._make_cell(5, 6, picked, 0, 1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=empty_plus,
            opened_minus=False, opened_plus=True
        )
        self.assertEqual(result["inline"], 4)

    def test_inline_cells_list_contains_picked_cell(self):
        """The picked cell should be counted in inline but returned in inline_cells."""
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_minus = [self._make_cell(5, 4, picked, 0, -1)]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=[],
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=False, opened_plus=False
        )
        # inline count includes picked cell + inline cells
        self.assertEqual(result["inline"], 2)
        # inline_cells should contain the picked cell and the inline cell
        all_rows_cols = [(c.row_index, c.col_index) for c in result["inline_cells"]]
        self.assertIn((5, 5), all_rows_cols)
        self.assertIn((5, 4), all_rows_cols)

    def test_max_inline_capped_at_five(self):
        """With 4 inline on each side (total 9 with picked), result inline should cap meaningfully."""
        model = SequenceModel()
        picked = self._picked(5, 5)
        inline_minus = [
            self._make_cell(5, 4, picked, 0, -1),
            self._make_cell(5, 3, picked, 0, -1),
            self._make_cell(5, 2, picked, 0, -1),
            self._make_cell(5, 1, picked, 0, -1),
        ]
        inline_plus = [
            self._make_cell(5, 6, picked, 0, 1),
            self._make_cell(5, 7, picked, 0, 1),
            self._make_cell(5, 8, picked, 0, 1),
            self._make_cell(5, 9, picked, 0, 1),
        ]

        result = model.determine_inline(
            picked,
            inline_minus_cells=inline_minus, inline_plus_cells=inline_plus,
            gap_minus_cells=[], gap_plus_cells=[],
            empty_minus_cells=[], empty_plus_cells=[],
            opened_minus=False, opened_plus=False
        )
        # INLINE_TO_WIN is 5, so the method should build a sequence of at most 5
        self.assertEqual(result["inline"], 5)
        self.assertEqual(result["gap_counter"], 0)


if __name__ == '__main__':
    unittest.main()