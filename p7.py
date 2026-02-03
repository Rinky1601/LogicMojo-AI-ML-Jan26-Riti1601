org_num = input("Enter three numbers:")
print(org_num)
a,b,c=map(int, org_num.split())
if(b<a>c):
    print(a)
elif(a<b>c):
    print(b)
else:
    print(c)