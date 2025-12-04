
import math
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

z = True
Symbol = ["1", "2","3"]
while z:
      A = input("calculator / Quadratic equation / Trigonometry (1 / 2 / 3) ")
      if A not in Symbol:
        symbol = ""
        print("wrong input")
      else:
          z = False
          break  

if A == "1":
    while True:
        one = input("first number = ")
        if isfloat(one) == False:
            print("input a number")
        elif isint(one):
           input_one = int(one)
           break
        elif isfloat(one):
            input_one = float(one)
            break

    symbol_list = ["+" , "-" , "/" , "*"]
    
    while True:
        symbol = input("+ , -, / , * = ")
        if symbol not in symbol_list:
            print("wrong input")
        else:
            break

    while True:
        two = input("second number = ")
        if isfloat(two) == False:
            print("input a number")
        elif isint(two):
            input_two = int(two)
            break
        elif isfloat(two):
            input_two = float(two)
            break

    if symbol == "+":
        print(input_one + input_two)
    if symbol == "-":
        print(input_one - input_two)
    if symbol == "/":
        print(input_one / input_two)
    if symbol == "*":
        print(input_one * input_two)
elif A == "2":

    import math
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    def isint(num):
        try:
            int(num)
            return True
        except ValueError:
            return False

    while True:
        Equation = print("ax²+bx+c=0")
        one = input("a = ")
        if isfloat(one)==False:
            print("input a number")
        elif isint(one):
           a = int(one)
           break
        elif isfloat(one):
            a = float(one)
            break
 
    while True:
        Equation_2 = print(f"\n {a}x²bx+c=0")
        two  = input("b = ")
        if isfloat(two)==False:
            print("input a number")
        elif isint(two):
           b = int(two)
           break
        elif isfloat(two):
            b = float(two)
            break

    while True:
        Equation_3 = print(f"\n {a}x²+{b}x+c=0")
        three  = input("c = ")
        if isfloat(three)==False:
            print("input a number")
        elif isint(three):
           c = int(three)
           break
        elif isfloat(three):
            c = float(three)
            break

    x = b**2 - 4*a*c
    if x > 0:
        y = math.sqrt(x)
        z = (-b + y) / 2
        v = (-b - y) / 2    
        o=str(z)
        p=str(v)
        print(f"\n{a}x²+{b}x+{c}=0")
        print(f"\nx1 = {o}")
        print(f"\nx2 = {p}")
    elif x < 0:
        r = str(-b)
        I = str(x)
        J = str(2 * a)
            
        print(f"\n{a}x²+{b}x+{c}=0")
        print(f"\nx1 = {r} + /{J} + √{I} + /{J}")
        print(f"\nx2 = {r} + /{J} - √{I} + /{J}")
        print("\nD = imajiner")
    else:
         r = -b/(2*a)
         print(f"\nx1 & x2 = {r}")

elif A == "3":
    import math
    trigon = ["sin", "cos", "tan", "csc", "sec", "cot"]
    while True:
        symbol = input("sin, cos, tan, csc, sec, cot: ")
        if symbol not in trigon:
            print("wrong input")
        else:
            break

    if symbol == "sin":
        while True:
            x = input("sin ")
            if isfloat(x) == False:
                print("input a number")
            elif isint(x):
                input_x = int(x)
                break
            elif isfloat(x):
                input_x = float(x)
                break
        if input_x == 0 or input_x % 180 == 0:
            degree = 0
        else :
            input_x = 180 / input_x
            degree = math.pi / input_x
        a = round(math.sin(degree),5)
        print(a)
        
    if symbol == "cos":
        while True:
            x = input("cos ")
            if isfloat(x) == False:
                print("input a number")
            elif isint(x):
                input_x = int(x)
                break
            elif isfloat(x):
                input_x = float(x)
                break
        if input_x == 0 or input_x % 180 == 0:
            degree = 0
        else :
            input_x = 180 / input_x
            degree = math.pi / input_x
        a = round(math.cos(degree),5)
        print(a)

    if symbol == "tan":
        while True:
            x = input("tan ")
            if isfloat(x) == False:
                print("input a number")
            elif isint(x):
                input_x = int(x)
                break
            elif isfloat(x):
                input_x = float(x)
                break
        if input_x % 180 != 0 and input_x % 90 == 0:
            print("undefined")
        else:
            if input_x == 0 or input_x % 180 == 0:
                degree = 0
            else :
                input_x = 180 / input_x
                degree = math.pi / input_x
                a = round(math.tan(degree),5)  
                print(a)

    if symbol == "csc":
        while True:
            x = input("csc ")
            if isfloat(x) == False:
                print("input a number")
            elif isint(x):
                input_x = int(x)
                break
            elif isfloat(x):
                input_x = float(x)
                break
        if input_x == 0 or input_x % 180 == 0:
            degree = 0
        else :
            input_x = 180 / input_x
            degree = math.pi / input_x
        
        try:
            a = round((1 / math.sin(degree)),5)
        except ZeroDivisionError:
            a = "undefined"
        print(a)

    if symbol == "sec":
        while True:
            x = input("sec ")
            if isfloat(x) == False:
                print("input a number")
            elif isint(x):
                input_x = int(x)
                break
            elif isfloat(x):
                input_x = float(x)
                break
        if input_x == 0 or input_x % 180 == 0:
            degree = 0
        else :
            input_x = 180 / input_x
            degree = math.pi / input_x
        try:
            a = round((1 / round(math.cos(degree),2)),5)
        except ZeroDivisionError:
            a = "undefined"
        print(a)

    if symbol == "cot":
        while True:
            x = input("cot ")
            if isfloat(x) == False:
                print("input a number")
            elif isint(x):
                input_x = int(x)
                break
            elif isfloat(x):
                input_x = float(x)
                break
        if input_x % 180 != 0 and input_x % 90 == 0:
            print("undefined")
        else:
            if input_x == 0 or input_x % 180 == 0:
                degree = 0
            else :
                input_x = 180 / input_x
                degree = math.pi / input_x
                a = round(math.tan(degree),5)  
            try:
                a = round((1 / math.tan(degree)),5)
            except ZeroDivisionError:
                a = "undefined"
            print(a)     
    