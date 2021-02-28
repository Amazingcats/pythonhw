txt = open("/Users/Sherry/downloads/WSW.txt","r")
dict1={}
e = txt.readlines()
for line in e:
    all = line.strip()
    if all in dict1:
        dict1[all]+=1
    else:
        dict1[all]=1
sortedall = sorted(dict1.items(), key = lambda x: x[1], reverse=True)
print(sortedall[0])
d = input('Input a World series team.')
if d in dict1:
    print(dict1[d])
