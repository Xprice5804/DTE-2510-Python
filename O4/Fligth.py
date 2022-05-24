from datetime import *


class Flight:
        def __init__(self, flight = "unknown", departure = 0, arrival = 0):
            self.__flightNumber = flight
            self.__departureTime = departure
            self.__arrivalTime = arrival
            
            
        #getters
        def getFlightNumber(self):
            return self.__flightNumber

        def getDepartureTime(self):
            return self.__departureTime

        def getArrivalTime(self):
            return self.__arrivalTime

        def getFlightTime(self):
            return (int((self.__arrivalTime - self.__departureTime).total_seconds()/60))
            
            
        #setters
        def setDepartureTime(self, departure):
            self.__departureTime = departure
            
        def setArrivalTime(self, arrival):
            self.__arrivalTime = arrival
            
        


class Itinerary:
    def __init__(self, fligths):
        self.__Fligths = fligths
    
    
    def getTotalFlightTime(self):
        TotalTime = int()
        a = int()
        for x in self.__Fligths:
            TotalTime = TotalTime + self.__Fligths[a].getFlightTime()
            a += 1
        return TotalTime
    
    def getTotalTravelTime(self):
        Start = self.__Fligths[0].getDepartureTime()
        index = len(self.__Fligths) - 1
        TotalTime = self.__Fligths[index].getArrivalTime() - Start
        TotalTime = int(TotalTime.total_seconds()/60)
        return TotalTime
        

def main():

    flights = []

    flights.append(Flight("US230",

        datetime(2014, 4, 5, 5, 5, 0),

        datetime(2014, 4, 5, 6, 15, 0)))

    flights.append(Flight("US235",

        datetime(2014, 4, 5, 6, 55, 0),

        datetime(2014, 4, 5, 7, 45, 0)))

    flights.append(Flight("US237",

        datetime(2014, 4, 5, 9, 35, 0),

        datetime(2014, 4, 5, 12, 55, 0)))

   

    itinerary = Itinerary(flights)

    print(itinerary.getTotalTravelTime())

    print(itinerary.getTotalFlightTime())

main()
