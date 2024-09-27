# 2024.09.26
def exponent(base, exp):
    result = pow(int(base), int(exp))
    print(base + " raises to the power of " + exp + " is: " + str(result))
    print("i.e. " + ' '.join(base * int(exp)).replace(" ", " * ") + f" = {result}")
    print("\n")


base_input = input('Enter a number: ')
exponent_input = input('Enter an exponent: ')

print("\n")
exponent(base_input, exponent_input)
