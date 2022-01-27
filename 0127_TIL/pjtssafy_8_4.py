class StackClass:

    def __init__(self, stack):
        self.stack = stack

    def empty(self):
        if self.stack == []:
            return True
        else:
            return False

    def top(self):
        if self.stack == []:
            return None
        else:
            return self.stack[-1]

    def pop(self):
        if self.stack == []:
            return None
        else:
            ans = self.stack.pop(-1)
            return ans

    def push(self, adding):
        self.stack.append(adding)

    def __repr__(self):
        return self.stack

a = [1,2,3,4,5,6,7]
aa = StackClass(a)
print(aa.empty())
print(aa.top())
print(aa.pop())
print(aa.top())
print(aa.__repr__())
aa.push(9)
print(aa.top())