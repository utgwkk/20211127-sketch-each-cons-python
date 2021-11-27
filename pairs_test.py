import unittest

from pairs import pairs_append_yield, pairs_even_odd, pairs_index_access, pairs_slice_copy

class TestPairsFunction(unittest.TestCase):
    def test_pairs_append_yield(self):
        xs = [1, 2, 3, 4, 5, 6]
        gen = pairs_append_yield(xs)
        self.assertTupleEqual(next(gen), (1, 2))
        self.assertTupleEqual(next(gen), (3, 4))
        self.assertTupleEqual(next(gen), (5, 6))
        with self.assertRaises(StopIteration):
            next(gen)

    def test_pairs_even_odd(self):
        xs = [1, 2, 3, 4, 5, 6]
        gen = pairs_even_odd(xs)
        self.assertTupleEqual(next(gen), (1, 2))
        self.assertTupleEqual(next(gen), (3, 4))
        self.assertTupleEqual(next(gen), (5, 6))
        with self.assertRaises(StopIteration):
            next(gen)

    def test_pairs_index_access(self):
        xs = [1, 2, 3, 4, 5, 6]
        gen = pairs_index_access(xs)
        self.assertTupleEqual(next(gen), (1, 2))
        self.assertTupleEqual(next(gen), (3, 4))
        self.assertTupleEqual(next(gen), (5, 6))
        with self.assertRaises(StopIteration):
            next(gen)

    def test_pairs_slice_copy(self):
        xs = [1, 2, 3, 4, 5, 6]
        gen = pairs_slice_copy(xs)
        self.assertTupleEqual(next(gen), (1, 2))
        self.assertTupleEqual(next(gen), (3, 4))
        self.assertTupleEqual(next(gen), (5, 6))
        with self.assertRaises(StopIteration):
            next(gen)

if __name__ == '__main__':
    unittest.main()
