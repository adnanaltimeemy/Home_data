import matplotlib.pyplot as plt
import numpy as np

# Years from 1995 to 2025
years = np.arange(1995, 2026)

# Sample data: Youth homelessness presentations (in thousands)
# Approximate and illustrative (you can replace with real data)
youth_homelessness = [
    20, 21, 22, 23, 24, 25, 27, 29, 30, 32,   # 1995-2004 slow rise
    35, 38, 42, 48, 55, 60, 65, 70, 80, 85,   # 2005-2014 steeper rise (recession impact)
    90, 95, 100, 105, 110, 115, 118, 118, 118, 118, 118  # 2015-2025 plateau
]

# Sample data: Youth homeownership % (ages 25-34)
# Approximate, downward trend
youth_homeownership = [
    65, 64, 63, 62, 60, 58, 55, 52, 50, 48,   # 1995-2004 gradual decline
    45, 42, 38, 34, 30, 27, 24, 21, 18, 15,   # 2005-2014 faster decline
    13, 12, 11, 10, 10, 10, 10, 10, 10, 10, 10  # 2015-2025 stabilizing low
]

plt.figure(figsize=(12, 6))
plt.title("Youth Homelessness and Homeownership in the UK (1995-2025)")
plt.plot(years, youth_homelessness, label="Youth Homelessness Presentations (thousands)", color="red", linewidth=2)
plt.ylabel("Homelessness (thousands)", color="red")
plt.tick_params(axis='y', labelcolor="red")

plt2 = plt.twinx()
plt2.plot(years, youth_homeownership, label="Youth Homeownership Rate (%)", color="blue", linewidth=2)
plt2.set_ylabel("Homeownership Rate (%)", color="blue")
plt2.tick_params(axis='y', labelcolor="blue")

plt.grid(True)
plt.show()
