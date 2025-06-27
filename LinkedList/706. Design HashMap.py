class MyHashMap:

    def __init__(self):
        self.hm = Counter() 

    def put(self, key: int, value: int) -> None:
        self.hm[key] = value

    def get(self, key: int) -> int:
        return self.hm[key] if key in self.hm else -1

    def remove(self, key: int) -> None: 
        del self.hm[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)