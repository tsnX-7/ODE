from sympy import *
from prettytable import PrettyTable

def funcVal(eqn, x, y):
    return eval(eqn)

def euler(eqn, x, y, x_f, step):
    curr_y = y + funcVal(eqn, x, y)*step
    if(x_f == x+step):
        result = curr_y
    else:
        result = euler(eqn, x+step, curr_y, x_f, step)
    return result

def heun(eqn, x, y, x_f, step):
    a1 = a2 = 1/2
    p = q = 1
    k1 = funcVal(eqn, x, y)
    k2 = funcVal(eqn, x+(p*step), y+(q*k1*step))

    curr_y = y + (a1*k1 + a2*k2)*step
    if (x_f == x+step):
        result = curr_y
    else:
        result = heun(eqn, x + step, curr_y, x_f, step)
    return result


def midpoint(eqn, x, y, x_f, step):
    a1 = 0
    a2 = 1
    p = q = 1/2
    k1 = funcVal(eqn, x, y)
    k2 = funcVal(eqn, x + (p * step), y + (q * k1 * step))

    curr_y = y + (a1 * k1 + a2 * k2) * step
    if (x_f == x+step):
        result = curr_y
    else:
        result = midpoint(eqn, x + step, curr_y, x_f, step)
    return result

def ralston(eqn, x, y, x_f, step):
    a1 = 1/3
    a2 = 2/3
    p = q = 3/4
    k1 = funcVal(eqn, x, y)
    k2 = funcVal(eqn, x + (p * step), y + (q * k1 * step))

    curr_y = y + (a1 * k1 + a2 * k2) * step
    if (x_f == x+step):
        result = curr_y
    else:
        result = ralston(eqn, x + step, curr_y, x_f, step)
    return result

eqn = input("Enter your differential equation: ")
x_0 = float(input("x_0 : "))
y_0 = float(input("y_0 : "))
x_f = float(input("x_f : "))
step = float(input("Step size: "))
exact = float(input("Exact solution to the equation: "))

ansTable = PrettyTable(['Step Size', 'Euler', 'Heun', 'Midpoint', 'Ralston'])
errTable = PrettyTable(['Step Size', '|\N{GREEK SMALL LETTER EPSILON}|%(Euler)', '|\N{GREEK SMALL LETTER EPSILON}|%(Heun)', '|\N{GREEK SMALL LETTER EPSILON}|%(Midpoint)', '|\N{GREEK SMALL LETTER EPSILON}|%(Ralston)'])

cnt=0
while(cnt!=5):
    ansEuler = euler(eqn, x_0, y_0, x_f, step)
    ansHeun = heun(eqn, x_0, y_0, x_f, step)
    ansMidpoint = midpoint(eqn, x_0, y_0, x_f, step)
    ansRalston = ralston(eqn, x_0, y_0, x_f, step)

    ansTable.add_row([step, round(ansEuler,3), round(ansHeun,3), round(ansMidpoint,3), round(ansRalston,3)])
    errTable.add_row([step, round((abs(exact-ansEuler)/exact)*100,3), round((abs(exact-ansHeun)/exact)*100,3),round((abs(exact-ansMidpoint)/exact)*100,3),round((abs(exact-ansRalston)/exact)*100,3)])

    cnt+=1
    step/=2

print("Solution table for comparison of different method of 'Ordinary Differential Equation' for different step sizes: ")
print(ansTable)
print("\n\n")
print("Error Table for comparison of different method of 'Ordinary Differential Equation' for different step sizes: ")
print(errTable)

'''
-2.2067*10**(-12)*(y**4-81*10**8)
0
1200
480
240
647.57
'''