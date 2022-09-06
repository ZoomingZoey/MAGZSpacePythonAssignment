
from constants import *
import math

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

def instant_velocity(acceleration , time):
  '''Returns the instant velocity for a given acceleration and time'''
  return acceleration * time

def instant_acceleration(velocity , time):
  '''Returns the instant acceleration for a given velocity and time'''
  return velocity / time

def instant_time(velocity , acceleration):
  '''Returns the instant time for a given velocity and acceleration'''
  return velocity / acceleration

def distance_travelled(time, acceleration):
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

def ms_to_kmph(ms):
  '''Converts and returns meters per seconds in kilometers per hour'''
  return ms * ONE_MS_IN_KMPH

def kinetic_energy(mass, velocity):
  '''Returns the kinetic energy from a given mass and velocity'''
  return (0.5 * mass) * (velocity ** 2)

def percentage(number, percentage):
  '''Returns a percentage of a number'''
  return (number * percentage) / 100

