import prompt


GAME_ROUND = 3


def main(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    counter = 0
    while counter < GAME_ROUND:
        question, correct_answer = game.get_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        elif counter == GAME_ROUND - 1:
            print(f'Congratulations, {name}!')
            break
        else:
            print('Correct!')
            counter += 1
