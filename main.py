mylist = [9, "jeremy", [5,6]]
        #0     1      2
newlist = mylist + [23, 24]
newlist.append("mara")
newlist.insert(2, 800)
newlist.extend([6,6,6,])
del newlist[0]
newlist.remove(800)
print(newlist)
del newlist[2:]
numberedlsit = [89, 56, 99 , 2]
print(sorted(numberedlsit))

if 56 in numberedlsit:
    print("found it")