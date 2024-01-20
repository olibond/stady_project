import random
def question_part():
    print('What is your question?')
    answer = input()
    print(random.choice(answers))
def one_more():
    print('One more question? y = yes / n = no')
    y_no = input().lower()
    return y_no
def bad_answer():
    print('Please write y o n')
    y_no = input().lower()
    return y_no

answers = ["Undoubtedly", "It seems to me - yes", "It's not clear yet, try again", "Don't even think about it",
           " Foregone conclusion ", "Most likely" ,  "Ask later", "No doubts", "Good prospects",
            "My answer is no", "No doubts", "Good prospects", "It’s better not to tell", "According to my data - no",
           "You can be sure of it", "Yes", "Concentrate and ask again", "Highly doubtful"]
print('Hello World, I am a magic ball and I know the answer to any question you have.')
print('What your name?')
name = input()
print('Hi,', name.capitalize())
while True:
    question_part()
    y_no = one_more()
    if y_no == 'y':
        question_part()
        continue
    elif y_no == 'n':
        print('Thank you! See you soon')
        break
    else:
        bad_answer()















