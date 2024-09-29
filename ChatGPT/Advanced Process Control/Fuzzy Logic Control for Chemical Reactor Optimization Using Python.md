**Python Implementation:**

We’ll use the skfuzzy library for fuzzy logic control. If you don’t have the library, install it with pip install scikit-fuzzy.

```
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables for the reactor system
temperature = ctrl.Antecedent(np.arange(200, 500, 1), 'temperature')
pressure = ctrl.Antecedent(np.arange(0, 20, 1), 'pressure')
reaction_rate = ctrl.Consequent(np.arange(0, 100, 1), 'reaction_rate')

# Define fuzzy membership functions for temperature
temperature['low'] = fuzz.trimf(temperature.universe, [200, 200, 300])
temperature['medium'] = fuzz.trimf(temperature.universe, [250, 350, 450])
temperature['high'] = fuzz.trimf(temperature.universe, [400, 500, 500])

# Define fuzzy membership functions for pressure
pressure['low'] = fuzz.trimf(pressure.universe, [0, 0, 7])
pressure['medium'] = fuzz.trimf(pressure.universe, [5, 10, 15])
pressure['high'] = fuzz.trimf(pressure.universe, [12, 20, 20])

# Define fuzzy membership functions for reaction rate
reaction_rate['slow'] = fuzz.trimf(reaction_rate.universe, [0, 0, 30])
reaction_rate['moderate'] = fuzz.trimf(reaction_rate.universe, [20, 50, 80])
reaction_rate['fast'] = fuzz.trimf(reaction_rate.universe, [70, 100, 100])

# Visualize membership functions
temperature.view()
pressure.view()
reaction_rate.view()

# Define fuzzy rules
rule1 = ctrl.Rule(temperature['low'] & pressure['low'], reaction_rate['slow'])
rule2 = ctrl.Rule(temperature['medium'] & pressure['medium'], reaction_rate['moderate'])
rule3 = ctrl.Rule(temperature['high'] & pressure['high'], reaction_rate['fast'])
rule4 = ctrl.Rule(temperature['medium'] & pressure['low'], reaction_rate['moderate'])
rule5 = ctrl.Rule(temperature['low'] & pressure['high'], reaction_rate['slow'])

# Create the fuzzy control system
reactor_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
reactor_sim = ctrl.ControlSystemSimulation(reactor_ctrl)

# Simulate reactor dynamics
time = np.linspace(0, 10, 100)  # Simulation time
temp_values = 300 + 50 * np.sin(0.5 * time)  # Simulated temperature changes
pressure_values = 10 + 5 * np.sin(0.3 * time)  # Simulated pressure changes
reaction_rates = []

for t, temp, pres in zip(time, temp_values, pressure_values):
    reactor_sim.input['temperature'] = temp
    reactor_sim.input['pressure'] = pres
    reactor_sim.compute()
    reaction_rates.append(reactor_sim.output['reaction_rate'])

# Plot simulation results
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(time, temp_values, 'r', label='Temperature (°C)')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(time, pressure_values, 'b', label='Pressure (bar)')
plt.xlabel('Time (s)')
plt.ylabel('Pressure (bar)')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(time, reaction_rates, 'g', label='Reaction Rate (%)')
plt.xlabel('Time (s)')
plt.ylabel('Reaction Rate (%)')
plt.legend()

plt.tight_layout()
plt.show()
```

**Explanation of Code:**

	1.	Defining Fuzzy Variables:
	•	The fuzzy variables temperature, pressure, and reaction_rate are defined with their respective ranges and membership functions.
	•	For example, the reactor temperature is defined with three linguistic categories: “low”, “medium”, and “high”.
	2.	Creating Membership Functions:
	•	Membership functions are defined using fuzz.trimf for triangular membership functions.
	•	These functions map the input values to fuzzy values (0 to 1) based on the defined ranges.
	3.	Defining Fuzzy Rules:
	•	Fuzzy rules are created to define the control strategy, such as:
	•	If temperature is “low” and pressure is “low”, then the reaction rate is “slow”.
	•	These rules encode expert knowledge about the system.
	4.	Fuzzy Inference System:
	•	The ctrl.ControlSystem is used to build the fuzzy control system using the defined rules.
	•	The ctrl.ControlSystemSimulation class is used to simulate the fuzzy logic control in real-time.
	5.	Simulation:
	•	The reactor is simulated over a period of 10 seconds with sinusoidal changes in temperature and pressure.
	•	The FLC adjusts the reaction rate based on the inputs.
	6.	Visualization:
	•	The results are plotted to show the time evolution of temperature, pressure, and reaction rate.

 
