def get_questions(subject):
    """Returns a list of questions and answers based on the selected subject."""
    if subject == "DBMS":
        return [
            {"question": "What does DBMS stand for?", 
             "options": ["1. Database Management System", "2. Data Building and Management System", "3. Data Backup Management System", "4. Data Business Management System"], 
             "correct": 1},
            {"question": "Which of the following is a type of database?", 
             "options": ["1. Hierarchical", "2. Network", "3. Relational", "4. All of the above"], 
             "correct": 4},
            {"question": "Which SQL statement is used to extract data from a database?", 
             "options": ["1. GET", "2. EXTRACT", "3. SELECT", "4. FETCH"], 
             "correct": 3},
            {"question": "What is a primary key?", 
             "options": ["1. A unique identifier for a table", "2. A foreign key", "3. A duplicate key", "4. None of the above"], 
             "correct": 1},
            {"question": "Which of the following is a NoSQL database?", 
             "options": ["1. MySQL", "2. MongoDB", "3. Oracle", "4. SQLite"], 
             "correct": 2}
        ]
    elif subject == "DSA":
        return [
            {"question": "What is the time complexity of binary search?", 
             "options": ["1. O(n)", "2. O(log n)", "3. O(n^2)", "4. O(1)"], 
             "correct": 2},
            {"question": "What does FIFO stand for in data structures?", 
             "options": ["1. First In First Out", "2. Fast Input Fast Output", "3. First Input First Operation", "4. None of the above"], 
             "correct": 1},
            {"question": "Which data structure is used in recursion?", 
             "options": ["1. Stack", "2. Queue", "3. Linked List", "4. Array"], 
             "correct": 1},
            {"question": "Which algorithm is used for finding the shortest path?", 
             "options": ["1. Dijkstra's Algorithm", "2. Bubble Sort", "3. Depth First Search", "4. Quick Sort"], 
             "correct": 1},
            {"question": "What is a stack overflow?", 
             "options": ["1. When too many items are pushed onto a stack", "2. When the stack is empty", "3. When the stack is full", "4. None of the above"], 
             "correct": 1}
        ]
    elif subject == "PYTHON":
        return [
            {"question": "Which keyword is used to define a function in Python?", 
             "options": ["1. def", "2. func", "3. function", "4. define"], 
             "correct": 1},
            {"question": "Which of the following is immutable in Python?", 
             "options": ["1. List", "2. Set", "3. Dictionary", "4. Tuple"], 
             "correct": 4},
            {"question": "How do you start a comment in Python?", 
             "options": ["1. //", "2. /*", "3. #", "4. <!--"], 
             "correct": 3},
            {"question": "Which of the following is not a keyword in Python?", 
             "options": ["1. pass", "2. eval", "3. assert", "4. foreach"], 
             "correct": 4},
            {"question": "What is the output of '2 ** 3' in Python?", 
             "options": ["1. 6", "2. 8", "3. 9", "4. 5"], 
             "correct": 2}
        ]
    else:
        return []


def quiz(subject):
    """Conducts a quiz based on the selected subject."""
    questions = get_questions(subject)
    if not questions:
        print("Invalid subject selected!")
        return
    
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        try:
            user_answer = int(input("Enter your choice (1-4): "))
            if user_answer == q["correct"]:
                print("Correct! 🎉")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {q['options'][q['correct'] - 1]}")
        except ValueError:
            print("Invalid input. Skipping the question.")
    
    print(f"\nQuiz Over! Your score: {score}/{len(questions)}")


# Main program
def main():
    print("Welcome to the Quiz Program!")
    print("Available subjects: DBMS, DSA, PYTHON")
    
    while True:
        subject = input("Enter the subject (or type 'exit' to quit): ").upper()
        if subject == "EXIT":
            print("Thank you for using the Quiz Program. Goodbye!")
            break
        quiz(subject)


if __name__ == "__main__":
    main()
