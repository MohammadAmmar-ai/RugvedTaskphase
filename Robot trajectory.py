import math
import matplotlib.pyplot as plt

x = 0.0
y = 0.0
theta = 0.0

x_history = [x]
y_history = [y]
theta_history = [theta]

def execute_command(command_text):
    global x, y, theta

    initial_pos = (round(x, 2), round(y, 2), round(theta, 2))

    parts = command_text.split()
    action = parts[0]
    value = float(parts[1])

    if action == "forward":
        theta_radians = math.radians(theta)
        x = x + value * math.cos(theta_radians)
        y = y + value * math.sin(theta_radians)
    elif action == "left":
        theta = theta + value
    elif action == "right":
        theta = theta - value
    else:
        print("Unknown command:", action)

    final_pos = (round(x, 2), round(y, 2), round(theta, 2))
    print("Initial Pos:", initial_pos, "| Executing:", command_text, "| Final Pos:", final_pos)

    x_history.append(x)
    y_history.append(y)
    theta_history.append(theta)


print("Enter motion commands one per line (forward <val> / left <val> / right <val>).")
print("Type 'done' when finished.")

while True:
    user_input = input("Command: ")
    if user_input == "done":
        break
    execute_command(user_input)

plt.figure(figsize=(7, 7))
plt.plot(x_history, y_history, marker='o', linestyle='-')
plt.plot(x_history[0], y_history[0], marker='s', color='green', markersize=12, label='Start')
plt.plot(x_history[-1], y_history[-1], marker='s', color='red', markersize=12, label='End')

for i in range(len(x_history)):
    angle_rad = math.radians(theta_history[i])
    dx = math.cos(angle_rad)
    dy = math.sin(angle_rad)
    plt.quiver(x_history[i], y_history[i], dx, dy, angles='xy', scale_units='xy', scale=1.5, color='blue')

plt.title("Robot Trajectory (Discrete Motion)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()