s=[x*x for x in range(1,11)]
print(s)

v=[2**x for x in range(10)]
print(v)

# code is equivalent to
pow=[]
for x in range(10):
    pow.append(2**x)
print(pow)

m=[x for x in s if x%2==0]
print(m)

words="the quick brown fox jumps over the lazy dog".split()
print(words)
l=[[w.upper(),len(w)] for w in words]
print(l)