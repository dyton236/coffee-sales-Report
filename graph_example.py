import matplotlib.pyplot as plt

# Data for average monthly temperature (in °C) for a city
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [15, 17, 21, 26, 30, 33, 32, 31, 29, 25, 20, 16]

# Create a line graph
plt.plot(months, temperature, marker='o', color='orange', linestyle='-', linewidth=2, markersize=6)

# Add labels and title
plt.title("Average Monthly Temperature of a City")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")

# Show grid
plt.grid(True)

# Display the graph
plt.show()