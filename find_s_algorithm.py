import csv

def find_s(a, t):
    h = a[0].copy()

    for i in range(len(a)):
        if t[i] == "Yes":
            for j in range(len(h)):
                if h[j] != a[i][j]:
                    h[j] = "?"

    return h

with open("trainingdata.csv") as f:
    data = list(csv.reader(f))

data = data[1:]

a = [row[:-1] for row in data]
t = [row[-1] for row in data]

h = find_s(a, t)

print("Final Hypothesis:", h)
