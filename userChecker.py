userName = 'salimul'
password = '1234'

userName_input = input('Enter Your UserName: ')
pas_input = input('Enter your password: ')

# if userName_input == userName and pas_input==password:
#     print('Login Successful')
# else:
#     print('something went wrong')

if userName_input != userName or pas_input != password:
    print('something went wrong')
    if userName_input != userName:
        print('incorrect username')
    elif pas_input != password:
        print('Incorrect password')
else:
    print('Login Successful')
    