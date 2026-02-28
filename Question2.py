flight_no="AI203"
base_fare="4500.75"
tax_percent="5"
seat_number="12A,12B,14C,15D"
is_international="True"

################################# a #################################
updated_fare=float(base_fare)
updated_tax=int(tax_percent)

print(f"Updated Fare is {updated_fare} and updated Tax is {updated_tax}")

final_fare = int(updated_fare+(updated_fare*updated_tax/100))

print(f"Final Fare is {final_fare}")

################################# b #################################

updated_seat_number=seat_number.split(",")
print(f"Updated Seat Number is {updated_seat_number}")

################################# c #################################
updated_set=set(updated_seat_number)
print(f"Updated Set is {updated_set}")

################################# d #################################

updated_is_international=bool(is_international)
print(f"Updated Is International is {updated_is_international}")

################################# e #################################
fight_summary ={"flight_no":"AI203",
                "final_fare":final_fare,
                "seat_number":tuple(updated_seat_number)    
                }

print(f"Final Result is {fight_summary}")