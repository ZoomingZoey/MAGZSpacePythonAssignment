
class Planet:
    def __init__(self, name, au_distance_from_sun, orbital_period_days):
        self.name = name
        self.au_distance = au_distance_from_sun
        self.orbital_period = orbital_period_days


planets = [
    Planet('Mars', 1.5, 687),
    Planet('Venus', 0.7, 225),
    Planet('Mercury', 0.4, 88),
    Planet('Neptune', 30, 60_266.25),
    Planet('Jupiter', 5.2, 4_383),
    Planet('Saturn', 9.5, 10_592.25),
    Planet('Uranus', 19.8, 30_681),
    Planet('Pluto', 39, 90_582),
    Planet('Eris', 68, 203_809.5),
    Planet('Earth', 1, 365.25)
]
