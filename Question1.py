class Flight:
    # flight_no="ABC"
    # source="India"
    # destination="USA"
    # base_fare=100000

    ################################## a ###############################

    def __init__(self,flight_no,source,destination,base_fare):
        self.flight_no=flight_no
        self.source=source
        self.destination=destination
        self.base_fare=base_fare
    
    ################################## b ################################

    def get_flight_info(self):
        return print(f"Flight no is {self.flight_no}, Source is {self.source} and Destination is {self.destination}")
    
    ################################## c ################################
    
    def calculate_fare(self, passenger_count):
        total_fare=self.base_fare*passenger_count
        print(f"Total Fare without discount is {total_fare}")

    def calculate_fare(self, passenger_count, discount_percent):
        updated_total_fare=(self.base_fare*passenger_count)/discount_percent*100
        print(f"Total Fare with discount is {updated_total_fare}")

    ################################## d ################################
    

fl=Flight("ABC","India","USA",100000)
# fl.calculate_fare(10)
# fl.calculate_fare(10,25)
fl.get_flight_info()
    ################################## e #################################
    # Couldn't solve

    
