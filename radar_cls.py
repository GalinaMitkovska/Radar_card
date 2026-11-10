import numpy as np

class Radar:
    def __init__(self):
        self.range_guard = 2
        self.doppler_guard = 1
        self.range_training = 5
        self.doppler_training = 4
        self.pfa = 0.001



    def calculate_N(self):
        total_rows = 2 * (self.range_guard + self.range_training) + 1
        total_cols = 2 * (self.doppler_guard + self.doppler_training) + 1

        guard_rows = 2 * self.range_guard + 1
        guard_cols = 2 * self.doppler_guard + 1

        N = total_rows * total_cols - guard_rows * guard_cols

        return N


    def calculate_alpha(self, N):
        alpha = N * (self.pfa **(-1/N) -1)
        return alpha

    def radar_detector(self, matrix):
        power_matrix = np.abs(matrix) ** 2

        range_radius = self.range_guard + self.range_training
        doppler_radius = self.doppler_guard + self.doppler_training
        rows, cols = power_matrix.shape

        detections = np.zeros((rows, cols), dtype=bool)

        N = self.calculate_N()
        alpha = self.calculate_alpha(N)

        for i in range(range_radius, rows - range_radius):
            for j in range(doppler_radius, cols - doppler_radius):

                window = power_matrix[i - range_radius: i + range_radius + 1,
                j - doppler_radius: j + doppler_radius + 1].copy()

                window[self.range_training: self.range_training + 2 * self.range_guard + 1,
                self.doppler_training: self.doppler_training + 2 * self.doppler_guard + 1] = np.nan

                noise_power = np.nanmean(window)

                threshold = alpha * noise_power

                if power_matrix[i, j] > threshold:
                    detections[i, j] = True

        return detections





