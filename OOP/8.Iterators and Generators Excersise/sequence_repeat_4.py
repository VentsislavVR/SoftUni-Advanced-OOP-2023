class sequence_repeat:
    def __init__(self, text, num):
        self.text = text
        self.num = num
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.num -1 :
            raise StopIteration

        self.idx += 1

        return self.text[self.idx % len(self.text)]


result = sequence_repeat('abc', 5)
for item in result:
 print(item, end ='')