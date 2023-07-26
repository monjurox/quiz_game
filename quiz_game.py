import random
import operator
print("Welcome to the quiz !!")

playing = input("Do you want to play? yes/no : ")

if playing != "yes":
    quit()

print("okay! Let's play :) ")



def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,

    }

    num1 = random.randint(0,20)
    num2 = random.randint(0,20)

    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num1,num2)
    print(f' what is {num1} {operation} {num2}')

    

    return answer



def ask_question():
    answer = random_problem()
    guess = int(input())
    return guess == answer


def game():
    print("lets go")
    score = 0

    while True:
        if ask_question() == True:
            score+=1
            print("correct!")
        else:
            print("incorrect!")
            # print('correct anser is ') 
            break
    print(f' your score is {score}')

game()


