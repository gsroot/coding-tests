# read the string filename
filename = input()
reqs = set()
multi_reqs = set()
with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    s = line.split()
    req = s[3].split()[0][1:]
    if req in reqs:
        multi_reqs.add(req)
    else:
        reqs.add(req)

with open(f'./req_{filename}', 'w') as f:
    for req in multi_reqs:
        f.write(f"{req}\n")