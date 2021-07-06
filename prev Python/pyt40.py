import array
arrInt=array.array('i',[81,22,13,44,55])
arrFloat=array.array('f',[1.1,2.4,4.66,3.3,5.5])
arrChar=array.array('u',['A','B','C','D','E'])
for x in range(len(arrInt)):
    print(arrInt[x])

for x in range(len(arrFloat)):
    print(arrFloat[x])

for x in range(len(arrChar)):
    print(arrChar[x])