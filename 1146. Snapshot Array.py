
"""
The solution is to use a dictionary.

The dictionary maps each index to a list.

The list contains all snap_id's where the index was changed and the value it was changed to.

We then do a binary search on the list every time get is called to find the lowest snap_id more than or equal to the parameter.

"""

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0] * length
        self.D = {i:[] for i in range(length)}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        D = self.D
        snap_id = self.snap_id

        if len(D[index]) == 0:
            D[index].append((snap_id, val))
        else:
            last = D[index][-1]
            if last[0] == snap_id:
                D[index][-1] = (snap_id, val)
            else:
                D[index].append((snap_id, val))
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        def bs(arr, snap_id):
            l,r = 0, len(arr) - 1
            while l <= r:
                mid = (r - l) // 2 + l

                if arr[mid][0] > snap_id:
                    r = mid - 1
                elif arr[mid][0] < snap_id:
                    l = mid + 1
                else:
                    return arr[mid][1]
            if l == 0:
                return 0
            else:
                return arr[l - 1][1]
        
        D = self.D
        return bs(D[index], snap_id)
            


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)