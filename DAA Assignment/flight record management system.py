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
        self.records = {'VIP': {}, 'VVIP': {}, 'public': {}}

    def insert(self, flight_id, flight_name, flight_capacity, arrival_time, departure_time, flight_class):
        key = (flight_id, arrival_time)
        self.records[flight_class][key] = FlightRecord(flight_id, flight_name, flight_capacity, arrival_time, departure_time, flight_class)
        print(f"Record {'updated' if key in self.records[flight_class] else 'inserted'} for flight {flight_id}")
    
    def delete(self, flight_class, flight_id, arrival_time):
        key = (flight_id, arrival_time)
        if key in self.records[flight_class]:
            del self.records[flight_class][key]
            print(f"Deleted flight {flight_id}")
        else:
            print(f"Flight {flight_id} not found")
    
    def getNumFlights(self):
        return sum(len(flights) for flights in self.records.values())

    def isEmpty(self):
        return self.getNumFlights() == 0

    def getSorted(self, key_function):
        sorted_flights = []
        for flight_class in self.records:
            sorted_flights += sorted(self.records[flight_class].values(), key=key_function)
        return sorted_flights

    def shortestPathCalculator(self, graph, src, dest):
        import heapq
        n = len(graph)
        distances = [float('inf')] * n
        distances[src] = 0
        pq = [(0, src)]
        while pq:
            current_dist, node = heapq.heappop(pq)
            if current_dist > distances[node]:
                continue
            for neighbor, weight in enumerate(graph[node]):
                if weight and current_dist + weight < distances[neighbor]:
                    distances[neighbor] = current_dist + weight
                    heapq.heappush(pq, (distances[neighbor], neighbor))
        return distances[dest]

# Example usage
if __name__ == "__main__":
    system = FlightManagementSystem()
    system.insert(101, "FlightA", 150, 8, 12, "VIP")
    system.insert(102, "FlightB", 200, 9, 14, "public")
    system.delete("VIP", 101, 8)
    print(f"Total flights: {system.getNumFlights()}")
    print(f"System empty? {system.isEmpty()}")
    sorted_on_arrival = system.getSorted(lambda flight: flight.arrival_time)
    print("Flights sorted by arrival time:", sorted_on_arrival)
    graph = [
        [0, 10, 0, 30, 100],
        [10, 0, 50, 0, 0],
        [0, 50, 0, 20, 10],
        [30, 0, 20, 0, 60],
        [100, 0, 10, 60, 0]
    ]
    print(f"Shortest path: {system.shortestPathCalculator(graph, 0, 4)}")
