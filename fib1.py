a=0
b=1
print(a)
print(b)
for i in range(2,7):
    a=a+b
    a,b=b,a
    print(a)
    
