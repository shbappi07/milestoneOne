# number = int(input('Enter your total number: '))

# if number <0:
#     print('invalid number!')
# elif number>=80 and number<=100:
#     print('you got A+')
# elif number >= 70 and number<=79:
#     print('you got A')
# elif number >=59:
#     print('you got A-')
# else:
#     print('you are failed')

num = int(input('Enter your number: '))
age = int(input('Enter your age: '))

# if num >=80 or age <=20:
#     print('You got a chocolate.')
# else:
#     print('Sorry you got less number or over weight')

if not(num <=79 or age <=20):
    print('You got a chocolate.')
else:
    print('Sorry you got less number or over weight')
    