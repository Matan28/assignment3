import unittest
import solutions


class CollectionClass(unittest.TestCase):
    def test_constructor_equal_none(self):
        self.assertEqual(solutions.Collection().iterable, None)

    def test_constructor_get_dict_equal_none(self):
        self.assertEqual(solutions.Collection({1: 'hello', 2: 'world'}).iterable, None)

    def test_constructor_get_list(self):
        self.assertEqual(solutions.Collection([1, 2, 'hello']).iterable, [1, 2, 'hello'])

    def test_constructor_get_set(self):
        self.assertEqual(solutions.Collection({1, 2, 'hello'}).iterable, {1, 2, 'hello'})

    def test_constructor_get_tuple(self):
        self.assertEqual(solutions.Collection((1, 2, 'hello')).iterable, (1, 2, 'hello'))
