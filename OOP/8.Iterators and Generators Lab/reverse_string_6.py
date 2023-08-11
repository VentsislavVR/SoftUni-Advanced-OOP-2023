def reverse_text(text):
    cur_ind = len(text) -1
    end = 0
    while cur_ind >= end:
        yield text[cur_ind]
        cur_ind -= 1





for char in reverse_text("step"):
    print(char, end='')