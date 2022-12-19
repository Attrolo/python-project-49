import prompt

def welcome_user():
    name = ''
while name == '':
    print('May I have your name? ', end='')
    name = input('Enter your name')
    print(f'Hello, {name}')
