**1.Conveyor Belt Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a conveyor belt system with three stations, where each station allows a user to stop the conveyor. The system should automatically start and stop based on input from five sensors that detect the presence of objects on the conveyor. The conveyor belt speed must be maintained at 2 meters per second. The program should manage both manual and automatic control modes while ensuring safe and efficient operation.

Implement logic that prioritizes safety by ensuring the conveyor stops if any station triggers a stop command or if an object is not detected by the sensors.

**2.Heating System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control the temperature of a heating system. The system should use input from three temperature sensors to automatically turn the heating on and off, maintaining a constant temperature range between 20°C and 22°C. The program must ensure smooth temperature regulation and prioritize energy efficiency by minimizing frequent switching. Safety measures should be implemented to handle sensor faults or temperature deviations beyond the specified range.

**3.Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**4.Pneumatic System Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a pneumatic system with a control loop frequency of 100 ms. The system should regulate the flow of air to actuators based on input signals, maintaining a flow rate of 50 standard liters per minute. The system must also ensure that the pressure remains within the specified range of 5.5 to 6 bar. Implement safety checks to handle any deviations in flow or pressure and ensure efficient and reliable operation under varying load conditions.

**5.Elevator Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program to control an elevator in a 5-floor building. Each floor has top and bottom limit switches to detect the elevator’s position. The elevator door should remain open for 7 seconds after reaching a floor. If no buttons inside the elevator cabin are pressed during this time, the door should reopen for an additional 10 seconds before closing. The elevator’s movement is governed by its current direction and the direction imposed by the up and down call buttons on each

**6.Automatic Car Wash Station Control Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards to control an automatic car wash station with a single wash bay. The system should use a sensor to detect the presence of a car. Once the car is detected and no human is present in the wash area, the system should initiate the car wash process. If a human is detected within the car wash area at any point, the station should immediately stop the wash process, trigger an alarm, and remain in a safe state until the area is clear.

**7.Entry/Exit Control for Underground Car Park Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 to control the entry and exit of an underground car park. The system uses the following sensors and actuators:

	•	Sensors:
	•	X1: Photoelectric switch at the ground floor entry/exit. It will be ON when a car passes.
	•	X2: Photoelectric switch at the basement entry/exit. It will be ON when a car passes.
	•	M1: ON for one scan cycle when a car from the ground floor passes X1.
	•	M2: ON for one scan cycle when a car from the basement passes X1.
	•	M3: ON for one scan cycle when a car from the basement passes X2.
	•	M4: ON for one scan cycle when a car from the ground floor passes X2.
	•	Intermediate Variables:
	•	M20: ON during the process of a car entering the passage from the ground floor.
	•	M30: ON during the process of a car entering the passage from the basement.
	•	Output Devices:
	•	Y1: Red lights at the entry/exit of the ground floor and the basement.
	•	Y2: Green lights at the entry/exit of the ground floor and the basement.

Process Description:

The entry and exit of the underground car park is controlled by a single lane passage, with traffic lights regulating car movement. The red lights (Y1) prohibit cars from entering or leaving, while the green lights (Y2) allow movement.

	•	When a car enters the passage from the ground floor entry, the red lights at both the ground floor and basement turn ON, while the green lights turn OFF, preventing any other cars from entering or leaving until the car passes through the passage.
	•	Similarly, when a car enters from the basement, the red lights will turn ON at both entry points, prohibiting other vehicles from entering or leaving until the car passes through.
	•	When the passage is clear, the green lights will turn ON again, allowing cars to enter or exit freely.
	•	Initially, the PLC should set the green lights ON and the red lights OFF to indicate free movement.

**8.Pick-and-Place Application for a Robot Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards for a pick-and-place robotic application with two conveyors, following the process described below:

Process Description:

The system operates in two modes: Manual Mode and Auto Mode. These modes are interlocked, meaning only one can be active at any time.

	1.	Manual Mode:
	•	When the Manual button is pressed, the robotic arm will execute the following steps in response to individual manual commands:
	•	Clip: Clip the product from conveyor A.
	•	Transfer: Move the product to conveyor B.
	•	Release: Release the product onto conveyor B, allowing it to be carried away.
	2.	Auto Mode:
	•	When the Auto button is pressed, the robotic arm will execute the entire pick-and-place process automatically:
	•	Clip: Clip the product from conveyor A and hold it.
	•	Transfer: Transfer the product to conveyor B (this action takes 2 seconds).
	•	Release: Release the product onto conveyor B.
	•	The auto process completes after one cycle, but can be re-triggered by pressing the Auto button again.

The system should ensure that manual and auto modes cannot operate simultaneously, using interlocking logic to prevent conflicts between the two modes.

**9.Empty Bottle Removal:**

Write a self-contained 61131-3 structured text program for packaging bottles. After filling, the bottles are moved with a conveyor to packaging. A proximity sensor detects any bottle, another one only empty bottles. A cylinder removes empty bottles.

**10.Coffee Maker:**

Write a self-contained 61131-3 structured text program for a coffee machine.

This machine contains three tanks, each for coffee, milk, and mixer, and three valves, one for the coffee, one for the milk, and the last valve for the output. This coffee machine contains a mixer, which is required to mix the coffee and milk properly to create the best output, The mixer is designed to work for four seconds after which it will automatically stop and the output valve will open to get the output.

The mixer is designed with a timer and will automatically start when the mixer tank reaches the maximum level, the tank is attached to the mixer as both the valves of coffee and milk are open and it started to fill the mixer and then the tank level comes into play with the preset maximum level, the mixer tank can be filled up to 130ml as it reaches the maximum level, the valves of coffee and milk will close and then it will start the mixing.

The coffee machine contains four Push buttons. Button one is for emergency stop, Button two is to start the machine, Button three is for Coffee and Milk and the last button is for Coffee only. The emergency stop is use as a safety button if anything goes wrong in the machine like if any of the valves not open, if the tank level does not work properly, if the mixer fails to work properly or any of the unexpected events occur, then there is a need of emergency stop to stop the machine instantly.
