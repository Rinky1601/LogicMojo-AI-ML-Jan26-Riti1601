params=input("Enter the principal , rate and interest:")
print(params)
params_list=params.split()
a, b, c=map(int,params_list)
simple_interest=(a*b*c)/100
print(simple_interest)










