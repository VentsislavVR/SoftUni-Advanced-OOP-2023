
from collections import deque

bomb_effect =deque([int(x) for x in input().split(',')])
bomb_casing = [int(x) for x in input().split(',')]


bombs={120:"Smoke Decoy Bombs",
       60:"Cherry Bombs",
       40:"Datura Bombs"
       }
pouch = {
       "Datura Bombs": 0,
       "Cherry Bombs": 0,
       "Smoke Decoy Bombs":0}


while bomb_effect and bomb_casing:
       pouch_is_full = False
       if all(value >= 3 for value in pouch.values()):
              pouch_is_full = True
              print("Bene! You have successfully filled the bomb pouch!")
              break
       cur_effect = bomb_effect.popleft()
       cur_casing = bomb_casing.pop()

       cur_sum = cur_effect + cur_casing

       if cur_sum == 120:
              pouch["Smoke Decoy Bombs"] += 1
              continue
       elif cur_sum ==60:
              pouch["Cherry Bombs"] +=1
       elif cur_sum == 40:
              pouch["Datura Bombs"] += 1

       else:
              cur_casing -= 5
              bomb_casing.append(cur_casing)
              bomb_effect.appendleft(cur_effect)


if not pouch_is_full:
       print("You don't have enough materials to fill the bomb pouch.")
if bomb_effect:
       print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}")
else:
       print("Bomb Effects: empty")
if bomb_casing:
       print(f"Bomb Casings: {','.join(str(x) for x in bomb_casing)}")
else:
       print("Bomb Casings: empty")

result = []
for key,value in sorted(pouch.items()):
       result.append(f"{key}: {value if value != 0 else 0}")
print('\n'.join(result))

