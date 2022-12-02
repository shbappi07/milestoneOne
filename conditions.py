# number = float(input('enter a number: '))

# if number >10: 
#     add = number+2
#     print(add)

# age = float(input('Enter your age: '))

# if age >18:
#     print('you are eligible for voting')
# else:
#     print('you are not eligible to vote')

number = int(input('Enter number to check: '))

if number >=80 :
    print('Congratulation! you got A+, your total number is :', number)
elif number >=70:
    print('Congratulation! you got A, your total number is :', number)
elif number >=60:
    print('COngratulation! you got A-, your total number is ', number)
else:
    print('!sorry you\'ve failed, your number is ',number)
