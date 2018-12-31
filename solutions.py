class Collection(object):
    def __init__(self, iterable=None):
        """
        constructor for collection class convert the iterable to tuple (immutable) so we can work on it
        :param iterable: Can be any iterable except dict
        """
        self.iterable = None if type(iterable) in (dict, None) else list(iterable)

    def first(self):
        """
        take the first element of the iterable and return it as a list
        :return: list with the first element of the iterable
        """
        return self.iterable[0]

    def last(self):
        """
        take the last element of the iterable and return it
        :return: the last value as list
        """
        return self.iterable[len(self.iterable - 1)]

    def take(self, amount):
        """
        check the amount of item the user ask for. if it's grater then the length of the
        iterable it will return all item. if les i will return the amount
        :param amount: The amount of item the user ask for
        :return: Empty iterable for len less then 0, amount for valid number, all for more then len
        """
        return Collection((self.iterable[:amount]))

    def append(self, *elements):
        """

        :param elements: Add elements to the end of the iterable
        :return: New collection with all elements (old and new)
        """
        elements = type(self.iterable)(elements)
        return None if type(iterable) in (dict, None) else Collection((self.iterable + elements))

    def prepend(self, *elements):
        """

        :param elements: Add elements to the beginning of the iterable
        :return: New collection
        """
        elements = type(self.iterable)(elements)
        return None if type(iterable) in (dict, None) else Collection((elements + self.iterable))

    def filter(self, *callbacks):
        for item in callbacks:
            self.iterable = filter(item, self.iterable)
        return Collection(self.iterable)

    def map(self, *callbacks):
        for item in callbacks:
            self.iterable = map(item, self.iterable)
        return Collection(self.iterable)

    def sort(self, key=None, reversed=False):
        return Collection(sorted(self.iterable, key, reversed))

    def __eq__(self, other):
        return True if self.iterable == other.iterable else False

    def __ne__(self, other):
        return (not (self.__eq__(other)))

    def __str__(self):
        return 'Collection{}'.format(tuple(self.iterable))

    def __repr__(self):
        return 'Collecton' + (self.__str__())

    def reduce(self, callback, initial=0):
        result = initial
        for num in self.iterable:
            result = callback(result, num)
        return (result)

    def sort(self, key=None, reversed=False):
        return Collection(
            sorted(self.iterable, key=lambda func: func[key], reverse=reversed)) if key != None else Collection(
            sorted(self.iterable, key=None, reverse=reversed))

    def set(self, position, value):
        return Collection(self.iterable[:position] + (value) + self.iterable[position + 1:])

    def pluck(self, key):
        return Collection(map(lambda func: func[key], self.iterable))

    def values(self):
        return Collection(self.iterable) if type(iterable) not in (dict, None) else None

    def unique(self):
        return Collection(set(self.iterable))

    def tap(self, callback):
        for index in range(len(self.iterable)):
            callback(self.iterable[index])


c = Collection('HELLO')
c.tap(print)
