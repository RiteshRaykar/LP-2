# Dictionary to store flights
flights = {}

# Dictionary to store cargo
cargo = {}

# Function to add a flight
def add_flight():
    flight_number = input("Enter flight number: ")
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    departure_time = input("Enter departure time: ")
    
    flights[flight_number] = {
        'origin': origin,
        'destination': destination,
        'departure_time': departure_time,
        'cargo': []
    }
    print(f'Flight {flight_number} added successfully.')

# Function to add cargo to a flight
def add_cargo():
    flight_number = input("Enter flight number: ")
    cargo_item = input("Enter cargo item: ")
    
    if flight_number in flights:
        flights[flight_number]['cargo'].append(cargo_item)
        print(f'Cargo {cargo_item} added to flight {flight_number}.')
    else:
        print(f'Flight {flight_number} does not exist.')

# Function to display all flights
def display_flights():
    if flights:
        print("Flight Details:")
        for flight_number, flight_info in flights.items():
            print(f"Flight Number: {flight_number}")
            print(f"Origin: {flight_info['origin']}")
            print(f"Destination: {flight_info['destination']}")
            print(f"Departure Time: {flight_info['departure_time']}")
            print("Cargo: ", flight_info['cargo'])
            print()
    else:
        print("No flights available.")

# Menu-driven interface
while True:
    print("Airline and Cargo System")
    print("------------------------")
    print("1. Add Flight")
    print("2. Add Cargo")
    print("3. Display Flights")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_flight()
    elif choice == '2':
        add_cargo()
    elif choice == '3':
        display_flights()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
