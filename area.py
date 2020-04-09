a=float(input('enter value'))
b=float(input('enter value'))
c=float(input('enter value'))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print('Area is %0.2f' %area)
