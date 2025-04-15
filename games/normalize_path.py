# Normalize path problem:
# Pseudocode - Whenever I see '..', I'll delete the previous element, because parent of a child neutralizes.
# This will hopefully give me a normalized path
class PathError(Exception):
    pass


class Stack:
    def __init__(self, maxsize=None, elements=[],):
        self.maxsize, self.elements = maxsize, elements
        self.size = len(elements)
        if maxsize:
            assert self.size <= maxsize

    def push(self, element):
        if not self.isfull():
            self.elements.append(element)
            self.size += 1
            return
        return -1

    def pop(self):
        if not self.isempty():
            self.elements.pop()
            self.size -= 1
            return
        raise PathError("Invalid path")

    def peek(self):
        if self.size >= 1:
            return self.elements[-1]
        return -1

    def isfull(self):
        if self.maxsize:
            return self.size >= self.maxsize
        return None

    def isempty(self):
        return self.size == 0

    def __repr__(self):
        return f"A stack, of size {self.size}{f', max-size {self.maxsize}' if self.maxsize else ''}, elements: {self.elements}"


def path_normalization(path=None, delimiter='/'):
    path = path or input("Enter the path: ").strip().split('/')
    path_stack = Stack()
    for element in path:
        if element == '..':
            path_stack.pop()
            continue
        path_stack.push(element)
    return delimiter.join(path_stack.elements)


print(path_normalization())
