
class Asteroid:
    def __init__(self, name, au_distance_from_sun, orbital_period_days):
        self.name = name
        self.au_distance = au_distance_from_sun
        self.orbital_period = orbital_period_days


asteroids = [
    Asteroid('Ceres', 2.766, 1_682),
    Asteroid('Vesta', 2.362, 1_325),
    Asteroid('Pallas', 2.773, 1_686)
]
