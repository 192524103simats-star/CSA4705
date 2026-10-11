import numpy as np
steps = np.array([
    5000, 6000, 7500, 8000, 6500, 9000, 7000,
    8500, 9500, 6000, 7200, 8100, 7600, 8800,
    9200, 6800, 7400, 8300, 7900, 9600, 8700,
    6500, 7100, 8200, 9000, 7700, 8600, 9400,
    7300, 8900
])
first_week = steps[:7]
last_five = steps[-5:]
alternate = steps[::2]
reversed_steps = steps[::-1]
print("First Week:", first_week)
print("Last 5 Days:", last_five)
print("Every Alternate Day:", alternate)
print("Reversed Vector:", reversed_steps)
print("Lengths:", len(first_week), len(last_five),
      len(alternate), len(reversed_steps))
