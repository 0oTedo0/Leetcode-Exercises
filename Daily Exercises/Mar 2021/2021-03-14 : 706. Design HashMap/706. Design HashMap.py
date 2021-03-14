class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base=1021
        self.get_key=lambda x: x%self.base
        self.l=[list()]*self.base

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        for item in self.l[self.get_key(key)]:
            if item[0]==key:
                item[1]=value
                break
        else:
            self.l[self.get_key(key)].append([key,value])


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for item in self.l[self.get_key(key)]:
            if item[0]==key:
                return item[1]
        return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for item in self.l[self.get_key(key)]:
            if item[0]==key:
                self.l[self.get_key(key)].remove(item)
                break



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
Since it does not put a constraint on space complexity, there is another method which requires more space but performs fast
"""
"""
class MyHashMap:

    def __init__(self):
        # Initialize your data structure here.
        self.l=[-1]*int(1e6+1)

    def put(self, key, value):
        # value will always be non-negative.
        self.l[key]=value


    def get(self, key):
        # Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        return self.l[key]


    def remove(self, key):
        # Removes the mapping of the specified value key if this map contains a mapping for the key
        self.l[key]
"""
