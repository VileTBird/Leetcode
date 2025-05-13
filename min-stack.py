"""
Another pitfall once i have the naive solution i shouldnt be satisfied

this is a decent design problem. initially i just used the existing stack data structure but the self.minval method makes it o(n) for getmin
i think using deltas would work, would be much more commplex and its too early for me to write delta logic lol

next theres the optimal solution, its reall not that complex its basically o(2n)  space or o(n) cus we really dont care abt tha tanyways, the thing is 
we could make it o(n) wit deltas anyways regqardless.. the solution by itself is pretty simlke. for each push, we store the corresponding min value by comparing
current minvalue from on top of the min stack with the current val, then we store a duplicate or the val as new min, so when we pop  we pop in parallel,
we maintain minimum for all points in the array easy


"""


class MinStack:

    def __init__(self):
        self.array = []
        self.minVal = None

    def push(self, val: int) -> None:
        self.array.append(val)
        
        if self.minVal is None:
            self.minVal = val
        
        if val < self.minVal:
            self.minVal = val

    def pop(self) -> None:
        poppedElement = self.array.pop(len(self.array) - 1)
        if self.minVal not in self.array:
            self.minVal = None
            for i in self.array:
                if self.minVal is None:
                    self.minVal = i
                if i < self.minVal:
                    self.minVal = i

    def top(self) -> int:
        return self.array[len(self.array) - 1]
        

    def getMin(self) -> int:
        return self.minVal
        

class MinStack:

    def __init__(self):
        self.array = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.array.append(val)
        
        if self.minStack is None:
            self.minStack.append(val)
            return
        
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)


    def pop(self) -> None:
        self.array.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.array[len(self.array) - 1]
        

    def getMin(self) -> int:
        return self.minStack[len(self.array) - 1]
        
