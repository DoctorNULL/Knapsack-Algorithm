from csv import reader


file = open('Data.csv', 'r')

lines = reader(file)

c = []
w = []
names = []

for line in lines:
    w.append(int(line[0]))
    c.append(int(line[1]))
    names.append(line[2])

file.close()

b = int(input('Enter Knapsack Size : '))

n = len(c)

triple = [(0, 0, [])]

if w[0] <= b:
    triple.append((c[0], w[0], [0]))

for i in range(0, n - 1):
    Set = [x for x in triple]

    for p, x, t in triple:
        if x + w[i + 1] <= b:
            Set.append((p + c[i + 1], x + w[i + 1], [z for z in t] + [i + 1]))

    for d in Set:
        if d not in triple:
            triple.append(d)

print(triple)

m = triple[0]

for z in triple:
    if z[0] > m[0]:
        m = z

print("Final : ", m)
for i in m[2]:
    print(names[i])
