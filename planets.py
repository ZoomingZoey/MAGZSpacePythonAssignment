
class Planet:
    def __init__(self, name, au_distance_from_sun):
        self.name = name
        self.au_distance = au_distance_from_sun


planets = [
    Planet('Mars', 1.5),
    Planet('Venus', 0.7),
    Planet('Mercury', 0.4),
    Planet('Neptune', 30),
    Planet('Jupiter', 5.2)
]
