import random

# dice = [1,2,3,4,5,6]

# select = random.choice(dice)

# print(select)

person = ['khan','terrorist']

name = person[0]
profession = person[1]


sentence_group_one = [
    f'my name is {name}',
    f'{name} is my name',
    f'i am {name}',
    f'{name} is a name'

]

sentence_group_two = [
    f'and i am not a {profession}',
    f'i am not a {profession}',
    f'and khan is not a {profession}'
]

random_name = random.choice(sentence_group_one)
random_profession = random.choice(sentence_group_two)

print(random_name,'.' ,random_profession)