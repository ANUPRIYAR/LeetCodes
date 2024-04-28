class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        print(f"buses: {buses}")
        print(f"passengers: {passengers}")
        capacities = [capacity]*len(buses)

        passenger = 0
        time = 0
        for  bus in buses:
            cap = capacity
            while passenger < len(passengers) and cap != 0 and passengers[passenger] <= bus:
                passenger  += 1
                cap -= 1
        if passenger != 0:
            last_passenger_time = passengers[passenger-1]
        else:
            return bus
        print(last_passenger_time)
        if cap > 0 and last_passenger_time < bus:
            return bus
             
        

        while last_passenger_time in passengers and last_passenger_time > 0:
            last_passenger_time -= 1

        return last_passenger_time
        
                 
            
           




        