

class Flight:
    
    def __init__(self, number,aircraft):
        self._number = self._parse_flight_number(number)
        self._aircraft = aircraft     
        rows, seats = self._aircraft.seat_blueprint()     
        self._seatplan = [None] + [{seat: None for seat in seats} for _ in rows]


    def _parse_flight_number(self,number):
        if not number[:2].isalpha():
            raise ValueError(f"Invalid airline code {number}")
        if not number[:2].isupper():
            raise ValueError(f"Airline code {number} not uppercase")
        if not (number[2:].isdigit() and int(number[2:]) < 9999):
            raise ValueError(f"Invalid route number {number}")    
        return number

    def number(self):
        return self._number

    def airline_code(self):
        return self._number[:2]    

    @property
    def aircraft_model(self):
        return  self._aircraft.model() 

    def seatplan(self):
        return self._seatplan 

    def _parse_seat(self,seat_no):       
        """Parse a seat number into valid row and letter
        
        Args:
            seat_no: e.g. "12C" or "3A"

        Returns:
            a tuple of (seat_rows, letters)
            seat_rows: row number of seat
            letters: column alphabet of seat   
        """ 
        rows, seats = self._aircraft.seat_blueprint()        
        letters = seat_no[-1]
        if not letters in seats:
            raise ValueError(f"Invalid seat number: {letters}") 
        seat_rows = seat_no[:-1]        
        try:
            seat_rows = int(seat_rows)
        except ValueError:
            raise ValueError(f"Seat row must be an integer: {seat_rows}")
        if  seat_rows not in rows:
            raise ValueError(f"No such row numbers: {seat_rows}")
        return seat_rows, letters     

    def booking(self, seat_no, passenger_name):        
        """Allocate seat to passenger
        
        Args:
            seat_no: seat number to book such as "12C" or "2E"
            passenger_name: name of the passenger

        Raises:
            ValueError: when seat is unavailable
        """
        seat_rows, letters = self._parse_seat(seat_no)
        if  self._seatplan[seat_rows][letters] is not None:
            raise ValueError(f"Seat is already taken: {seat_no}")
        self._seatplan[seat_rows][letters] = passenger_name  

    def relocate(self,from_seat, to_seat):
        """Relocate passenger from one seat to another

        Args:
            from_seat: the original seat the passenger was in
            to_seat: the seat the passenger wishes to relocate to

        Raise:
            ValueError: if from_seat is empty or if to_seat is already occupied    
        
        """
        from_seat_rows, from_seat_letters = self._parse_seat(from_seat)  
        if self._seatplan[from_seat_rows][from_seat_letters] is None:
            raise ValueError(f"There is no one in this seat {from_seat}")         
        to_seat_rows, to_seat_letters = self._parse_seat(to_seat) 
        if self._seatplan[to_seat_rows][to_seat_letters] is not None:
            raise ValueError(f"This seat {to_seat} is already occupied")   
        self._seatplan[to_seat_rows][to_seat_letters] = self._seatplan[from_seat_rows][from_seat_letters]
        self._seatplan[from_seat_rows][from_seat_letters] = None

    def total_available_seats(self):        
        return sum(sum(1 for letters in row.values() if letters is None)
                        for row in self.seatplan()
                        if not row is None)

    def print_boarding_pass(self, boarding_pass):        
        for passenger, seat in self._passenger_seat(): 
            boarding_pass(passenger, seat, self.number(),self.aircraft_model)          

    def _passenger_seat(self):        
        rows, seats = self._aircraft.seat_blueprint()
        for row in rows:
            for seat in seats:
                passenger = self._seatplan[row][seat] 
                if passenger is not None:
                    yield passenger, f"{row}{seat}" 
                                    

# class Aircraft:
#     def __init__(self, aircraft_number, model, max_rows, max_seats):
#         self._aircraft_number = aircraft_number
#         self._model = model
#         self._max_rows = max_rows
#         self._max_seats = max_seats
        


#     def seat_blueprint(self):
#         return (range(1,self._max_rows + 1), "ABCDEFGHJK"[:self._max_seats])

class Aircraft:
    def __init__(self,aircraft_number,model):
        self._aircraft_number = aircraft_number
        self._model = model

    def aircraft_number(self):
        return self._aircraft_number

    def model(self):
        return self._model     

    def num_seats(self):
        rows, letters = self.seat_blueprint()
        return len(rows)*len(letters)


class Airbus(Aircraft):
    def seat_blueprint(self):
        return range(1,11), "ABCDE"


class Boeing(Aircraft):   
    def seat_blueprint(self):
        return range(1,21), "ABCDEFGHJK"         


def makeflight():
    f = Flight("SD1000",Airbus("SMALL105","Airbus101"))
    f.booking("1B", "Rondo")
    f.booking("1C", "Paul Pierce")
    f.booking("3A", "Kobe Byrant")
    f.booking("3E", "Shaq")       
    f.booking("10C", "Lebron James") 
    
    g = Flight("SD1000", Boeing("BIG999","747"))
    g.booking("1B", "MJ")
    g.booking("5C", "Sir Charles")
    g.booking("13K", "Karl Postman")
    g.booking("13H", "Scottie Pippen")       
    g.booking("20H", "The Dream") 
    return f,g

def boarding_pass(passenger_name, seat_no, flight_number, aircraft_number):
    output = f"| Name: {passenger_name} \
                 Seat: {seat_no} \
                 Flight: {flight_number} \
                 Aircraft: {aircraft_number} |"
    banner = "+" + "-"*(len(output)-2) + "+"
    border = "|" + " "*(len(output)-2) + "|"
    lines = [banner,border, output,border, banner]
    card = "\n".join(lines)
    print(card)
    print()
    
        


             