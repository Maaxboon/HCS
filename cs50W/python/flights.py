class Flight():
    
    # Creates new flight
    def __init__(self, capacity):
        self.capacity = capacity
        # creates an empty list of passengers
        self.passengers = []

# Flight methods

# Adds a passenger to the flight
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        # Adds a passenger to the end of the empty passengers list
        self.passengers.append(name)
        return True

        #  Tells us how many open seats are on the flight
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

players = ['Maaxboon', 'Kimaru', 'Muchacho', 'Mwongela']
for player in players:
     success = flight.add_passenger(player)
     if success:
         print(f"Added {player} to flight successfully!")
     else:
        print(f"No available seats for {player}")

