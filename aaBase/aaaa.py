a = {'b':None,'d':None,'e':'f'}

for k in a.keys():
    v = a[k]
    if not v:
        del a[k]
print(a)

