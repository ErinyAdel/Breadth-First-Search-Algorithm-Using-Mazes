# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 22:38:30 2022
@author: Eriny
"""


class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return not self.items
        #return len(self.items) == 0
    
    def enqueue(self, val):
        self.items.append(val)
        
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
    
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.isEmpty())
    q.enqueue("A")
    q.enqueue("D")
    q.enqueue("F")
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())
    print(q)
    
            