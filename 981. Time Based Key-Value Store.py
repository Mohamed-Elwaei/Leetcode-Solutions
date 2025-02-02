class TimeMap:

    def __init__(self):
        self.D = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.D:
            self.D[key] = []
        self.D[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.D or len(self.D[key]) == 0:
            return ''

        values = self.D[key]
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        # If r is -1, it means all timestamps are greater than the given timestamp
        if r == -1:
            return ''
        return values[r][1]

# Example of usage:
# obj = TimeMap()
# obj.set("foo", "bar", 1)
# print(obj.get("foo", 1))  # Outputs "bar"
# print(obj.get("foo", 3))  # Outputs "bar"
# obj.set("foo", "bar2", 4)
# print(obj.get("foo", 4))  # Outputs "bar2"
# print(obj.get("foo", 5))  # Outputs "bar2"