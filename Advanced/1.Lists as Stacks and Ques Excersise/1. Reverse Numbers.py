original_string = 'I Love Python'

s = []

for c in original_string:
    s.append(c)

rev_str = ''

while s:
    rev_str +=s.pop()

print(rev_str)