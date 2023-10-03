from collections import deque

colors_string = deque(input().split())

main_colors = ["red", "yellow", "blue"]

second_colors = {
    "orange": ['red', 'yellow'],
    "purple": ['red', 'blue'],
    "green": ['yellow', 'blue'],
}

collected_colors = [

]
while colors_string:
    first_str = colors_string.popleft()
    last_str = colors_string.pop() if colors_string else ''

    if first_str + last_str in main_colors or first_str + last_str in second_colors:
        collected_colors.append(first_str + last_str)
    elif last_str + first_str in main_colors or last_str + first_str in second_colors:
        collected_colors.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            colors_string.insert(len(colors_string) // 2, first_str[:-1])
        if len(last_str) > 1:
            colors_string.insert(len(colors_string) // 2, last_str[:-1])

for color in collected_colors:
    if color in second_colors:
       for el in second_colors[color]:
           if el not in collected_colors:
               collected_colors.remove(color)
               break
print(collected_colors)