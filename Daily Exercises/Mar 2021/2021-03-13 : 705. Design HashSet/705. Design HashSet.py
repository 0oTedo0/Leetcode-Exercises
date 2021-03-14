class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base=1021
        self.getkey=lambda x:x%self.base
        self.l=[list()]*self.base


    def add(self, key):
        if not self.contains(key):
            self.l[self.getkey(key)].append(key)

    def remove(self, key):
        if self.contains(key):
            self.l[self.getkey(key)].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        """
        return (key in self.l[self.getkey(key)])



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

"""
Since it does not put a constraint on space complexity,
there is another method which requires more space but performs fast.
"""

"""
class MyHashSet:

    def __init__(self):
        # Initialize your data structure here.
        self.l=[False]*int(1e6+1)


    def add(self, key):
        self.l[key]=True

    def remove(self, key):
        self.l[key]=False

    def contains(self, key):
        # Returns true if this set contains the specified element
        return self.l[key]
"""
