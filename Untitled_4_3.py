class Collection(object):
	def	__init__(self, iterable=None):
		self.iterable = None if type(iterable) in (dict ,None) else iterable
	def first(self):
		 self.iterable[0]
	def last(self):
		return self.iterable[len(self.iterable-1)]
	def take(self, amount):
			return Collection((self.iterable[:amount]))
	def append(self, *elements):
		elements=type(self.iterable)(elements)
		return None if type(iterable) in (dict ,None) else Collection((self.iterable+elements))	
	def prepend(self, *elements):
		elements=type(self.iterable)(elements)
		return None if type(iterable) in (dict ,None) else Collection((elements+self.iterable))
	def filter(self, *callbacks):	
		for item in callbacks:
			self.iterable=filter(item, self.iterable)
		return Collection(self.iterable)
	def map(self, *callbacks):
		for item in callbacks:
			self.iterable = map(item,self.iterable)
		return Collection(self.iterable)
	def sort(self, key=None, reversed=False):
		return Collection(sorted(self.iterable, key, reversed))
	def __eq__(self, other):
		return True if self.iterable==other.iterable else False
	def __ne__(self, other):
		return (not (self.__eq__(other)))
	def __str__(self):
		return 'Collection{}'.format(tuple(self.iterable))
	def __repr__(self):
		return 'Collecton' + (self.__str__())
	def reduce(self, callback, initial=0):
		result=initial
		for num in self.iterable:
			result=callback(result, num)
		return (result)
	def sort(self, key=None, reversed=False):
		return Collection (sorted(self.iterable, key=lambda func: func[key], reverse=reversed))if key != None else Collection (sorted(self.iterable, key= None, reverse=reversed))
	def set(self, position, value):
		return Collection(self.iterable[:position]+(value)+self.iterable[position+1:])
	def pluck(self, key):
		return Collection(map(lambda func: func[key], self.iterable))
	def values(self):
		return Collection(self.iterable) if type(iterable) not in (dict ,None) else None
	def unique(self):
		return Collection(set(self.iterable))
	def tap(self, callback):
		for index in range(len(self.iterable)):
			callback(self.iterable[index])	
c = Collection('HELLO')
c.tap(print)

