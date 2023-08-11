from typing import Sequence, Any


class reverse_iter:
    def __init__(self, collection: Sequence):
        self.collection = collection
        self.start_index = len(self.collection) - 1
        self.end_index = 0
        self.current_index = self.start_index + 1

    def __iter__(self):
        return self # reversed(self.collection)

    def __next__(self) -> Any:
        self.current_index -= 1
        if self.current_index < self.end_index:
            raise StopIteration
        return self.collection[self.current_index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
