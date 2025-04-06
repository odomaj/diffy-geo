import matplotlib.pyplot as plt
import numpy as np


def gen_points(stop: np.float64, count: np.int64):
    increment: np.float64 = stop / count

    dog_position = np.array([0, 1], dtype=np.float64)
    owner_position = np.array([0, 0], dtype=np.float64)

    dog_velocity = np.array([0, 0], dtype=np.float64)
    owner_velocity = np.array([1, 0], dtype=np.float64)

    dog_positions = [dog_position]
    for i in range(count):
        owner_position += owner_velocity * increment
        dog_velocity = dog_position - owner_position
        dog_velocity = dog_velocity / np.sqrt(
            np.dot(dog_velocity, dog_velocity)
        )
        dog_position = owner_position + dog_velocity
        dog_positions.append(dog_position)

    return dog_positions


def plot(points):
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, marker="o", linestyle="-", color="b")

    # Add labels and title
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Plot of Points")

    # Display the plot
    plt.show()


if __name__ == "__main__":
    plot(gen_points(np.float64(5), np.int64(1000)))
