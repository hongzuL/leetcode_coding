# 155. Min Stack

class MinStack:
    
    def __init__(self):
        self.min_stack = list()
        self.min_vals = [2**31]

    def push(self, val):
        self.min_stack.append(val)
        if val <= self.min_vals[-1]:
            self.min_vals.append(val)
        else:
            for i in range(len(self.min_vals)):
                if val >= self.min_vals[i]:
                    self.min_vals.insert(i,val)
                    break

    def pop(self):
        self.min_vals.pop(self.min_vals.index(self.top()))
        self.min_stack.pop()
        
    def top(self):
        return self.min_stack[-1]

    def getMin(self):
        return self.min_vals[-1]

def main(operations, data):
    for i in range(len(operations)):
        if operations[i] == "MinStack":
            obj = MinStack()
        elif operations[i] == "push":
            obj.push(data[i][0])
        elif operations[i] == "pop":
            obj.pop()
        elif operations[i] == "top":
            the_top = obj.top()
            print(the_top)
        elif operations[i] == "getMin":
            the_min = obj.getMin()
            print(the_min)


a = ["MinStack","push","push","push","push","pop","getMin","pop","getMin","pop","getMin"]
b = [[],[512],[-1024],[-1024],[512],[],[],[],[],[],[]]

main(a,b)