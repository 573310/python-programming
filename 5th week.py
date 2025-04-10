i,k,p=0,0,""

for i in range(2,10,1):
    p=p+("# %d단 #" %i)

print(p)

for i in range(1,10,1):
    p=""
    for k in range(2,10):
        p=p+str("%2d X%2d = %2d"%(k,i,k*i))
    print(p)