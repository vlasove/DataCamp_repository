#Квадратное уравнение.
#На вход вашей программе подаются 3 числа : A,B,C
#Ax^2 + Bx + C = 0
#На выходе - корни уравнения (x1,x2 так же x1)
#Если D < 0 --- корней нет
#Гарантируется, что как минимум один из кожффициентов != 0

#D = B**2 - 4*A*C
#X1 = (-B + D**(1/2) ) / (2*A)
#X2 = (-B - D**(1/2) ) / (2*A)


#input                         #output
#2                             нет корней
#1
#2

#1                              2, 3
#-5
#6

#1                              1
#-2
#1



A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

if A == 0:
    if B == 0:
        print("нет корней")  
    else:
        print(-C/B)
else:
    D = B**2 - 4*A*C
    if D < 0:
        print("нет корней")
    elif D == 0:
        x = (-B/(2*A))
        print(x)
    else:
        x1 = (-B+D**(1/2))/(2*A)
        x2 = (-B-D**(1/2))/(2*A)
        print(x1,x2)



#D = B**2 - 4*A*C
#X1 = (-B + D**(1/2) ) / (2*A)
#X2 = (-B - D**(1/2) ) / (2*A)