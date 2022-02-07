import glob, json

fl = glob.glob('./1202/*.json')

all = []
for fn in fl:
    with open(fn) as f:
        st = f.read()
        jo = json.loads(st)
        all += jo
    print(fn, len(all))

with open('all_2020.json', 'w+') as f:
    f.write(json.dumps(all))