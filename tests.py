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
        self.assertEqual(solutions.Collection({1, 2, 'hello'}).iterable, [1, 2, 'hello'])

    def test_constructor_get_tuple(self):
        self.assertEqual(solutions.Collection((1, 2, 'hello')).iterable, [1, 2, 'hello'])

    def test_get_first_element(self):
        self.assertEqual(solutions.Collection({1, 2, 3}).first(), 1)

    def test_get_last_element(self):
        self.assertEqual(solutions.Collection({1, 2, 3}).last(), 3)

    def test_take_subset_amount_bigger(self):
        self.assertEqual(solutions.Collection((2, 4, 5, 1)).take(8).iterable, [2, 4, 5, 1])

    def test_take_subset_amount_smaller_then_the_amount_abs(self):
        self.assertEqual(solutions.Collection((2, 4, 5, 1)).take(-28).iterable, [])

    def test_take_subset_amount_smaller(self):
        self.assertEqual(solutions.Collection((2, 4, 5, 1)).take(-4).iterable, [])

    def test_append(self):
        self.assertEqual(solutions.Collection((1, 2, 3)).append({'a', 'b', 'c'}, 'r').iterable,
                         [1, 2, 3, {'a', 'b', 'c'}, 'r'])

    def test_prepend(self):
        self.assertEqual(solutions.Collection({1, 2, 3}).prepend('a').iterable, ['a', 1, 2, 3])

    def test_append_original_iterable_unchanged(self):
        a = solutions.Collection([1, 2, 3])
        b = a.append('a')
        self.assertNotEqual(a.iterable, b.iterable)
        self.assertEqual(a.iterable, [1, 2, 3])
        self.assertEqual(b.iterable, [1, 2, 3, 'a'])

    def test_prepend_original_iterable_unchanged(self):
        a = solutions.Collection([1, 2, 3])
        b = a.prepend('a')
        self.assertNotEqual(a.iterable, b.iterable)
        self.assertEqual(a.iterable, [1, 2, 3])
        self.assertEqual(b.iterable, ['a', 1, 2, 3])

    def test_map(self):
        self.assertEqual(solutions.Collection([1, 2, 3]).map(lambda x: x + 2, lambda x: x * x).iterable, [9, 16, 25])

    def test_reduce_add_equal_15(self):
        self.assertEqual(solutions.Collection([1, 2, 3, 4]).reduce(lambda x, y: x + y, 5), 15)

    def test_reduce_add_equal_10(self):
        self.assertEqual(solutions.Collection([1, 2, 3, 4]).reduce(lambda x, y: x + y), 10)

    def test_sort_list(self):
        self.assertEqual(solutions.Collection('HELLO').sort().iterable, ['E', 'H', 'L', 'L', 'O'])

    def test_sort_list_reversed(self):
        self.assertEqual(solutions.Collection('HELLO').sort(None, True).iterable, ['O', 'L', 'L', 'H', 'E'])

    def test_sort_list_of_dict(self):
        self.assertEqual(
            solutions.Collection([{'name': 'Joe', 'age': 20}, {'name': 'Jane', 'age': 13}]).sort('age').iterable,
            [{'name': 'Jane', 'age': 13}, {'name': 'Joe', 'age': 20}])

    def test_set_position_0(self):
        self.assertEqual(solutions.Collection('HELLO').set(0, 'h').iterable, ['h','E','L','L','O'])

    def test_dict_keys_age(self):
        self.assertEqual(solutions.Collection([{'name': 'Joe', 'age': 20},
                                               {'name': 'Jane', 'age': 13}]).pluck('age').iterable, [20, 13])

    def test_dict_key_name(self):
        self.assertEqual(solutions.Collection([{'name': 'Joe', 'age': 20},
                                               {'name': 'Jane', 'age': 13}]).pluck('name').iterable, ['Joe', 'Jane'])
