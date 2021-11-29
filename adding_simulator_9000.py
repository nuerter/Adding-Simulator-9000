introduction = input("Welcome to \"adding simulator 9000\", press enter to continue.")
first = input("first digit: ")
if first == str():
    print(str("You chose the red pill"))
    exit()
else:
    final_first = float(first)
second = input("second digit: ")
if second == str():
    print(str("You chose the red pill"))
    exit()
else:
    final_second = float(second)

sim = float(final_first + final_second)
print(str("The result: ") + str(sim))
