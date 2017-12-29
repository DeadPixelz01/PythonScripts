# Defining functions
# A basic function
def my_function():
    print('This is a normal function')

# A function that supports arguments
def my_function_with_args(username, greeting):
    print('Unlike the last function, this one supports arguments')
    print('Hello, %s. I hope you have %s day'%(username, greeting))

# A function that can return a numerical int by doing math
def my_function_with_ints(x, y):
    return x + y


# Calling functions
my_function()

my_function_with_args("Alex", "great")

a = my_function_with_ints(2, 2)

