# sets implementation
colors = {'red', 'green', 'blue'}
colors.add('yellow')
print(colors) # {'red', 'green', 'blue', 'yellow'}
colors.remove('red') # remove element
print(colors) # {'green', 'blue', 'yellow'}
print('red' in colors) # False
print('green' in colors) # True
colors.clear() # remove all elements
print(colors) # set()
# set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b) # union {1, 2, 3, 4, 5, 6}
print(a & b) # intersection {3, 4}
print(a - b) # difference {1, 2}
print(a ^ b) # symmetric difference {1, 2, 5, 6}
# set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # {'r', 'd'}
# frozenset
a = frozenset([1, 2, 3, 4]) # immutable set
print(a) # frozenset({1, 2, 3, 4})
# a.add(5) # AttributeError: 'frozenset' object has no attribute 'add'
# a.remove(1) # AttributeError: 'frozenset' object has no attribute 'remove'
# a.clear() # AttributeError: 'frozenset' object has no attribute 'clear'
b = frozenset([3, 4, 5, 6])
print(a | b) # frozenset({1, 2, 3, 4, 5, 6})
print(a & b) # frozenset({3, 4})
print(a - b) # frozenset({1, 2})
print(a ^ b) # frozenset({1, 2, 5, 6})
# a |= b # TypeError: unsupported operand type(s) for |=: 'frozenset' and 'frozenset'
# a &= b # TypeError: unsupported operand type(s) for &=: 'frozenset' and 'frozenset'
# a -= b # TypeError: unsupported operand type(s) for -=: 'frozenset' and 'frozenset'
# a ^= b # TypeError: unsupported operand type(s) for ^=: 'frozenset' and 'frozenset'
# a = {x for x in 'abracadabra' if x not in 'abc'} # TypeError: unhashable type: 'set'
# a = frozenset({x for x in 'abracadabra' if x not in 'abc'}) # TypeError: unhashable type: 'set'
# frozenset comprehension is not possible
