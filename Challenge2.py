def diff_files(source,target):
    if len(source)==0:
        source=[]
    else:
        source=source.strip().split()
    if len(target)==0:
        target=[]
    else:
        target=target.strip().split()
    i=0
    while i<len(source):
        t=source[i]
        if t in target:
            source.remove(t)
            target.remove(t)
        else:
            i+=1
    return(len(target),len(source))
print(diff_files('\nz\ncW\nFe1by\n6X5\n\nsqFzv\nb', 'S\nxb3\n1\nlfJ1\nt9sqW\nUUUZE\n\n\n\nw\nqjT\ngGVBL\n\n'))