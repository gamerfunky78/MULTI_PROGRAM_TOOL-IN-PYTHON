print("1:Hello there? ")
print("2:This programme was made to calculate simple and compound interest")
print("____________________________________________________________________")
print("1. simple interest.")
print("2. compound interest.")
print("3. quadratic equation.")
print("_____________________________________________________________________")
choice = input("input choice from above: ")

if choice == "1":
    print("________________________________________________________________")
    print(" ____              ___          ___                             ")
    print(" |___  |  |\\  /|  |___|  |      |__                            ")
    print(" ____| |  | \\/ |  |      |___   |__                            ")
    print("                  |                                             ")
    print("  ___         _____ ___  ___  ___  ___  ___                     ")
    print("   |    |\\ |    |   |__  |__| |__  |__   |                     ")
    print("  _|_   | \\|    |   |__  | \\  |__  ___|  |           by Brian.")
    print("________________________________________________________________")

    print("you chose simple interest: ")

    deposit = input("input the deposit here: ")
    rate = input("input the interest rate here: ")
    time = input("input the time in years here: ")
    result = float(deposit) * float(rate) * float(time) / 100
    print("The simple interest is: ")
    print("")
    print(result)
# This prints the results of simple interest alone excluding the initial deposit    print("______________________________________________________________________")

if choice =="2":
    print("________________________________________________________________")
    print("   ___    __          ___   __                                  ")
    print("   |     |  |  |\\  /| |__| |  |   |  |  |\\ |  |\\             ")
    print("   |__   |__|  | \\/ | |    |__|   |__|  | \\|  |_|             ")
    print("                                                                ")
    print("   ___       ___  ___   ___  ___  ___  ___                      ")
    print("    |   |\\ |  |   |__   |__| |__  |__   |                      ")
    print("   _|_  | \\|  |   |__   | \\  |__  ___|  |            by Brian.")
    print("________________________________________________________________")
    print("you chose compound interest: ")

    deposit = float(input("input the deposit here: "))
    rate = float(input("input the interest rate in percentage here: "))
    time = float(input("input the time in years here: "))
    result = deposit * ((1 + rate / 100) ** time - 1)
    print("The compound interest is: ")
    print("")
    print(result)
# This prints the results of compound interest alone excluding the initial deposit
    print("")
    print("")
    print("thanks for using my programme.")
print("______________________________________________________________________")
print("______________________________________________________________________")

if choice ==3:
    import math
    print("simple quadratic equations programme")
    a = float(input("input a here:"))
    b = float(input("input b here:"))
    c = float(input("input c here:"))

discriminant = b**2 - 4*a*c
result1 = (-b + math.sqrt(discriminant)) / (2*a)
result2 = (-b - math.sqrt(discriminant)) / (2*a)

    print("the formulae = ax^2 + bx + c")
    print("therefore we substitute a b and c")
    print("________________________________________________________")
    print("this becomes " + str(a)+"x^2 + " + str(b) + "x" + str(c))
    print("the quadratic equation is -b ± √b -4ac /2a")
    print("therefore the substitution becomes"+ str(-b) + "±" + str(b) + "-" + str(4*a*c) + "/" + str(2*a))
    print(" x is therefore equal to:" + str(result1) + " or " + str(result2))
    print("_________________________________________________________")
    print("thanks for using this programme.")
    print("_________________________________________________________")
