from Clases import Alien
import random
import math

for index in range(1, math.floor(random.random() * 20 + 2)):
    print(f"Alien {index}")
    Alien(f"Alien {index}")


print(Alien.getNumberOfAliens())
