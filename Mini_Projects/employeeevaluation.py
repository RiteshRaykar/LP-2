# Dictionary to store employee evaluations
evaluations = {}

# Function for the manager to give evaluation, rating, and suggestions for improvements
def give_evaluation():
    employee_id = input("Enter employee ID: ")
    evaluation = input("Enter evaluation: ")
    rating = float(input("Enter rating (0-10): "))
    improvements = input("Enter suggestions for improvements: ")
    
    evaluations[employee_id] = {
        'evaluation': evaluation,
        'rating': rating,
        'improvements': improvements
    }
    print(f'Evaluation added for employee {employee_id}.')

# Function for the employee to view their evaluation
def view_evaluation():
    employee_id = input("Enter your employee ID: ")
    
    if employee_id in evaluations:
        print(f'Evaluation: {evaluations[employee_id]["evaluation"]}')
        print(f'Rating: {evaluations[employee_id]["rating"]}')
        print(f'Suggestions for Improvements: {evaluations[employee_id]["improvements"]}')
    else:
        print(f'No evaluation found for employee {employee_id}.')

# Menu-driven interface
while True:
    print("Employee Evaluation System")
    print("--------------------------")
    print("1. Manager")
    print("2. Employee")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        give_evaluation()
    elif choice == '2':
        view_evaluation()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
