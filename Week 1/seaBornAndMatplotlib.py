import matplotlib.pyplot as plt
import seaborn as sns

# Simple line plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)  # Draw the line plot
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Line Plot")
plt.show()  # Display the plot
