import math
import matplotlib.pyplot as plt

x = 0.0
y = 0.0
theta = 0.0
dt = 0.1

x_history = [x]
y_history = [y]

def execute_velocity_command(v, omega, duration):
    global x, y, theta

    print("Before command -> x:", round(x,2), "y:", round(y,2), "theta:", round(math.degrees(theta),2))

    steps = int(duration / dt)
    for step in range(steps):
        x = x + v * math.cos(theta) * dt
        y = y + v * math.sin(theta) * dt
        theta = theta + omega * dt
        x_history.append(x)
        y_history.append(y)

    print("After command  -> x:", round(x,2), "y:", round(y,2), "theta:", round(math.degrees(theta),2))
    print()


print("Enter velocity commands as: v omega duration")
print("Example: 2 0.5 3   (means v=2, omega=0.5, for 3 seconds)")
print("Type 'done' when finished.")

while True:
    user_input = input("Command: ")
    if user_input == "done":
        break
    parts = user_input.split()
    v = float(parts[0])
    omega = float(parts[1])
    duration = float(parts[2])
    execute_velocity_command(v, omega, duration)

plt.figure(figsize=(7,7))
plt.plot(x_history, y_history, linestyle='-')
plt.plot(x_history[0], y_history[0], marker='s', color='green', markersize=12, label='Start')
plt.plot(x_history[-1], y_history[-1], marker='s', color='red', markersize=12, label='End')
plt.title("Robot Trajectory (Continuous Unicycle Model)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()