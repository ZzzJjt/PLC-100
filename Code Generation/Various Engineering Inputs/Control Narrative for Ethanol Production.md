1. Process Overview

The ethanol production process involves multiple stages, starting from feedstock preparation, milling, saccharification, fermentation, and finally, distillation. The primary focus of this control narrative is on the Fermentation stage, where sugars are converted into ethanol and carbon dioxide by the action of yeast. This process requires precise control of parameters such as temperature, pH, and nutrient levels to ensure maximum ethanol yield, minimize byproduct formation, and maintain optimal fermentation efficiency.

2. Fermentation Tank Description

	•	Tank Type: Continuous Stirred Tank Reactor (CSTR)
	•	Volume: 100,000 liters
	•	Material: Stainless Steel (316L)
	•	Design Pressure: 2 bar (Maximum Allowable Working Pressure)
	•	Design Temperature: 50°C (Maximum Allowable Temperature)
	•	Operating Pressure: 0.5 to 1.0 bar
	•	Operating Temperature: 30°C to 35°C

3. Fermentation Control Strategy

	1.	Sugar Concentration Control
	•	Objective: Maintain a consistent concentration of fermentable sugars (glucose and maltose) in the fermenter to ensure steady ethanol production.
	•	Setpoint: 15% w/w ± 0.5%
	•	Control Mode: Cascade control using a flow transmitter (FT) on the feed line and a concentration analyzer (CA) in the fermenter.
	•	Controller Actions:
	•	Adjust the feed rate of the glucose solution to maintain the target concentration.
	•	Reduce feed rate if sugar concentration exceeds 15.5%.
	•	Increase feed rate if sugar concentration drops below 14.5%.
	2.	Temperature Control
	•	Objective: Maintain the fermenter temperature within an optimal range to promote yeast activity and maximize ethanol yield.
	•	Setpoint: 32°C ± 1°C
	•	Control Mode: PID control using a temperature transmitter (TT) and a temperature control valve (TCV) connected to the cooling jacket.
	•	Controller Actions:
	•	Open the cooling water valve if the temperature exceeds 33°C.
	•	Close the cooling water valve if the temperature drops below 31°C.
	•	Alarms:
	•	High-Temperature Alarm at 34°C.
	•	Low-Temperature Alarm at 30°C.
	3.	pH Control
	•	Objective: Maintain the pH within the optimal range for yeast activity and fermentation efficiency.
	•	Setpoint: pH 4.8 ± 0.2
	•	Control Mode: PID control using a pH transmitter (pHT) and an alkali dosing pump.
	•	Controller Actions:
	•	Increase alkali dosing if pH drops below 4.6.
	•	Reduce alkali dosing if pH rises above 5.0.
	•	Alarms:
	•	Low pH Alarm at 4.5.
	•	High pH Alarm at 5.2.
	4.	Dissolved Oxygen (DO) Control
	•	Objective: Maintain optimal DO levels at the initial stage to promote yeast growth, and then reduce to prevent unwanted byproduct formation.
	•	Setpoint:
	•	Initial Phase: 5 ppm ± 0.2 ppm
	•	Production Phase: < 0.2 ppm
	•	Control Mode: PID control using a dissolved oxygen transmitter (DOT) and an air or nitrogen control valve.
	•	Controller Actions:
	•	Open the air control valve to maintain 5 ppm during yeast growth.
	•	Close the air valve or introduce nitrogen to maintain DO below 0.2 ppm during ethanol production.
	5.	Agitator Speed Control
	•	Objective: Ensure uniform mixing for even distribution of temperature and nutrients throughout the fermenter.
	•	Setpoint: 150 rpm ± 5 rpm
	•	Control Mode: Speed control using a variable frequency drive (VFD).
	•	Controller Actions:
	•	Increase speed if solids or sediment accumulation is detected.
	•	Decrease speed to prevent shear stress on yeast cells.
	6.	Ethanol Concentration Monitoring
	•	Objective: Continuously monitor ethanol concentration to ensure the fermentation process is proceeding as expected.
	•	Setpoint: 10% v/v ± 1%
	•	Control Mode: Monitoring using an online ethanol concentration analyzer.
	•	Controller Actions:
	•	Adjust feed rate, temperature, or pH as necessary to maintain ethanol concentration.
	•	Alarms:
	•	Low Concentration Alarm: < 9% v/v
	•	High Concentration Alarm: > 12% v/v

4. Detailed Control Steps During Fermentation

	1.	Sugar Concentration Control
At the start of fermentation, it is critical to establish and maintain the correct sugar concentration in the fermenter. The feed of glucose solution from the saccharification stage is controlled to ensure a concentration of 15% w/w in the fermenter. This is achieved using a flow transmitter (FT) on the feed line and a concentration analyzer (CA) that continuously measures the sugar concentration. A cascade control strategy is employed, where the feed flow rate is adjusted based on the measured concentration. If the concentration exceeds 15.5%, the feed rate is reduced to avoid overfeeding and potential byproduct formation. Conversely, if the concentration falls below 14.5%, the feed rate is increased to maintain steady fermentation conditions.
	2.	Temperature Control
Maintaining the temperature within the optimal range of 32°C is crucial for yeast metabolism and ethanol production. Temperature control is managed using a PID loop, which monitors the fermenter temperature via a temperature transmitter (TT). The temperature control valve (TCV) regulates the flow of cooling water through the fermenter’s cooling jacket to dissipate heat generated during fermentation. If the temperature exceeds 33°C, the cooling water valve opens to increase the cooling rate. If the temperature drops below 31°C, the valve closes to reduce cooling and prevent excessive chilling, which can inhibit yeast activity and slow down ethanol production.
	3.	pH Control
During fermentation, the pH must be maintained at 4.8 to ensure yeast viability and process efficiency. A pH transmitter (pHT) monitors the pH of the fermenting broth, and a PID control loop adjusts the alkali dosing pump to regulate the pH. As fermentation progresses, organic acids are produced, causing a natural decrease in pH. If the pH drops below 4.6, the alkali dosing pump is activated to add a base solution, restoring the pH to the setpoint. If the pH rises above 5.0, the dosing rate is reduced. Maintaining the correct pH prevents yeast stress and ensures a high ethanol yield.
	4.	Dissolved Oxygen (DO) Management
Dissolved oxygen levels play a critical role in different stages of fermentation. During the initial phase, a DO setpoint of 5 ppm is maintained to promote yeast growth and cell replication. This is achieved using a dissolved oxygen transmitter (DOT) that controls the opening of an air valve. As the yeast population reaches the desired level, the DO setpoint is lowered to less than 0.2 ppm to minimize the formation of unwanted byproducts such as acetic acid. This is done by closing the air valve and, if necessary, introducing nitrogen gas to displace residual oxygen. The low-oxygen environment shifts the yeast metabolism towards ethanol production.
	5.	Agitator Speed Control
Proper mixing is essential for maintaining uniformity of temperature, nutrients, and pH throughout the fermenter. The agitator speed is initially set at 150 rpm and is controlled using a variable frequency drive (VFD). The speed may be increased if sediment accumulation or poor mixing is detected. Conversely, the speed is reduced if high shear stress is observed, which can damage the yeast cells. This dynamic adjustment ensures that the yeast cells are evenly distributed, promoting efficient fermentation and avoiding dead zones within the fermenter.
	6.	Ethanol Concentration Monitoring
Continuous monitoring of ethanol concentration is used to track the progress of fermentation and detect any deviations from the expected production rate. An online ethanol concentration analyzer provides real-time feedback on the ethanol concentration. If the concentration drops below 9% v/v, it may indicate an issue with yeast activity, prompting a review of temperature, pH, and feed conditions. If the concentration rises above 12%, it suggests that the fermentation is nearing completion, and the batch is ready for downstream processing. Adjustments to feed rate, temperature, and pH are made as needed to maintain optimal production levels.
