from random import randint
class RandomizedSet:
 

    def __init__(self):
        self.arr = []
        self.mapping = {}

    def insert(self, val: int) -> bool:
        arr = self.arr
        mapping = self.mapping

        
        if val in mapping:
            return False


        arr.append(val)
        mapping[val] = len(arr) - 1
        return True


    def remove(self, val: int) -> bool:
        arr = self.arr
        mapping = self.mapping

        if val not in mapping:
            return False
        
        prev = mapping[val]
        arr[prev] = arr[len(arr) - 1]
        mapping[arr[prev]] = prev
        arr.pop()
        del mapping[val]
        return True

    def getRandom(self) -> int:
        arr = self.arr
        index = randint(0, len(arr) - 1)


        return arr[index]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()