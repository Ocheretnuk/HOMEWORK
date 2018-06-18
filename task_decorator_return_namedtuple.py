from collections import namedtuple

def return_namedtuple(*names):
	def dec(func):
		def wr(*args, **kwargs):
			result = func(*args, **kwargs)
			if isinstance(result, tuple):
				named_tuple = namedtuple('namedtuple', list(names))
			return named_tuple(*result)
		return wr
	return dec