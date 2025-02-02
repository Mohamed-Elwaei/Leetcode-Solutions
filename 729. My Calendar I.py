class MyCalendar:

    def __init__(self):
        self.arr = []


    def book(self, start: int, end: int) -> bool:
        arr = self.arr

        for start2, end2 in arr:
            if start2 <= start <= (end2 - 1) or start <= start2 <= (end - 1):
                return False
        arr.append([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)