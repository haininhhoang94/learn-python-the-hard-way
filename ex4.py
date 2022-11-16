# Define the number of cars
cars = 100
# Define the seat contain in a car
# Use this to convert to floating point number
space_in_a_car = 4.0
# Define the number of drivers
drivers = 30
# Define the number of passengers
passengers = 90
# Cars that won't have the drivers
cars_not_driver = cars - drivers
# Cars that have drivers
cars_driven = drivers
# Cars that have drivers will be allowed to drive, which translate into the
# number of people that can be transported
carpool_capacity = cars_driven * space_in_a_car
# Average passengers per cars
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "car available.")
print("There are only", drivers, "drivers available.")
