from collections import OrderedDict

# hash table implementation
data = {}
data['a'] = 1 # key-value pair
data['b'] = 2 
data['c'] = 3
print(data) # {'a': 1, 'b': 2, 'c': 3}
print(data['a']) # 1
print(data['b'])
print(data['c'])
print(data.keys()) # dict_keys(['a', 'b', 'c']) - dict_keys is a view object
print(data.values()) # dict_values([1, 2, 3]) - dict_values is a view object
print(data.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)]) - dict_items is a view object

# ordered dictionary implementation - maintains the order of insertion of keys
data2 = OrderedDict()
data2['a'] = 1
data2['b'] = 2
data2['c'] = 3
print(data2) # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
