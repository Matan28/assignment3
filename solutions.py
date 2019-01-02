class Collection(object):
    def __init__(self, iterable=None):
        """
        constructor for collection class convert the iterable to tuple (immutable) so we can work on it
        :param iterable: Can be any iterable except dict
        """
        self.iterable = None if type(iterable) in (None, dict) else list(iterable)

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
        return self.iterable[-1]

    def take(self, amount):
        """
        check the amount of item the user ask for. if it's grater then the length of the
        iterable it will return all item. if les i will return the amount
        :exception
        If the amount bigger take() will return all the iterable
        If the amount is a negative number smaller then abs of amount take() will return take(-amount)
        self.iterable[:-amount] return from the end
        If the amount is a negative number bigger then abs of amount take() will return empty list []
        :param amount: The amount of item the user ask for
        :return: Empty iterable for len less then 0, amount for valid number, all for more then len
        """
        return Collection((self.iterable[:amount]))

    def append(self, *elements):
        """
        add new element to the end of the iterable if the elements are not None or Dict
        :param elements: new element to add in the end
        :return: New collection with the new elements in the end.
        """
        return None if type(elements) in (dict, None) else Collection((self.iterable + list(elements)))

    def prepend(self, *elements):
        """
        add new element to the head of the iterable if the elements are not None or Dict
        :param elements: new element to add in the beginning of the iterable
        :return: New collection with the elements in the biginning of the iterable
        """
        return None if type(elements) in (dict, None) else Collection((list(elements) + self.iterable))

    def filter(self, *callbacks):
        """
        take the self.iterable and filter with all the functions in callback
        :param callbacks: function to filter with the function need to be bool
        :return: new collection with the filter elements
        """
        return Collection([item for item in self.iterable if all(fun(item) for fun in callbacks)])

    def map(self, *callbacks):
        """
        take multi function and computation it on the iterable
        :param callbacks: functions
        :return: iterable after apply the callback
        """
        temp = self.iterable
        for item in callbacks:
            temp = map(item, temp)
        return Collection(temp)

    def reduce(self, callback, initial=0):
        """
        performing some computation on a iterable and returning the result.
        :param callback: function take 2 arguments
        :param initial: starting computation point
        :return: result
        """
        result = initial
        for num in self.iterable:
            result = callback(result, num)
        return result

    def sort(self, key=None, reversed=False):
        """
        sort the iterable by a key and optional to reversed the iterable
        :exception if the function get reversed without the key ',' must be sent also, telling the function there
        is a second parameter.
        :param key:(Optional) - Function that serves as a key for the sort comparison
        :param reversed:(Optional) - If true, the sorted list is reversed (or sorted in Descending order)
        :return: A sorted list from the given iterable
        """
        return Collection(
            sorted(self.iterable, key=lambda func: func[key], reverse=reversed)) if key is not None else Collection(
            sorted(self.iterable, key=None, reverse=reversed))

    def set(self, position, value):
        """
        set a new value to a position asked. if the position is valid
        :param position: the place where the new value should be
        :param value:New value
        :return:New Collection if the position is valid else the new Collection with the original iterable
        """
        return Collection(list(self.iterable[:position]) + list(value) + list(self.iterable[position + 1:]))

    def pluck(self, key):
        """
        If the internal elements are not dictionaries, then no action should
        be taken and a copy of the current collection should be returned
        :param key:
        :return: A new Collection with the only the key of each element
        """
        return Collection(self.iterable) if type(self.iterable) is not type(dict) else Collection(
            map(lambda func: func[key], self.iterable))

    def values(self):
        """
        return the elements in the iterable
        :return: all elements in the iterable else None
        """
        return Collection(self.iterable) if type(self.iterable) not in (dict, None) else None

    def unique(self):
        """
        should return a new Collection with only unique items.
        :return: set of all element in the iterable
        """
        return Collection(set(self.iterable))

    def tap(self, callback):
        """
        should pass each element of the collection by-value to a callback function
        :param callback: function that given
        :return:the result for each value
        """
        for index in range(len(self.iterable)):
            callback(self.iterable[index])

    def __getitem__(self, position):
        """

        :param position:
        :return:
        """
        return self.iterable[position] if position < len(self.iterable) else None

    def __add__(self, other):
        """

        :param other:
        :return:
        """
        return list(self.iterable) + list(other)

    def __sub__(self, other):
        """

        :param other:
        :return:
        """
        return list(self.iterable) - list(other)

    def __len__(self):
        """

        :return:
        """
        return len(self.iterable)

    def __contains__(self, element):
        """

        :param element:
        :return:
        """
        return True if element in self.iterable else False

    def __eq__(self, other):
        """

        :param other:
        :return:
        """
        return True if self.iterable == other.iterable else False

    def __ne__(self, other):
        """

        :param other:
        :return:
        """
        return not (self.__eq__(other))

    def __str__(self):
        """

        :return:
        """

        return 'Collection{}'.format(tuple(self.iterable))

    def __repr__(self):
        """

        :return:
        """
        return 'Collection' + (self.__str__())
