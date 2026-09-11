s = input("text: ")
s = s.split()
d = {}
for i in s:
    for j in i:
        d[j] = d.get(j,0)+1
print(d)
