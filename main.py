# import all required modules
from planets import planets
from asteroids import asteroids
import utils
from constants import *
from datetime import datetime


# get the current local time from the computer
current_local_time = datetime.now()

print('--------------------------------------------------------------------------------------')
print('Project MAGZ Planet Distance Calculation Software.\n\n')
print('Copyright (c) 2022 Space Research Laboratories, New Zealand. All Rights Reserved.')
print('--------------------------------------------------------------------------------------')

# create a loop to keep the program running until the user is done
while True:

    # display the local time
    print(f'\nThe current local time is: {str(current_local_time)}\n')

    # prompt the user asking them if they only want a static simulation?
    only_static = utils.prompt_only_static()

    # copy the planets array into a destinations array
    destinations = planets.copy()

    # only include the list of asteroids in the destinations array if we are not doing a static simulation
    if only_static is False:
        destinations.extend(asteroids)

    # loop over and display all the destinations, then prompt the user to select one
    print('\nPlease enter a destination name from the list of destinations below.\n')

    print('The Destinations are:\n')
    print('Planets:\n')
    for i in range(len(planets)):
        print(f'- {planets[i].name}')

    # only loop over and list the asteroids array if we are not doing a static simulation
    if only_static is False:
        print('\nAsteroids:\n')
        for i in range(len(asteroids)):
            print(f'- {asteroids[i].name}')

    # create a list of all the destination names in lowercase
    destination_names = [destination.name.lower()
                         for destination in destinations]

    # get the destination  name and store it in a variable
    destination_name = utils.prompt_destination(destination_names)

    # get the thrust force and store it in a variable
    thrust_force_newtons = utils.prompt_thrust_force()

    # get the vehicle mass and store it in a variable
    vehicle_mass = utils.prompt_vehicle_mass()

    # get the selected destination as an object
    selected_destination = utils.find(
        lambda v: v.name.lower() == destination_name.lower(), destinations)

    print('\n--------------------------------------------------------------------------------------')

    # calculate the AU distance from earth to the destination
    destination_total_distance_au = utils.calculate_destination_au_distance(
        selected_destination.au_distance)

    # convert the AU distance to kilometers
    destination_total_distance_km = utils.au_to_kilometers(
        destination_total_distance_au)

    # convert the kilometer distance to meters for later use
    destination_total_distance_m = utils.km_to_meters(
        destination_total_distance_km)

    # display the distance from earth to the destination in AU's and Kilometers
    print(
        f'Total distance to {destination_name.capitalize()}: {destination_total_distance_au:.2f} AU ({destination_total_distance_km:.2f} Kilometers)')

    # convert the thrust force from Newtons to Kilograms
    thrust_force_kg = utils.newtons_to_kilogram_force(thrust_force_newtons)

    # display the applied (thrust) force in Newtons and Kilogram-force
    print(
        f'Applied (thrust) force: {thrust_force_newtons}N ({thrust_force_kg:.2f} Kilometer-force)')

    # display the craft's mass in kilograms
    print(f'Craft Mass: {vehicle_mass}Kg')

    # display the orbital velocity
    print(f'Orbital velocity: {INITIAL_LAUNCH_VELOCITY} m/2')

    # get the craft's acceleration in meters per second per second
    craft_acceleration = utils.acceleration(thrust_force_newtons, vehicle_mass)

    # display the acceleration experienced by the craft
    print(f'Craft acceleration: {craft_acceleration:.2f} m/2\u00b2')

    print('\n--------------------------------------------------------------------------------------')

    (current_distance_travelled, instant_velocity,
        time_counter, time_step) = utils.run_static_simulation(destination_total_distance_km, craft_acceleration)

    # if the user has selected only a static simulation, run the code from iteration 1
    if only_static is True:
        # tell the user the half way point has been reached
        print('\nATTENTION: The Half-way point has been reached.\n')

        # display the time taken to reach the half way point in years, months, weeks, days, hours, minutes and seconds
        print(f'Time taken to reach the half way point:')
        time_counter.print()

        # display the craft's instant (present) velocity in meters per second, kilometers per second and kilometers per hour at the half way point
        print(
            f'\nCraft instant (present) velocity: {instant_velocity:.2f} m/2 ({utils.ms_to_kmps(instant_velocity):.2f} km/s, {utils.ms_to_kmph(instant_velocity):.2f} km/h)\n')

        # display the distance travelled in kilometers and meters
        print(
            f'Distance travelled: {current_distance_travelled:.2f} Km ({utils.km_to_meters(current_distance_travelled):.2f} m)\n')

        # calculate the distance left to travel and display it in kilometers and meters
        distance_left = destination_total_distance_km - current_distance_travelled
        print(
            f'Distance left to travel: {distance_left:.2f} Km ({utils.km_to_meters(distance_left):.2f} m)\n')

        # display the half way velocity as a percentage of light speed
        print(
            f'Half way velocity percentage: {utils.percentage(instant_velocity, SPEED_OF_LIGHT):.2f}% of light-speed\n')

        # display the kinetic energy of the craft at the half way point
        print(
            f'Craft kinetic energy: {utils.kinetic_energy(vehicle_mass, instant_velocity):.2f}\n')

        # calculate the estimated total travel time and display it in years, months, weeks, days, hours, minutes and seconds
        print(f'Estimated total time to reach the destination:')
        estimated_total_travel_time_seconds = utils.time_from_distance_and_speed(
            destination_total_distance_m, INITIAL_LAUNCH_VELOCITY)
        print(time_counter.calculate_from_seconds(
            estimated_total_travel_time_seconds))

        print('\n--------------------------------------------------------------------------------------')
    # if the user has not selected only a static simulation, run the code for that includes the destinations orbit into the equation
    else:
        # get the total travel time from the static simulation then display it
        total_travel_time = time_counter.total_time
        print(f'Total travel time: {total_travel_time}')

        # calculate the orbitral circumference of the destination and convert it from AU to kilometres then display it
        orbital_circumference = utils.orbital_circumference(
            utils.au_to_kilometers(selected_destination.au_distance))
        print(
            f'Destination Orbital Circumference: {orbital_circumference:.2f} Km')

        # display the destination's orbital period in years and days
        print(
            f'Orbital period: {selected_destination.orbital_period / utils.DAYS_IN_A_YEAR:.2f} years ({selected_destination.orbital_period} days)')

        # convert the orbital period to seconds and display it
        orbital_time = utils.orbital_period_seconds(
            selected_destination.orbital_period)
        print(f'Orbital time: {orbital_time} seconds')

        # calculate the destination's orbital velocity from the orbital circumference and orbital period in seconds then display it
        destination_orbital_velocity = utils.calc_orbital_velocity(
            orbital_circumference, orbital_time)
        print(
            f'Destination orbital velocity: {destination_orbital_velocity:.2f} km/2 ({utils.kmps_to_ms(destination_orbital_velocity):.2f} m/s)')

        # calculate the probes flight time from the total static distance to the destination and the probes's acceleration then display it
        probe_flight_time = utils.time_from_distance_and_speed(
            destination_total_distance_km, craft_acceleration)
        print(f'Probe flight time: {probe_flight_time:.2f} seconds')

        # probe_flight_time = total_travel_time

        # calculate the destination's distance travelled in kilometres and display it
        destination_km_travelled = destination_orbital_velocity * probe_flight_time
        print(f'Destination km travelled: {destination_km_travelled:.2f} km')

        # calculate the kilometres per degree from the orbital circumference
        km_per_degree = utils.km_per_degree(orbital_circumference)

        # calculate the angular offset in degrees from the destination's distance travelled and the kilometres per degree then display it
        angular_offset_degrees = utils.angular_degrees(
            destination_km_travelled, km_per_degree)
        print(
            f'Angular offset degrees: {angular_offset_degrees:.2f} degrees')

        # convert the angular offset from degrees to radians and display it again
        angular_offset_radians = utils.degrees_to_radians(
            angular_offset_degrees)
        print(
            f'Angular offset radians: {angular_offset_radians:.2f} radians')

        lateral_velocity = utils.calc_instant_acceleration(
            utils.kmps_to_ms(destination_orbital_velocity), total_travel_time)
        print(f'Lateral velocity: {lateral_velocity:.2f} m/2')

        probe_momentum = utils.momentum(vehicle_mass, lateral_velocity)
        print(f'Probe actual sideways momentum: {probe_momentum:.2f} m/2')

        earth_movement = utils.earth_movement(total_travel_time)
        print(f'Earth moved {earth_movement:.2f} AU during the probes flight')

    # ask the user if they would like to calculate another Destination, if 'N' is entered the application will close.
    choice = input(
        '\nWould you like to calculate another Destination? (Y/N): ')
    if choice.lower() == 'n':
        break
