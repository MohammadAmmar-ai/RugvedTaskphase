#diamond pattern
n = int(input("Enter n: "))

for k in range(1, n + 1):
    num_spaces = n - k
    line = ""
    for s in range(num_spaces):
        line = line + " "
    for s in range(k):
        line = line + "* "
    print(line)

for k in range(n, 0, -1):
    num_spaces = n - k
    line = ""
    for s in range(num_spaces):
        line = line + " "
    for s in range(k):
        line = line + "* "
    print(line)

#Butterfly pattern
n = int(input("Enter n: "))

total_slots = 2 * n - 1   # total width stays fixed for every row

for i in range(1, n + 1):
    line = ""
    for slot in range(total_slots):
        if slot < i or slot >= total_slots - i:
            line = line + "* "
        else:
            line = line + "  "
    print(line)

for i in range(n - 1, 0, -1):
    line = ""
    for slot in range(total_slots):
        if slot < i or slot >= total_slots - i:
            line = line + "* "
        else:
            line = line + "  "
    print(line)