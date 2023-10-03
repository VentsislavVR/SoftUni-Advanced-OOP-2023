from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

points = {
    150: "Doll",
    250:"Wooden train",
    300:"Teddy bear",
    400:"Bicycle",
}
presents ={}

while materials and magic:
    total_magic = materials[-1] * magic[0]

    if total_magic in points:
        new_present = points[total_magic]
        if new_present not in presents:
            presents[new_present] = 0
        presents[new_present] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())

    elif total_magic > 0:
        magic.popleft()
        materials.append(materials.pop() + 15)
    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()

if ('Doll' in presents and 'Wooden Train' in presents) or ('Teddy bear' in presents and 'Bicycle' in presents ):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key,value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")


