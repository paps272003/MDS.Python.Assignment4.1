def filter_long_words(l,n):
    f=[]
    for e in range(len(l)):
        if len(l[e]) > n:
            f.append(l[e])
    return(f)