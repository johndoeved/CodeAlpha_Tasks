## create a program capable of displaying questions to the user like kbc. 
##use list data type to store the questions and their correct answers.
# display the final amount the person is taking home aftr playing the game.#
# import random

# def ask_question(question, options, correct_answer):
#     print("\n" + question)
#     for i, option in enumerate(options, 1):
#         print(f"{i}. {option}")

#     answer = int(input("Enter the number of your answer: "))
#     if options[answer - 1] == correct_answer:
#         return True
#     return False

# def game():
#     questions = [
#         {
#             "question": "What is the capital of France?",
#             "options": ["Paris", "London", "Berlin", "Madrid"],
#             "answer": "Paris"
#         },
#         {
#             "question": "Which planet is known as the Red Planet?",
#             "options": ["Earth", "Mars", "Venus", "Jupiter"],
#             "answer": "Mars"
#         },
#         {
#             "question": "Who wrote 'Harry Potter'?",
#             "options": ["J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin"],
#             "answer": "J.K. Rowling"
#         }
#         # Add more questions as needed
#     ]

#     random.shuffle(questions)
#     score = 0
    
#     for q in questions:
#         if ask_question(q["question"], q["options"], q["answer"]):
#             score += 1
#             print("Correct!")
#         else:
#             print("Incorrect!")

#     print(f"\nYour final score is: {score}/{len(questions)}")

# if __name__ == "__main__":
#     game()





##use list data type to store the questions and their correct answers.
# import random

# def ask_question(question, options, correct_answer):
#     print("\n" + question)
#     for i, option in enumerate(options, 1):
#         print(f"{i}. {option}")

#     answer = int(input("Enter the number of your answer: "))
#     if options[answer - 1] == correct_answer:
#         return True
#     return False

# def game():
#     questions = [
#         {
#             "question": "What is the capital of France?",
#             "options": ["Paris", "London", "Berlin", "Madrid"],
#             "answer": "Paris"
#         },
#         {
#             "question": "Which planet is known as the Red Planet?",
#             "options": ["Earth", "Mars", "Venus", "Jupiter"],
#             "answer": "Mars"
#         },
#         {
#             "question": "Who wrote 'Harry Potter'?",
#             "options": ["J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin"],
#             "answer": "J.K. Rowling"
#         }
#         # Add more questions as needed
#     ]

#     random.shuffle(questions)
#     score = 0
    
#     for q in questions:
#         if ask_question(q["question"], q["options"], q["answer"]):
#             score += 1
#             print("Correct!")
#         else:
#             print("Incorrect!")

#     print(f"\nYour final score is: {score}/{len(questions)}")

# if __name__ == "__main__":
#     game()


## display the final amount the person is taking home aftr playing the game.
import random

def ask_question(question, options, correct_answer):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    answer = int(input("Enter the number of your answer: "))
    if options[answer - 1] == correct_answer:
        return True
    return False

def game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Venus", "Jupiter"],
            "answer": "Mars"
        },
        {
            "question": "Who wrote 'Harry Potter'?",
            "options": ["J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin"],
            "answer": "J.K. Rowling"
        }
        # Add more questions as needed
    ]

    random.shuffle(questions)
    score = 0
    prize_amounts = [1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
    
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            break

    prize = prize_amounts[score] if score < len(prize_amounts) else prize_amounts[-1]
    print(f"\nYour final score is: {score}/{len(questions)}")
    print(f"Congratulations! You are taking home ₹{prize}.")

if __name__ == "__main__":
    game()
