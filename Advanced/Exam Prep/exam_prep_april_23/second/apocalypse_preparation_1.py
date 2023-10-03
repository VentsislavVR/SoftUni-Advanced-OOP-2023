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
both_empty = False
if not medicament and not textiles:
    both_empty = True

    print('Textiles and medicaments are both empty.')

if not textiles:
    if both_empty == False:
        print("Textiles are empty.")
if not medicament:
    if both_empty == False:
        print("Medicaments are empty.")

for key,value in sorted(meds_count.items(),key=lambda x:(-x[1],x[0])):
    if value:
        print(f"{key} - {value}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")

if medicament:
    print(f"Medicaments left: {', '.join([str(x) for x in medicament][::-1])}")

