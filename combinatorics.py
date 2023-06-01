from copy import copy
from typing import Any
from abc import ABC

class BasicStructure(ABC):
    def __str__(self) -> str:
        return str(self._data)
    
    def __bool__(self):
        return len(self._items) > 0
    
    def __getitem__(self, key):
        if key >= self._end or key < -1 * self._end:
            raise IndexError("index out of range")
        return self._data[key]
    
    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._iterator >= self._end:
            raise StopIteration
        else:
            self._iterator += 1
            return self._data[self._iterator - 1]
    
    def __contains__(self, item):
        for permutation in self._data:
            if permutation == item:
                return True
        return False

class Permutations(BasicStructure):
    def __init__(self, source=[]):
        self._iterator = 0
        if len(source) < 2:
            self._items = copy(source)
            self._data = [copy(source)]
        else:
            self._items = sorted(copy(source))
            self._data = []
            for i in range(len(self._items)):
                reccache = Permutations([*self._items[:i], *self._items[i + 1:]])
                for item in reccache._data:
                    permutation = [self._items[i], *item]
                    if permutation in self._data:
                        break
                    else:
                        self._data.append(permutation)
        self._end = len(self._data)                        
        if type(source) == str:
            for i in range(len(self._data)):
                self._data[i] = ''.join(self._data[i])

class Arrangements(BasicStructure):
    def __init__(self, source=[], k=0):
        if len(source) < k:
            raise ValueError("incorrect values for Combinations. It must be: n = len(source) >= k")
        self._iterator = 0
        if k == 0:
            self._items = copy(source)
            self._data = [[]]
        elif k == 1:
            self._items = copy(source)
            self._data = [[item] * k for item in self._items]
        elif len(source) < 2:
            self._items = copy(source)
            self._data = [copy(source)]
        elif len(source) == k:
            self._items = copy(source)
            self._data = [sorted(copy(source))]
        else:
            self._items = sorted(copy(source))
            self._data = []
            reccache = Arrangements(self._items[1:], k - 1)
            for arrangement in reccache:
                if not [self._items[0], *arrangement] in self._data:
                    self._data.append([self._items[0], *arrangement])
            reccache = Arrangements(self._items[1:], k)
            for arrangement in reccache:
                if not arrangement in self._data:
                    self._data.append(arrangement)
        self._end = len(self._data)                        
        if type(source) == str:
            for i in range(len(self._data)):
                self._data[i] = ''.join(self._data[i])

class Combinations(BasicStructure):
    def __init__(self, source=[], k=0):
        if len(source) < k:
            raise ValueError("incorrect values for Combinations. It must be: n = len(source) >= k")
        self._iterator = 0
        if k == 0:
            self._items = copy(source)
            self._data = [[]]
        elif k == 1:
            self._items = copy(source)
            self._data = [[item] * k for item in self._items]
        elif len(source) < 2:
            self._items = copy(source)
            self._data = [copy(source)]
        else:
            self._items = sorted(copy(source))
            self._data = []
            for i in range(len(self._items)):
                reccache = Combinations([*self._items[:i], *self._items[i + 1:]], k - 1)
                for item in reccache._data:
                    combination = [self._items[i], *item]
                    if combination in self._data:
                        break
                    else:
                        self._data.append(combination)
        self._end = len(self._data)                        
        if type(source) == str:
            for i in range(len(self._data)):
                self._data[i] = ''.join(self._data[i])