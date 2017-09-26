

# defaultdict
give a default value

```Python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

default_d = defaultdict(list) # define a default data type
for color, num in s:
    default_d[color].append(num)

# equlvent to

dic = {}
for color, num in s:
    dic[color] = dic.get(color, []) + [num]
```

# deque
Deques are a generalization of stacks and queues
Thread safe
set maxlen when create, to control deque size
Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.
```Python
deq = deque(maxlen=5)
```

# namedtuple
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.
Its like a easy way to define a class

```Python
Point = namedtuple('Point', ['x','y'])
p = Point(11,22)
p.x # 11
p.y # 22
p.__doc__ = 'doc'
p.x.__doc__ = 'x doc'
```

# OrderedDict
just like regular dictionaries but they remember the order that items were inserted.

# ChainMap
groups multiple dicts or other mappings together to create a single, updateable view
Lookups search the underlying mappings successively until a key is found

```Python
a = {'a':12, 'b':22, 'c': 33}
b = {'a':55, 'd':120}
c = ChainMap(a,b)
c['a'] # 12
c['d'] # 120
c['w'] # raise KeyError(key)
```

# Counter
It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

Counts are allowed to be any integer value including zero or negative counts.

# UserList
TODO
# UserDict
TODO
# UserString
TODO
