from time import time
from random import randint as ri
from inspect import getsource as gs


# algorithm - input*(length of input) - series of 1s depending on the length of input
# solution
solution=lambda n:n*(x:=len(str(n)))-int('1'*x)


def length(func):
	"""returns the length of <func>"""
	func_length = len(gs(func))
	return func_length - 1


def timer(func):
	"""returns the amount of time it takes to run <func>"""
	ts = time()
	for i in range(1, 1000000):
		func(ri(1, 100000))
	return time() - ts


print(f"solution: {timer(solution)}")
print(f"solution length: {length(solution)}")
