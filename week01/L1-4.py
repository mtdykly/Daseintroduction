#print("{:chr(0x2605)^15}".format("*"))
print('{0:^15}'.format(' '.join([chr(0x2605)]*11)))
#print(chr(0x2605+"数据科学与工程导论"+chr(0x2605)))
print(chr(0x2605),end=" ")
print("数据科学与工程导论",end="")
print(chr(0x2605))
print('{0:^15}'.format(' '.join([chr(0x2605)]*11)))