class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = [iter(nested_list)]
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.stack:
            try:
                element = next(self.stack[-1])
                if isinstance(element, list):
                    self.stack.append(iter(element))
                else:
                    return element
            except StopIteration:
                self.stack.pop()
        raise StopIteration