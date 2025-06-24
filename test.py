val = "Hey guys, how is it going?"
vals = val.split()
for i in range(len(vals)):
    print(f"{vals[i]}: {len(vals[i])}")