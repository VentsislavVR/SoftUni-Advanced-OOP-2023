def genrange(start, end):
    curr_num = start
    while curr_num <= end:
        yield curr_num
        curr_num += 1


print(list(genrange(1, 10)))
