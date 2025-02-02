class BrowserHistory:

    def __init__(self, homepage: str):
        self.before = deque([])
        self.after  = deque([]) 
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.after.clear()
        self.before.append(url)

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.before) - 1)
        for _ in range(steps):
            self.after.appendleft(self.before.pop())
        return self.before[-1]

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.after))
        for _ in range(steps):
            self.before.append(self.after.popleft())
        return self.before[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)