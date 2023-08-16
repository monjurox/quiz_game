import random
import operator

print("Welcome to the quiz !!")

playing = input("Do you want to play? yes/no : ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")


def random_problem(difficulty):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    if difficulty == "easy":
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
    elif difficulty == "medium":
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
    elif difficulty == "hard":
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
    else:
        print("Invalid difficulty level.")
        return None

    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num1, num2)
    print(f'What is {num1} {operation} {num2}')

    return answer


def ask_question(difficulty):
    answer = random_problem(difficulty)
    guess = int(input())
    return guess == answer, answer


def game():
    print("Let's go!")
    score = 0

    difficulty = input("Choose a difficulty level (easy/medium/hard): ").lower()

    while True:
        is_correct, correct_answer = ask_question(difficulty)
        if is_correct:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {correct_answer}")
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

