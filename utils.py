
from constants import *
import math
import time_counter as tc
from planets import planets


def force(mass, acceleration):
    '''Returns the Force in Newtons from a Mass in Kilograms and an Acceleration in Meters per Second.'''
    return mass * acceleration


def acceleration(force, mass):
    '''Returns the Acceleration in Meters per Second from a Force in Newtons and a Mass in Kilograms.'''
    return force / mass


def mass(force, acceleration):
    '''Returns the Mass in Kilograms from a Force in Newtons and an Acceleration in Meters per Second.'''
    return force / acceleration


def find(pred, iterable):
    for element in iterable:
        if pred(element):
            return element
    return None


def calculate_destination_au_distance(destination_au):
    '''Returns the distance from earth to a destination planet in AU's'''
    # if the planet is inside earth's orbit, meaning they are closer to the sun then earth's AU distance will be greater than the planets AU distance
    if EARTH_AU_DISTANCE > destination_au:
        return EARTH_AU_DISTANCE - destination_au

    # if the planet is outside earth's orbit, meaning they are further from the sun then earth's AU distance will be less than the planets AU distance
    return destination_au - EARTH_AU_DISTANCE


def au_to_kilometers(au_value):
    '''Converts and returns an AU value in Kilometers'''
    return au_value * ONE_AU_DISTANCE_KM


def newtons_to_kilogram_force(newtons):
    '''Converts and returns Newtons in Kilogram-force'''
    return newtons * ONE_KILOGRAM_FORCE_KG


def calc_instant_velocity(acceleration, time):
    '''Returns the instant velocity for a given acceleration and time'''
    return acceleration * time


def calc_instant_acceleration(velocity, time):
    '''Returns the instant acceleration for a given velocity and time'''
    return velocity / time


def calc_instant_time(velocity, acceleration):
    '''Returns the instant time for a given velocity and acceleration'''
    return velocity / acceleration


def calc_distance_travelled(time, acceleration):
    '''Returns the distance travelled for a given time and acceleration'''
    return math.pow(time, 2) * (acceleration / 2)


def time_from_distance_and_speed(distance, speed):
    '''Returns the time taken to travel a given distance in meters at a given speed'''
    return distance / speed


def km_to_meters(distance):
    '''Converts and returns a kilometer distance in meters'''
    return distance * ONE_KM_DISTANCE_M


def ms_to_kmps(ms):
    '''Converts and returns meters per seconds in kilometers per second'''
    return ms / ONE_KMPS_IN_MS


def kmps_to_ms(kmps):
    '''Converts and returns kilometers per second in meters per second'''
    return kmps * ONE_KMPS_IN_MS


def ms_to_kmph(ms):
    '''Converts and returns meters per seconds in kilometers per hour'''
    return ms * ONE_MS_IN_KMPH


def kinetic_energy(mass, velocity):
    '''Returns the kinetic energy from a given mass and velocity'''
    return (0.5 * mass) * (velocity ** 2)


def percentage(number, percentage):
    '''Returns a percentage of a number'''
    return (number * percentage) / 100


def prompt_destination(destination_names):
    '''Prompts the user for a destination based on a given list'''
    # create a variable to hold the destination name
    destination_name = str()

    # create a while True loop to simulate a do-while loop so that the user will continually be asked for a valid destination name if an invalid one is entered
    while True:
        # prompt for the input
        destination_name = input('\nDestination: ')

        # if the destination exists break out of the loop
        if destination_name.lower() in destination_names:
            break

        print('\nInvalid Destination. Please enter a destination name from the list.')

    # return the value
    return destination_name


def prompt_thrust_force():
    '''Prompts the user for a thrust force in newtons'''
    # create a variable to hold the thrust force
    thrust_force_newtons = int()

    # create a while True loop to simulate a do-while loop so that the user will continually be asked for a thrust value if the value entered is not a number
    while True:
        try:
            # try prompt for the input
            thrust_force_input = int(input(
                f'\nPlease enter the thrust force in Newtons between {MIN_THRUST_FORCE_N}N and {MAX_THRUST_FORCE_N}N: '))

            if thrust_force_input < MIN_THRUST_FORCE_N or thrust_force_input > MAX_THRUST_FORCE_N:
                raise ValueError

            thrust_force_newtons = thrust_force_input
            break
        except ValueError:
            print(
                f'\nThrust force must be a positive integer value between {MIN_THRUST_FORCE_N} and {MAX_THRUST_FORCE_N}.')

    # return the value
    return thrust_force_newtons


def prompt_vehicle_mass():
    '''Prompts the user for a vehicle mass in kilograms'''
    # create a variable to hold the vehicle mass
    vehicle_mass = int()

    # create a while True loop to simulate a do-while loop so that the user will continually be asked for a vehicle mass value if the value entered is not a number
    while True:
        try:
            # prompt for the input
            vehicle_mass_input = int(input(
                f'\nPlease enter the Vehicle mass in Kilograms between {MIN_VEHICLE_WEIGHT_KG}Kg and {MAX_VEHICLE_WEIGHT_KG}Kg: '))

            if vehicle_mass_input < MIN_VEHICLE_WEIGHT_KG or vehicle_mass_input > MAX_VEHICLE_WEIGHT_KG:
                raise ValueError

            vehicle_mass = vehicle_mass_input
            break
        except ValueError:
            print(
                f'\nVehicle mass must be a positive integer value between {MIN_VEHICLE_WEIGHT_KG} and {MAX_VEHICLE_WEIGHT_KG}.')

    # return the value
    return vehicle_mass


def run_static_simulation(destination_distance, craft_acceleration):
    # begin running the calculation
    current_distance_travelled = 0
    half_way_point = destination_distance / 2
    time_step = 0
    instant_velocity = 0
    time_counter = tc.TimeCounter()

    # use a while loop to calculate the distance and velocity while we are less than the destination's half way point
    while current_distance_travelled < half_way_point:
        # derive the instant velocity for each time increment
        instant_velocity = calc_instant_velocity(craft_acceleration, time_step)

        # derive the distance travelled so far for each time increment in seconds
        current_distance_travelled = calc_distance_travelled(
            time_step, craft_acceleration)

        # increment the time step and time counter
        time_counter.increment()
        time_step += 1

    # return the data as a tuple
    return (current_distance_travelled, instant_velocity, time_counter, time_step)


def prompt_only_static():
    '''Prompts the user wether they want to run only a static simulation'''
    # create a variable to hold the value
    only_static = False

    # create a while True loop to simulate a do-while loop so that the user will continually be asked for a thrust value if the value entered is not a number
    while True:
        # prompt for the input
        option = input(
            f'\nDo you want to run only a static simulation? (Y/N): ')

        if option.lower() == 'y':
            only_static = True
            break
        elif option.lower() == 'n':
            break

    # return the value
    return only_static


def orbital_circumference(radius):
    '''Returns the orbital circumference of a given radius'''
    return 2 * radius * math.pi


def km_per_degree(circumference):
    '''Returns the kilometres per degree for a given circumference'''
    return circumference / 360


def orbital_period_seconds(orbital_period_days):
    '''Returns the orbital period in seconds from a orbital period given in days'''
    return orbital_period_days * SECONDS_IN_A_DAY


def calc_orbital_velocity(circumference, time):
    '''Returns the orbital velocity from a given circumference and time'''
    return circumference / time


def angular_degrees(km_travelled, km_per_degree):
    '''Returns the angular degrees travelled from a given km distance travelled and km per degrees'''
    return km_travelled / km_per_degree


def degrees_to_radians(degrees):
    '''Converts and returns degrees as radians'''
    return degrees * (math.pi / 180)


def radians_to_degrees(radians):
    '''Converts and returns radians as degrees'''
    return radians * (180 / math.pi)


def momentum(mass, velocity):
    '''Returns the momentum from a given mass and velocity'''
    return mass * velocity


def time_to_days(time):
    '''Converts a time in seconds to days'''
    return time / SECONDS_IN_A_DAY + 30


def earth_movement(time):
    '''Calculates Earth's movement'''
    earth_obj = find(lambda v: v.name == 'Earth', planets)
    earth_orbital_circ = orbital_circumference(earth_obj.au_distance)
    time_in_days = time_to_days(time)
    distance_moved = (earth_orbital_circ * time_in_days) / DAYS_IN_A_YEAR
    return distance_moved
