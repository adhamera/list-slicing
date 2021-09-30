"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

input_string = 'calculate: '
tokens = input_string.split(' ')
while True:
    if tokens[0] == "q":
        print('Goodbye! We will see you next time.')
    else: 
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        if tokens[0] == "+":
            print(add(num1,num2))
        elif tokens[0] == "-":
            print(subtract(num1,num2))
# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens