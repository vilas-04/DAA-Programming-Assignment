# Flight Records Management System in Python

class FlightRecord:
    def __init__(self, flight_id, flight_name, flight_capacity, arrival_time, departure_time, flight_class):
        self.flight_id = flight_id
        self.flight_name = flight_name
        self.flight_capacity = flight_capacity
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.flight_class = flight_class
    
    def __repr__(self):
        return f"ID: {self.flight_id}, Name: {self.flight_name}, Capacity: {self.flight_capacity}, Arrival: {self.arrival_time}, Departure: {self.departure_time}, Class: {self.flight_class}"

class FlightManagementSystem:
    def __init__(self):
        # Separate dictionaries for VIP, VVIP, and public flights
        self.records = {
            'VIP': {},
            'VVIP': {},
            'public': {}
        }

    def insert(self, flight_id, flight_name, flight_capacity, arrival_time, departure_time, flight_class):
        record = FlightRecord(flight_id, flight_name, flight_capacity, arrival_time, departure_time, flight_class)
        key = (flight_id, arrival_time)
        
        if key in self.records[flight_class]:
            print(f"Updating existing flight record: {flight_id}")
        else:
            print(f"Inserting new flight record: {flight_id}")
        
        self.records[flight_class][key] = record
        return True

    def delete(self, flight_class, flight_id, arrival_time):
        key = (flight_id, arrival_time)
        if key in self.records[flight_class]:
            del self.records[flight_class][key]
            print(f"Deleted flight record: {flight_id}")
        else:
            print(f"No flight found with ID {flight_id} in {flight_class} class.")
            return False
        return True

    def getNumFlights(self):
        total_flights = sum(len(self.records[cls]) for cls in self.records)
        return total_flights

    def isEmpty(self):
        return self.getNumFlights() == 0

    def isFull(self):
        # For demonstration purposes, let's assume a max limit of 100 records
        MAX_RECORDS = 100
        return self.getNumFlights() >= MAX_RECORDS

    def getFlightWithLongestStay(self):
        longest_stay = 0
        longest_flights = []
        
        for cls in self.records:
            for flight in self.records[cls].values():
                stay_time = flight.departure_time - flight.arrival_time
                if stay_time > longest_stay:
                    longest_stay = stay_time
                    longest_flights = [flight]
                elif stay_time == longest_stay:
                    longest_flights.append(flight)
        
        return longest_flights

    def getSortedOnArrivalTime(self):
        sorted_flights = []
        for cls in self.records:
            sorted_flights.extend(sorted(self.records[cls].values(), key=lambda x: x.arrival_time))
        return sorted_flights

    def getSortedOnDepartureTime(self):
        sorted_flights = []
        for cls in self.records:
            sorted_flights.extend(sorted(self.records[cls].values(), key=lambda x: x.departure_time))
        return sorted_flights

    def getSortedOnStayTime(self):
        sorted_flights = []
        for cls in self.records:
            sorted_flights.extend(sorted(self.records[cls].values(), key=lambda x: (x.departure_time - x.arrival_time)))
        return sorted_flights

    def shortestPathCalculator(self, graph, src, dest):
        # Implementing Dijkstra's algorithm
        import heapq
        n = len(graph)
        distances = [float('inf')] * n
        distances[src] = 0
        priority_queue = [(0, src)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in enumerate(graph[current_node]):
                if weight > 0:  # There is a direct path
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances[dest]

# Example usage
if __name__ == "__main__":
    system = FlightManagementSystem()
    
    # Inserting some flights
    system.insert(101, "FlightA", 150, 8, 12, "VIP")
    system.insert(102, "FlightB", 200, 9, 14, "public")
    
    # Deleting a flight
    system.delete("VIP", 101, 8)
    
    # Get number of flights
    print(f"Number of flights: {system.getNumFlights()}")
    
    # Check if the system is empty
    print(f"Is system empty? {system.isEmpty()}")
    
    # Sort by arrival time
    print("Sorted by arrival time:")
    for flight in system.getSortedOnArrivalTime():
        print(flight)
    
    # Shortest path calculation
    graph = [
        [0, 10, 0, 30, 100],
        [10, 0, 50, 0, 0],
        [0, 50, 0, 20, 10],
        [30, 0, 20, 0, 60],
        [100, 0, 10, 60, 0]
    ]
    print(f"Shortest distance from 0 to 4: {system.shortestPathCalculator(graph, 0, 4)}")
