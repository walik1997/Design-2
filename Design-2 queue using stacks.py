# Time Complexity :O(1)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode :yes
# Any problem you faced while coding this : Tried using reverse function which returned an itterator that did not support indexing. 


# Your code here along with comments explaining your approach: First I appended the values in stack1
# and popped from stack 1 to append in stack 2 i.e reversing the order.  

class MyQueue:

    def __init__(self):
        self.stack_1=[]
        self.stack_2=[]

    def push(self, x: int) -> None:
        self.stack_1.append(x)
    def pop(self) -> int:
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()
    def peek(self) -> int:
        if not self.stack_2 :
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        display = self.stack_2[-1]
        return display
    def empty(self) -> bool:
        if not self.stack_2 and not self.stack_1:
            return True
        else:
            return False   
