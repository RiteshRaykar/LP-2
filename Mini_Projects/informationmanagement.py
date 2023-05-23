# Dictionary to store information
information = {}

# Function to add information to a category
def add_information(category):
    if category not in information:
        information[category] = []
    
    data = input(f"Enter {category} information: ")
    information[category].append(data)
    print(f"Information added to the {category} category.")

# Function to view information for a category
def view_information(category):
    if category in information:
        print(f"{category} Information:")
        for data in information[category]:
            print("- " + data)
    else:
        print(f"No information found for the {category} category.")

# Menu-driven interface
while True:
    print("Information Management System")
    print("-----------------------------")
    print("1. Add Information")
    print("2. View Information")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        category = input("Enter category: ")
        add_information(category)
    elif choice == '2':
        category = input("Enter category: ")
        view_information(category)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
