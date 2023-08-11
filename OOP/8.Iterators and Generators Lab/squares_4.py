# def squares(n): # suboptimal
#     for i in range(1,n+1):
#         yield i * i
#         i += 1

def squares(n):
    num = 1
    while num <= n:
        yield num * num
        num += 1


print(list(squares(5)))
