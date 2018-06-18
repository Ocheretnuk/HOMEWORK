
class LinkedList(object):

    def __init__(self, *args):
        self.list = args
        self.index = 0


    def add(self, value):
        self.list = self.list + (value,)


    def insert(self, index, value):
        self.list = self.list[:index] + (value,) + self.list[index:]


	def get(self, index):
		if index >= self._length:
			raise IndexError()
		i = 0
		last = self._head
		while i < index:
			last = last._next
			i+=1
		return last._value


	def remove(self, value):
		node = self._head;
		i = 0
		while node:
			if node._value == value:
				self.remove_at(i)
			node = node._next
			i+=1
		return self


    def remove_at(self, index):
        if index >= len(self.list):
            raise IndexError
        element = self.list[index]
        self.list = self.list[:index] + self.list[index + 1:]
        return element


    def clear(self):
        self.list = ()


    def contains(self, value):
        if value in self.list:
            return True
        else: return False


    def len(self):
        return len(self.list)


	def is_empty(self):
		return not bool(self._head)



    def __iter__(self):
        return self


	def __next__(self):
		if not self._iter:
			self.__iter__()
		return next(self._iter)

      