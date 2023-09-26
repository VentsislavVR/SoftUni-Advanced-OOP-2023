line = input().split('|')


sub_list = []

for i in line[::-1]:
    sub_list.extend(i.split())

print(*sub_list)