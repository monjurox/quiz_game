import random
import operator

print("Welcome to the quiz !!")

playing = input("Do you want to play? yes/no : ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")


def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)

    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num1, num2)
    print(f'What is {num1} {operation} {num2}')

    return answer


def ask_question():
    answer = random_problem()
    guess = int(input())
    return guess == answer


def game():
    print("Let's go!")
    score = 0

    while True:
        if ask_question():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            break

    return score


leaderboard = []

while True:
    score = game()
    print(f'Your score is {score}')

    player_name = input("Enter your name: ")
    leaderboard.append({'name': player_name, 'score': score})

    play_again = input("Do you want to play again? yes/no: ")
    if play_again.lower() != "yes":
        break

print("Thanks for playing! Goodbye!")

# Display the leaderboard
print("Leaderboard:")
leaderboard.sort(key=lambda x: x['score'], reverse=True)
for index, entry in enumerate(leaderboard, start=1):
    print(f"{index}. {entry['name']}: {entry['score']} points")
