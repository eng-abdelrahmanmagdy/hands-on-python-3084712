NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for i, name in enumerate(NAMES):
   print(f"{i} {name}")

 

# enumerate
