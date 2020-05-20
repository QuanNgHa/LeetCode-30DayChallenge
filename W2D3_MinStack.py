class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.minStack.append(x)
        if x < self.min:
            self.min = x
    # Methods pop, top and getMin operations
    # will always be called on non-empty stacks.

    def pop(self):
        """
        :rtype: None
        """
        if self.minStack:
            item = self.minStack.pop()

            if item == self.min:
                self.min = float('inf')
                for i in self.minStack:
                    if i < self.min:
                        self.min = i

    def top(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.min
        else:
            return None


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()  # return -3
    minStack.pop()
    print(minStack.top())  # return 0
    print(minStack.getMin())  # return -2
    minStack.pop()
    minStack.pop()
    minStack.pop()
    print(minStack.getMin())
