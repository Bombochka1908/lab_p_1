#lab_p_1
print("введите коэффициенты уравнения y= ax**2 + bx + c")
a=float(input())
b=float(input())
c=float(input())

d= b**2 -4*a*c
if d>0:
    x1=(-b +d**0,5)/2*a
    x2=(-b -d**0,5)/2*a
    print(x1,x2)
if d==0:
    x1=(-b)/2*a
    print(x1)
else:
    print("нет корней")