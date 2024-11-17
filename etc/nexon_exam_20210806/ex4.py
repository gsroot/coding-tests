# read the string filename
filename = input()

gifs = set()
with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    s = line.split()
    url = s[-4]
    fname = url.split('/')[-1]
    if s[-5] == '"GET' and s[-2] == '200' and fname.split('.')[-1].lower() == 'gif':
        gifs.add(fname)

with open(f'./gifs_{filename}', 'w') as f:
    for gif in gifs:
        f.write(f"{gif}\n")