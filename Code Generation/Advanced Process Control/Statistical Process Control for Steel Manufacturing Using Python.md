**Solution Approach:**

	1.	Implement Control Charts:
	•	Use X-bar and R charts for variables such as tensile strength and thickness.
	•	Use P charts or C charts for attributes such as surface finish defects.
	2.	Develop Real-Time Monitoring:
	•	Continuously calculate control limits and update charts.
	•	Implement rules for detecting out-of-control conditions.
	3.	Simulate Steel Manufacturing Process:
	•	Generate synthetic data to simulate a steel production line with random variations.
	•	Use SPC tools to monitor the simulated data and trigger alarms.

**Python Implementation:**
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters for the simulation
np.random.seed(42)
num_samples = 100  # Number of samples for simulation
sample_size = 5    # Number of observations in each sample

# Simulated process data for tensile strength (in MPa), thickness (in mm), and surface defects (count)
tensile_strength = np.random.normal(loc=450, scale=10, size=(num_samples, sample_size))
thickness = np.random.normal(loc=5.0, scale=0.2, size=(num_samples, sample_size))
surface_defects = np.random.poisson(lam=2, size=(num_samples, sample_size))

# Calculate X-bar and R values for tensile strength and thickness
xbar_tensile = np.mean(tensile_strength, axis=1)
range_tensile = np.max(tensile_strength, axis=1) - np.min(tensile_strength, axis=1)
xbar_thickness = np.mean(thickness, axis=1)
range_thickness = np.max(thickness, axis=1) - np.min(thickness, axis=1)

# Calculate control limits for X-bar and R charts
A2, D3, D4 = 0.577, 0.0, 2.114  # Constants for X-bar and R charts (sample size = 5)
central_line_xbar_tensile = np.mean(xbar_tensile)
central_line_range_tensile = np.mean(range_tensile)
UCL_xbar_tensile = central_line_xbar_tensile + A2 * central_line_range_tensile
LCL_xbar_tensile = central_line_xbar_tensile - A2 * central_line_range_tensile
UCL_range_tensile = D4 * central_line_range_tensile
LCL_range_tensile = D3 * central_line_range_tensile

central_line_xbar_thickness = np.mean(xbar_thickness)
central_line_range_thickness = np.mean(range_thickness)
UCL_xbar_thickness = central_line_xbar_thickness + A2 * central_line_range_thickness
LCL_xbar_thickness = central_line_xbar_thickness - A2 * central_line_range_thickness
UCL_range_thickness = D4 * central_line_range_thickness
LCL_range_thickness = D3 * central_line_range_thickness

# Plot control charts for tensile strength
plt.figure(figsize=(12, 10))
plt.subplot(2, 1, 1)
plt.plot(xbar_tensile, marker='o', linestyle='-', color='b', label='X-bar')
plt.axhline(central_line_xbar_tensile, color='green', linestyle='--', label='Central Line')
plt.axhline(UCL_xbar_tensile, color='red', linestyle='--', label='UCL')
plt.axhline(LCL_xbar_tensile, color='red', linestyle='--', label='LCL')
plt.title('X-bar Control Chart for Tensile Strength')
plt.xlabel('Sample Number')
plt.ylabel('Tensile Strength (MPa)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(range_tensile, marker='o', linestyle='-', color='b', label='Range')
plt.axhline(central_line_range_tensile, color='green', linestyle='--', label='Central Line')
plt.axhline(UCL_range_tensile, color='red', linestyle='--', label='UCL')
plt.axhline(LCL_range_tensile, color='red', linestyle='--', label='LCL')
plt.title('Range Control Chart for Tensile Strength')
plt.xlabel('Sample Number')
plt.ylabel('Range (MPa)')
plt.legend()
plt.tight_layout()
plt.show()

# Plot control charts for thickness
plt.figure(figsize=(12, 10))
plt.subplot(2, 1, 1)
plt.plot(xbar_thickness, marker='o', linestyle='-', color='b', label='X-bar')
plt.axhline(central_line_xbar_thickness, color='green', linestyle='--', label='Central Line')
plt.axhline(UCL_xbar_thickness, color='red', linestyle='--', label='UCL')
plt.axhline(LCL_xbar_thickness, color='red', linestyle='--', label='LCL')
plt.title('X-bar Control Chart for Thickness')
plt.xlabel('Sample Number')
plt.ylabel('Thickness (mm)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(range_thickness, marker='o', linestyle='-', color='b', label='Range')
plt.axhline(central_line_range_thickness, color='green', linestyle='--', label='Central Line')
plt.axhline(UCL_range_thickness, color='red', linestyle='--', label='UCL')
plt.axhline(LCL_range_thickness, color='red', linestyle='--', label='LCL')
plt.title('Range Control Chart for Thickness')
plt.xlabel('Sample Number')
plt.ylabel('Range (mm)')
plt.legend()
plt.tight_layout()
plt.show()

# Plot defect counts for surface finish
surface_defects_total = np.sum(surface_defects, axis=1)
UCL_defects = np.mean(surface_defects_total) + 3 * np.std(surface_defects_total)
LCL_defects = np.mean(surface_defects_total) - 3 * np.std(surface_defects_total)

plt.figure(figsize=(10, 6))
plt.plot(surface_defects_total, marker='o', linestyle='-', color='b', label='Defect Count')
plt.axhline(np.mean(surface_defects_total), color='green', linestyle='--', label='Central Line')
plt.axhline(UCL_defects, color='red', linestyle='--', label='UCL')
plt.axhline(LCL_defects, color='red', linestyle='--', label='LCL')
plt.title('Control Chart for Surface Defects')
plt.xlabel('Sample Number')
plt.ylabel('Number of Defects')
plt.legend()
plt.grid()
plt.show()

# Display control limits for all charts
print("Tensile Strength Control Limits (MPa): X-bar UCL =", round(UCL_xbar_tensile, 2), ", LCL =", round(LCL_xbar_tensile, 2))
print("Tensile Strength Range Control Limits (MPa): UCL =", round(UCL_range_tensile, 2), ", LCL =", round(LCL_range_tensile, 2))
print("Thickness Control Limits (mm): X-bar UCL =", round(UCL_xbar_thickness, 2), ", LCL =", round(LCL_xbar_thickness, 2))
print("Thickness Range Control Limits (mm): UCL =", round(UCL_range_thickness, 2), ", LCL =", round(LCL_range_thickness, 2))
print("Surface Defects Control Limits: UCL =", round(UCL_defects, 2), ", LCL =", round(LCL_defects, 2))
```

**Explanation of Code:**

	1.	Simulated Data Generation:
	•	Synthetic data for tensile strength, thickness, and surface defects is generated to simulate a steel manufacturing process.
	2.	Calculating Control Limits:
	•	X-bar and Range charts are calculated for tensile strength and thickness to monitor process stability.
	•	Control limits for surface defects are calculated using the mean ± 3 standard deviations.
	3.	Control Chart Plotting:
	•	X-bar and Range charts for tensile strength and thickness show whether the process is within control limits.
	•	Surface defect charts indicate whether the defect count is stable.
	4.	Displaying Control Limits:
	•	Control limits are printed for reference, showing the boundaries for each quality metric.
