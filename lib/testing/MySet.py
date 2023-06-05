class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return [value] in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary = {}
        return self
    
    def __str__(self):
        return f"MySet: {', '.join(str(value) for value in self.dictionary.keys())}"
    

set = MySet([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

print(set)  

set.add(4)
print(set)  

set.delete(2)
print(set)  

print(set.has(3))  
print(set.has(5))  

print(set.size())  

set.clear()
print(set)  