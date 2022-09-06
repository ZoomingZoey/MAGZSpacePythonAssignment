# import all required modules
from planets import planets
import utils
from constants import *
from datetime import datetime
import time_counter as tc


# get the current local time from the computer
current_local_time = datetime.now()

# create a list of all the planet names in lowercase
planet_names = [planet.name.lower() for planet in planets]

print('--------------------------------------------------------------------------------------')
print('Project MAGZ Planet Distance Calculation Software.\n\n')
print('Copyright (c) 2022 Space Research Laboratories, New Zealand. All Rights Reserved.')
print('--------------------------------------------------------------------------------------')

# create a loop to keep the program running until the user is done
while True:

    # loop over and display all the planets, then prompt the user to select one
    print('\nPlease enter a planet name from the list of destination Planets below.\n')

    print('The Destination Planets are:\n')
    for i in range(len(planets)):
        print(f'- {planets[i].name}')

    # create a variable to hold the destination planet name
    destination_name = str()

    # create a while True loop to simulate a do-while loop so that the user will continually be asked for a valid planet name if an invalid one is entered
    while True:
        # prompt for the input
        destination_name = input('\nDestination planet: ')

        if destination_name.lower() in planet_names:
            break

        print('\nInvalid Destination. Please enter a Planet name from the list.')

    # create a variable to hold the thrust force
    thrust_force_newtons = int()

    # create a while True loop to simulate a do-while loop so that the user will continually be asked for a thrust value if the value entered is not a number
    while True:
        try:
            # try prompt for the input
            thrust_force_input = int(input(f'\nPlease enter the thrust force in Newtons between {MIN_THRUST_FORCE_N}N and {MAX_THRUST_FORCE_N}N: '))

            if thrust_force_input < MIN_THRUST_FORCE_N or thrust_force_input > MAX_THRUST_FORCE_N:
              raise ValueError

            thrust_force_newtons = thrust_force_input
            break
        except ValueError:
            print(f'\nThrust force must be a positive integer value between {MIN_THRUST_FORCE_N} and {MAX_THRUST_FORCE_N}.')

    # create a variable to hold the vehicle mass
    vehicle_mass = int()

    # create a while True loop to simulate a do-while loop so that the user will continually be asked for a thrust value if the value entered is not a number
    while True:
        try:
            # prompt for the input
            vehicle_mass_input = int(input(f'\nPlease enter the Vehicle mass in Kilograms between {MIN_VEHICLE_WEIGHT_KG}Kg and {MAX_VEHICLE_WEIGHT_KG}Kg: '))
          
            if vehicle_mass_input < MIN_VEHICLE_WEIGHT_KG or vehicle_mass_input > MAX_VEHICLE_WEIGHT_KG:
              raise ValueError
            
            vehicle_mass = vehicle_mass_input
            break
        except ValueError:
            print(f'\nVehicle mass must be a positive integer value between {MIN_VEHICLE_WEIGHT_KG} and {MAX_VEHICLE_WEIGHT_KG}.')

    # get the selected destination as a Planet object
    selected_planet = utils.find(lambda v: v.name.lower() == destination_name.lower(), planets)

    print('\n--------------------------------------------------------------------------------------')

    # display the local time
    print(f'\nThe current local time is: {str(current_local_time)}\n')

    # calculate the AU distance from earth to the destination
    destination_total_distance_au = utils.calculate_destination_au_distance(selected_planet.au_distance)

    # convert the AU distance to kilometers
    destination_total_distance_km = utils.au_to_kilometers(destination_total_distance_au)

    # convert the kilometer distance to meters for later use
    destination_total_distance_m = utils.km_to_meters(destination_total_distance_km)

    # display te distance from earth to the destination in AU's and Kilometers
    print(f'Total distance to {destination_name.capitalize()}: {destination_total_distance_au:.2f} AU ({destination_total_distance_km:.2f} Kilometers)')

    # convert the thrust force from Newtons to Kilograms
    thrust_force_kg = utils.newtons_to_kilogram_force(thrust_force_newtons)

    # display the applied (thrust) force in Newtons and Kilogram-force
    print(f'Applied (thrust) force: {thrust_force_newtons}N ({thrust_force_kg:.2f} Kilometer-force)')

    # display the craft's mass in kilograms
    print(f'Craft Mass: {vehicle_mass}Kg')

    # display the orbital velocity
    print(f'Orbital velocity: {INITIAL_LAUNCH_VELOCITY} m/2')

    # get the craft's acceleration in meters per second per second
    craft_acceleration = utils.acceleration(thrust_force_newtons, vehicle_mass)

    # display the acceleration experienced by the craft
    print(f'Craft acceleration: {craft_acceleration:.2f} m/2\u00b2')

    # begin running the calculation
    current_distance_travelled = 0
    half_way_point = destination_total_distance_km / 2
    time_step = 0
    instant_velocity = 0
    time_counter = tc.TimeCounter()

    # use a while loop to calculate the distance and velocity while we are less than the destination's half way point
    while current_distance_travelled < half_way_point:
        # derive the instant velocity for each time increment
        instant_velocity = utils.instant_velocity(craft_acceleration, time_step)

        # derive the distance travelled so far for each time increment in seconds
        current_distance_travelled = utils.distance_travelled(time_step, craft_acceleration)

        # increment the time step and time counter
        time_counter.increment()
        time_step += 1

    print('\n--------------------------------------------------------------------------------------')

    # tell the user the half way point has been reached
    print('\nATTENTION: The Half-way point has been reached.\n')

    # display the time taken to reach the half way point in years, months, weeks, days, hours, minutes and seconds
    print(f'Time taken to reach the half way point:')
    time_counter.print()

    # display the craft's instant (present) velocity in meters per second, kilometers per second and kilometers per hour at the half way point
    print(f'\nCraft instant (present) velocity: {instant_velocity:.2f} m/2 ({utils.ms_to_kmps(instant_velocity):.2f} km/s, {utils.ms_to_kmph(instant_velocity):.2f} km/h)\n')

    # display the distance travelled in kilometers and meters
    print(f'Distance travelled: {current_distance_travelled:.2f} Km ({utils.km_to_meters(current_distance_travelled):.2f} m\n')

    # calculate the distance left to travel and display it in kilometers and meters
    distance_left = destination_total_distance_km - current_distance_travelled
    print(f'Distance left to travel: {distance_left:.2f} Km ({utils.km_to_meters(distance_left):.2f} m)\n')

    # display the half way velocity as a percentage of light speed
    print(f'Half way velocity percentage: {utils.percentage(instant_velocity, SPEED_OF_LIGHT):.2f}% of light-speed\n')

    # display the kinetic energy of the craft at the half way point
    print(f'Craft kinetic energy: {utils.kinetic_energy(vehicle_mass, instant_velocity):.2f}\n')

    # calculate the estimated total travel time and display it in years, months, weeks, days, hours, minutes and seconds
    print(f'Estimated total time to reach the destination:')
    estimated_total_travel_time_seconds = utils.time_from_distance_and_speed(destination_total_distance_m, INITIAL_LAUNCH_VELOCITY)
    print(time_counter.calculate_from_seconds(estimated_total_travel_time_seconds))

    print('\n--------------------------------------------------------------------------------------')

    # ask the user if they would like to calculate another Destination, if 'N' is entered the application will close.
    choice = input('\nWould you like to calculate another Destination? (Y/N): ')
    if choice.lower() == 'n':
        break
