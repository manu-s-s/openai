k='3\n\n4\n\n\n5'
k=k.split('\n')
k[:] = [item for item in k if item!='']
print(k)