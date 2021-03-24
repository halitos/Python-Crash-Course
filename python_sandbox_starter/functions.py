# A function is a block of code which only runs when it is called.
# In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def sayHello(name="Bob"):
    print(f'Hello {name}')


sayHello()

# Return values


def getSum(num1, num2):
    tot = num1 + num2
    return tot


res = getSum(3, 7)


print(res)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to JS arrow functions

def getMore(nom1, nom2): return nom1 + nom2


print(getMore(2, 6))
