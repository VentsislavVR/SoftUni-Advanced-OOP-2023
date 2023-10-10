from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

items = {
    range(400,499+1): ['Diamond Jewellery',0],
    range(300,399+1): ['Gold',0],
    range(200,299+1): ['Porcelain Sculpture',0],
    range(100,199+1): ['Gemstone',0],
}


while materials and magic:
    cur_material = materials[-1]
    cur_magic = magic[0]

    party_trick = cur_material + cur_magic
    if party_trick > 499:
        party_trick /= 2

    if party_trick < 100:
        if party_trick % 2 == 0:
            cur_material *= 2
            cur_magic *= 3
            party_trick = cur_material + cur_magic
        else:
            party_trick *= 2

    for pt in items.keys():
        if round(party_trick) in pt:
            items[pt][1] += 1
            break
    materials.pop()
    magic.popleft()
result = {}
wedding_gift_pairs = set()
success_pair = False

for item,value in sorted(items.items(),key=lambda x:x[1]): # didn't think the name trough lol
    final_item = value[0]
    count = value[1]
    result[final_item] = count
    if result[final_item] >0:
        wedding_gift_pairs.add(final_item)
condition1_set = {'Gemstone', 'Porcelain Sculpture'}
condition2_set = {'Diamond Jewellery', 'Gold'}


if (condition1_set.issubset(wedding_gift_pairs)) or (condition2_set.issubset(wedding_gift_pairs)):
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for item, count in result.items():
    if count > 0:
        print(f'{item}: {count}')
#
# print(*{f"Materials left: {', '.join(str(x) for x in materials)}"} if materials else '')
# print(*{f"Magic left: {', '.join(str(x) for x in magic)}"} if magic else '')
# print('\n'.join([f'{x}: {y}' for x, y in result.items() if y > 0]))


