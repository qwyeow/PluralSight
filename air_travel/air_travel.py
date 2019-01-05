from pprint import pprint as pp

class Flight:

    def __init__(self, num, aircraft):
        self._number = self.parse_number(num)
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{seat: None for seat in seats} 
                                              for _ in rows]

    def parse_number(self,num):
        if not num[:2].isalpha():
            raise ValueError(f"This must be alphabets: {num[:2]}") 
        if not num[:2].isupper():
            raise ValueError(f"This must be uppercase: {num[:2]}")
        if not (num[2:].isdigit() and int(num[2:]) <= 9999):
            raise ValueError(f"Invalid number: {num[2:]}")
        return num          


    def number(self):
        return self._number

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self,seat, passenger):
        
        row_text, seat_text = self._parse_seat(seat)   

        if not self._seating[row_text][seat_text] is None:
            raise ValueError("Seat is occupied")
        
        self._seating[row_text][seat_text] = passenger


    def _parse_seat(self,seat):
        rows, seats = self._aircraft.seating_plan()
        row_text = seat[:-1]
        seat_text = seat[-1]

        try:
            row_text = int(row_text)
        except ValueError:
            raise ValueError("Rows must be integers")
        if not int(row_text) in rows:
            raise ValueError("No such row number")
        if not seat_text in seats:
            raise ValueError("No such seat number") 

        return row_text, seat_text    


    def relocate_passsenger(self,from_seat, to_seat):
        from_row, from_seat = self._parse_seat(from_seat)   
        to_row, to_seat = self._parse_seat(to_seat)

        if self._seating[from_row][from_seat]  is None:
            raise ValueError("No passenger to move from")
        if not self._seating[to_row][to_seat] is None:
            raise ValueError("Desired seat is occupied")

        self._seating[to_row][to_seat]  =  self._seating[from_row][from_seat] 
        self._seating[from_row][from_seat] = None

    def available_seats(self):

        return sum(sum(1 for seat in row.values() if seat is None) 
                    for row in self._seating 
                    if row is not None) 

    def make_boarding_pass(self, boarding_pass):
        for passenger, seat in sorted(self.passenger_list()):
            #boarding_pass(self.number(), seat, passenger,self._aircraft.model()) # demeter's law!!!!!
            boarding_pass(self.number(), seat, passenger,self.aircraft_model())


    def passenger_list(self):
        rows, seats = self._aircraft.seating_plan()
        for row in rows:
            for seat in seats:
                passenger = self._seating[row][seat]
                if passenger is not None:
                    yield passenger, f"{row}{seat}" 
                            




class Aircraft:

    def __init__(self, registration):
        self._registration = registration    
        # self._num_rows = num_rows
        # self._num_seats = num_seats

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, seats = self.seating_plan()    
        return len(rows)*len(seats)

 
class AirbusA319(Aircraft):
    def model(self):
        return "AirbusA319"

    def seating_plan(self):
        return range(1,11), "ABCDE"


class Boeing747(Aircraft):
    def model(self):
        return "Boeing747"

    def seating_plan(self):
        return range(1, 21), "ABCDEFGHJK"        


def boarding_pass(flight, seat, passenger, aircraft, border = "*"):
    output = f"| Flight: {flight:2} \
                Seat: {seat:2} \
                Name: {passenger:2}\
                Model: {aircraft} |" 
    
    borderline = "+" + border*(len(output)-2) + "+"
    space = "|" + " "*(len(output)-2) + "|"
    line = [borderline,space,output, space, borderline]
    card = "\n".join(line)
    print(card)
    print() 



def test_aircraft():
    a = Aircraft("G-EURT", "Airbus A319", 22,5)
    print(a.model())
    print(a.seating_plan())   


def test_flight():
    f = Flight("SN100", Aircraft("G-EURT", "Airbus A319", 22,5))   
    print("f.aircraft_model():")
    print(f.aircraft_model())  
    print("f._seating:")
    pp(f._seating)
    print("f.allocate_seat 9D to Kobe:")
    f.allocate_seat("9D", "Kobe Bryant")
    pp(f._seating)

    print("f.allocate_seat 15A to Rondo:")
    f.allocate_seat("15A", "Rondo")
    print("f.allocate_seat 15B to Paul Pierce:")
    f.allocate_seat("15B", "Paul Pierce")
    pp(f._seating)

    print("f.allocate_seat 9D to MJ:")
    try:
        f.allocate_seat("9D", "Micheal Jordan")
    except ValueError as e:
        print(f"Value Error: {str(e)}")   

    print("f.allocate_seat D27 to Scottie Pippen:")
    try:
        f.allocate_seat("D27","Scottie Pippen")
    except ValueError as e:
        print(f"Value Error: {str(e)}")

    print("f.allocate_seat 29D to Hakeem the Dream:")
    try:
        f.allocate_seat("29D","Hakeem the Dream")
    except  ValueError as e:
        print(f"Value Error: {str(e)}")

    print("relocate passenger from 15B to 1A:")
    f.relocate_passsenger("15B", "1A")   
    

    print("relocate passenger from 1A to 15A:")
    try:
        f.relocate_passsenger("1A", "15A")   
    except ValueError as e:
        print({str(e)})

    print("Available seats:")
    print(f.available_seats())    

    boarding_pass("SQ1004", "13A", "Lebron James", "Boing 747", border = "*")

    print("Boarding pass of all passengers:")
    print(f.make_boarding_pass(boarding_pass))



if __name__ == "__main__":
    test_aircraft()
    test_flight()




