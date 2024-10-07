import random
import math

def estimate_pi(precision):
    Nhits = 0  # Number of points inside the circle
    Ntot = 0   # Total number of points
    Pi_Est = 0 # Estimated value of Pi

    while True:
        for i in range(10000):  # Generate 10,000 random points
            x = random.random()
            y = random.random()

            if x*x + y*y <= 1:  # Check if the point is inside the unit circle
                Nhits += 1

            Ntot += 1

        Pi_Est = 4 * Nhits / Ntot  # Estimate Pi using the ratio of points

        if abs(Pi_Est - math.pi) < 10**(-(precision+1)):  # Check if the estimate is within the desired precision
            break
    
    return Pi_Est

print(estimate_pi(3))  # Estimate Pi to 3 decimal places