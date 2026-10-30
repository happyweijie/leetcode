class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        # move elements from back stack to front stack
        # if front is empty
        if not self.front:
            self.shift_from_back_to_front()
        return self.front.pop()

    def peek(self) -> int:
        # move elements from back stack to front stack
        # if front is empty
        if not self.front:
            self.shift_from_back_to_front()
        return self.front[-1]

    def empty(self) -> bool:
        return not self.front and not self.back

    def shift_from_back_to_front(self) -> None:
        while self.back:
            self.front.append(self.back.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()




