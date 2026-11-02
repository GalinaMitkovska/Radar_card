import numpy as np
import matplotlib.pyplot as plt

from radar_cls import Radar

def main():
    np.random.seed(42)

    matrix = (
            np.random.randn(32, 32) +
            1j * np.random.randn(32, 32)
    )

    matrix[9, 12] += 4 + 4j
    matrix[15, 20] += 6 + 6j

    radar = Radar()
    detections = radar.radar_detector(matrix)
    detected_position = np.argwhere(detections)
    print(detected_position)

    power_matrix = np.abs(matrix) ** 2

    plt.figure(figsize=(10, 6))

    plt.imshow(
        10 * np.log10(power_matrix + 1e-10),
        origin="lower",
        aspect="auto",
        cmap="viridis"
    )

    plt.scatter(
        detected_position[:, 1],
        detected_position[:, 0],
        color="red",
        marker="x",
        label="Detected targets"
    )

    plt.xlabel("Doppler")
    plt.ylabel("Range")
    plt.title("Radar Detection")
    plt.colorbar(label="Power (dB)")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()