profile = ['samanta', '25', False , 'Nayok', 'Barsha']

name = profile[0]
age = profile[1]
nayika = profile[4]

is_male = profile[2]
if is_male:
    pronoun = 'he'
    gender = 'man'
    profession = 'nayok'
else:
    pronoun = 'she'
    gender = 'woman'
    profession = 'nayika'



print(f'{name} is a Business {gender}. {pronoun.title()} is also a {profession}. {pronoun.title()} is {age} years old ')