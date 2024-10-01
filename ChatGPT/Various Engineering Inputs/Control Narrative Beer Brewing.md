Control Narrative for Beer Brewing

1. Process Overview

The beer brewing process involves several stages, including mashing, lautering, boiling, fermentation, conditioning, and packaging. Each stage requires precise control over parameters such as temperature, pressure, and flow to ensure consistent quality and flavor of the final product. This narrative provides a detailed control strategy for each stage, with a focus on the Lautering process, which is crucial for extracting fermentable sugars from the grain bed.

2. Mashing Stage Control

	•	Objective: Convert starches in the malted grain into fermentable sugars by controlling the temperature and mixing in the mash tun.
	•	Setpoints:
	•	Initial Mash Temperature: 65°C ± 1°C
	•	Final Mash Temperature (Mashing-Out): 78°C ± 1°C
	•	Control Mode: PID control using a temperature transmitter (TT) and a steam control valve (TCV) to maintain the temperature.
	•	Alarms:
	•	High-Temperature Alarm: > 80°C
	•	Low-Temperature Alarm: < 60°C

3. Boiling Stage Control

	•	Objective: Sterilize the wort, extract hop flavors, and evaporate unwanted volatiles.
	•	Setpoints:
	•	Boiling Temperature: 100°C ± 2°C
	•	Boiling Duration: 60 minutes ± 5 minutes
	•	Control Mode: On-off control using a heating element or steam valve.
	•	Alarms:
	•	High-Temperature Alarm: > 105°C
	•	Low-Temperature Alarm: < 95°C

4. Lautering Stage Control

The Lautering stage involves separating the liquid wort from the solid grain husks after mashing. This step is critical for extracting as much fermentable sugar as possible while maintaining clarity in the wort. The process requires precise control of flow rates, bed depth, and sparge water temperature.

4.1. Equipment and Instrumentation Needed

	1.	Lauter Tun: A vessel equipped with a false bottom or slotted plates to support the grain bed and allow wort to filter through.
	2.	Mash Rake and Ploughs: Agitation devices to optimize wort flow and prevent channeling.
	3.	Flow Transmitters (FT): For monitoring wort flow rates.
	4.	Temperature Transmitters (TT): For measuring wort and sparge water temperature.
	5.	Pressure Transmitters (PT): For monitoring bed pressure to detect compaction or channeling.
	6.	Level Transmitter (LT): For maintaining the proper liquid level above the grain bed.
	7.	Control Valves (CV): For regulating wort outflow and sparge water inflow.
	8.	Sparge Water Heater: For maintaining the sparge water temperature at the required setpoint.
	9.	Recirculation Pump: For recycling wort through the grain bed during the initial stages to increase clarity.
	10.	Sight Glass: For visual monitoring of wort clarity.

4.2. Control Parameters

	•	Grain Bed Height: 60 cm ± 5 cm
	•	Initial Wort Recirculation Flow Rate: 5 L/min ± 0.5 L/min
	•	Sparge Water Temperature: 78°C ± 2°C
	•	Wort Outflow Rate: 25 L/min ± 2 L/min
	•	Final Wort Gravity: 1.010 ± 0.005

4.3. Control Strategy

The lautering process is divided into three phases: Recirculation, Wort Collection, and Sparging. During recirculation, the goal is to establish a clear wort by passing it through the grain bed multiple times. In the wort collection phase, the primary objective is to collect the high-sugar wort until a specific gravity is reached. Sparging involves rinsing the grain bed with hot water to extract remaining sugars without disturbing the bed.

4.4. Steps for Lautering Execution

	1.	Initial Recirculation:
	•	Start the recirculation pump to cycle wort from the lauter tun bottom to the top.
	•	Setpoint: Recirculation flow rate at 5 L/min ± 0.5 L/min.
	•	Monitor wort clarity using a sight glass and recirculate until clear wort is visible.
	•	If wort clarity is not achieved within 10 minutes, reduce flow rate and check for bed compaction.
	2.	Establish Grain Bed:
	•	Adjust the mash rake and ploughs to evenly distribute the grain bed and prevent channeling.
	•	Monitor the bed depth using a level transmitter (LT).
	•	Setpoint: Bed height at 60 cm ± 5 cm.
	•	If bed height is too low, add sparge water slowly while maintaining even distribution.
	3.	Wort Collection:
	•	Gradually open the wort outlet valve and increase the outflow rate.
	•	Setpoint: Outflow rate at 25 L/min ± 2 L/min.
	•	Monitor the pressure drop across the bed using pressure transmitters (PT) to avoid channeling or compacting.
	•	Collect wort until gravity reaches 1.010 ± 0.005.
	•	If gravity drops below 1.010, stop wort collection and move to sparging.
	4.	Sparging:
	•	Begin sparge water addition at a controlled flow rate.
	•	Sparge Water Temperature Setpoint: 78°C ± 2°C.
	•	Maintain a liquid level of 2 cm above the grain bed using the level transmitter (LT).
	•	Monitor wort gravity at the outlet. If gravity reaches 1.005, stop sparging.
	•	Ensure uniform bed washing by adjusting the rake speed and sparge water distribution.
	5.	Final Wort Collection:
	•	Once the desired gravity is achieved, close the sparge water inlet and continue collecting wort until the liquid level drops to 5 cm above the grain bed.
	•	Stop the collection when gravity drops to 1.005 ± 0.002 or when all desired wort is collected.
	•	Close all valves and prepare the lauter tun for cleaning.
	6.	Shutdown and Cleaning:
	•	Engage CIP (Clean-in-Place) system for the lauter tun.
	•	Remove spent grains using the mash ploughs.
	•	Flush the system with hot water and inspect for any blockages or residual grain.

The Lautering process is critical to achieving high-quality wort and minimizing sugar loss. By following these detailed steps and maintaining tight control over key parameters, the lautering process can be optimized for maximum efficiency and product consistency.
