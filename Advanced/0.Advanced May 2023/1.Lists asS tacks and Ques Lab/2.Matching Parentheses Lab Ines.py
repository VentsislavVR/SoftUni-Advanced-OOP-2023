# stack_parant = []
#
# text = input()
#
# for index in range(len(text)):
#     ch = text[index]
#     if ch == "(":
#         stack_parant.append(index)
#     elif ch == ")":
#         start_position = stack_parant.pop()
#         end_position = index+1
#         print(text[start_position:end_position])

expression = input()

stack = []

for index in range(len(expression)):
    if expression[index] == '(':
        stack.append(index)
    elif expression[index] == ')':
        last_par = stack.pop()
        print(expression[last_par:index+1])