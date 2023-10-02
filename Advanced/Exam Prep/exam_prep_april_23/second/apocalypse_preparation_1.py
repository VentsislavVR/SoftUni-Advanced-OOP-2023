from collections import deque


textiles = deque([int(x) for x in input().split()])
medicament = deque([int(x) for x in input().split()])
meds = {
    40:'Bandage',
    30:'Patch',
    100:'MedKit'
}
meds_count = {
    'Bandage': 0,
    'Patch': 0,
    'MedKit': 0
}

while textiles and medicament:
    textile = textiles.popleft()
    med = medicament.pop()
    current_sum = textile + med
    if current_sum not in meds and current_sum < 100:
        medicament.append(med + 10)

        continue
    if current_sum in meds:
        meds_count[meds[current_sum]] +=1
    if current_sum > 100:
        meds_count['MedKit'] +=1
        medicament[-1] += current_sum - 100




if not medicament and not textiles:
    print('Textiles and medicaments are both empty')

if not textiles:
    print("Textiles are empty.")
else:
    print(f"Textiles: {textiles}")
if not medicament:
    print("Medicaments are empty.")
else:
    print(f"Medicaments: {medicament}")







