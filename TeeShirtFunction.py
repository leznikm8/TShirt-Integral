'''
Created on 28 August 2025

@author: Dr. Mike
'''
import numpy as np

def evaluate_tee_shirt_optimized(n, num_simulation_trials, num_integral_samples):
    max_radius = np.sqrt(3.0 / (n * np.pi))
    total_integral_estimate = 0.0

    for _ in range(num_simulation_trials):
        # Generate random centers and radii
        centers = np.random.rand(n, 2)  # shape (n, 2)
        radii = np.random.rand(n) * max_radius  # shape (n,)

        # Generate random sample points
        samples = np.random.rand(num_integral_samples, 2)  # shape (num_integral_samples, 2)

        # Compute squared distances from each sample to each center
        diff = samples[:, np.newaxis, :] - centers[np.newaxis, :, :]  # shape (samples, centers, 2)
        dist_squared = np.sum(diff ** 2, axis=2)  # shape (samples, centers)

        # Check if each sample is inside each circle
        inside = dist_squared <= radii**2  # shape (samples, centers)

        # Count how many circles each sample is inside
        count_inside = np.sum(inside, axis=1)  # shape (samples,)

        # Apply mod 2 and average
        integral_estimate = np.mean(count_inside % 2)
        total_integral_estimate += integral_estimate

    return total_integral_estimate / num_simulation_trials

# Example usage
if __name__ == "__main__":
    n_value = 1000
    num_simulation_trials = 1000
    num_integral_samples = 1000

    result = evaluate_tee_shirt_optimized(n_value, num_simulation_trials, num_integral_samples)
    print(f"Approximated value of the expression on Tee Shirt: {result}")


