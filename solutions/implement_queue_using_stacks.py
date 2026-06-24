# Question number: 232
# Level: easy
# Author: Naama Tzadok
# Date: Jun 24, 2026 10:08


class MyQueue:

    def __init__(self):
        self.tail = []
        self.head = []

    def push(self, x: int) -> None:
        self.tail.append(x)
        
    def pop(self) -> int:
        if self.head:
            return self.head.pop()
        while self.tail:
            self.head.append(self.tail.pop())
        return self.head.pop()

    def peek(self) -> int:
        if self.head:
            return self.head[-1]
        if self.tail:
            return self.tail[0]

    def empty(self) -> bool:
        return self.tail == [] and self.head == []

# Time Complexity: O(1) (amortized)
# Space Complexity: O(1)

