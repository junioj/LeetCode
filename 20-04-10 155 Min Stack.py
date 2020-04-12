class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.y=[]

    def push(self, x: int) -> None:
        self.y.append(x)

    def pop(self) -> None:
        del self.y[-1]

    def top(self) -> int:
        return self.y[-1]

    def getMin(self) -> int:
        return min(self.y)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()