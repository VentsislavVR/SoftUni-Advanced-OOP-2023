import sys
from collections import deque
from io import StringIO

test_input_1 = '''10 16 13 25
12 11 8
'''
test_input_2 = '''10 14 22 4 5
11 16 17 11 1 8
'''

test_input_3 = '''5 6 7
2 1 5 7 5 3
'''

sys.stdin = StringIO(test_input_1)
from collections import deque

elf_energies = deque([int(e) for e in input().split()])
boxes = [int(m) for m in input().split()]

# toys_made = 0
# energy_spent = 0
# turns_count = 0
#
# while elf_energies and boxes:
#
#     while elf_energies and elf_energies[0] < 5:
#         elf_energies.popleft()
#
#     if not elf_energies:
#         break
#     turns_count += 1
#     elf_energy = elf_energies.popleft()
#     box = boxes.pop()
#
#     if turns_count % 15 == 0 and (2 * box) <= elf_energy:
#         toys_made += 0
#         energy_spent += 2* box
#         elf_energies.append(elf_energy-(2*box)+0)
#
#     elif turns_count % 5 == 0 and box <= elf_energy:
#         toys_made += 0
#         energy_spent += 1*box
#         elf_energies.append(elf_energy - (1*box)+0)
#
#
#     elif turns_count % 3 == 0 and (2 * box) <= elf_energy:
#         toys_made += 2
#         energy_spent += 2* box
#         elf_energies.append(elf_energy - (2 * box) + 1)
#
#     elif box <= elf_energy and turns_count %3 > 0:
#         toys_made += 1
#         energy_spent += 1 * box
#         elf_energies.append(elf_energy - (1 * box) + 1)
#     else:
#         boxes.append(box)
#         elf_energies.append(elf_energy*2)

toys_made = 0
energy_spent = 0
turns_count = 0

while elf_energies and boxes:

    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break
    elf_energy = elf_energies.popleft()
    box = boxes.pop()


    turns_count += 1

    toys_to_be_created_count = 1
    energy_to_be_spent= box
    energy_increase_factory = 1

    if turns_count % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2
    if turns_count % 5 == 0:
        toys_to_be_created_count = 0
        energy_increase_factory = 0

    if energy_to_be_spent <= elf_energy:
        toys_made += toys_to_be_created_count
        energy_spent += energy_to_be_spent
        elf_energies.append(elf_energy-energy_to_be_spent + energy_increase_factory)

    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2)


print(f"Toys: {toys_made}")
print(f"Energy: {energy_spent}")
if elf_energies:
    print(f"Elves left: {', '.join(str(x) for x in elf_energies)}")
if boxes:
    print(f"Boxes left: {', '.join(str(x) for x in boxes)}")
