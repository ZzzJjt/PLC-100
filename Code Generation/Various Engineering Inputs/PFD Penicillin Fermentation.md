Process Flow Diagram (PFD) in Textual Notation for Penicillin Fermentation

1. Process Overview

The penicillin production process involves several stages: fermentation, broth separation, product extraction, purification, and waste treatment. The main production stage is Fermentation, where a culture of Penicillium chrysogenum is grown under controlled conditions to produce penicillin. The process includes precise control of parameters such as temperature, pH, dissolved oxygen, and nutrient feed rate to maximize penicillin yield.

2. Equipment List

	•	F-101: Fermentation Vessel (20,000 liters)
	•	A-101: Air Compressor
	•	M-101: Agitator (Mechanical Stirrer)
	•	N-101: Nutrient Feed Tank
	•	N-102: Nutrient Feed Pump
	•	B-101: Broth Separator (Centrifuge)
	•	E-101: Extraction Unit (Solvent Extraction)
	•	C-101: Cooling Jacket (Fermentor Temperature Control)
	•	T-101: Product Tank
	•	T-102: Waste Tank

3. Instrumentation List

	•	FT-101: Fermentation Vessel Air Flow Transmitter (kg/hr)
	•	FCV-101: Air Flow Control Valve
	•	PT-101: Fermentation Vessel Pressure Transmitter (bar)
	•	TT-101: Fermentation Vessel Temperature Transmitter (°C)
	•	TC-101: Fermentation Temperature Controller (PID)
	•	LT-101: Fermentation Vessel Level Transmitter (%)
	•	LC-101: Fermentation Vessel Level Controller
	•	DO-101: Dissolved Oxygen Transmitter (ppm)
	•	PC-101: Dissolved Oxygen Controller (PID)
	•	FT-102: Nutrient Feed Flow Transmitter (L/hr)
	•	FCV-102: Nutrient Feed Flow Control Valve
	•	pH-101: Fermentation Vessel pH Transmitter
	•	pH-102: Fermentation Vessel pH Control Valve
	•	TT-102: Broth Separator Temperature Transmitter (°C)
	•	TT-103: Extraction Unit Temperature Transmitter (°C)
	•	FT-103: Product Flow Transmitter (kg/hr)
	•	PT-102: Product Tank Pressure Transmitter (bar)
	•	LT-102: Product Tank Level Transmitter (%)

4. Process Flow Description

	1.	Fermentation Stage
	•	Feed Preparation: The nutrient feed solution is prepared in the Nutrient Feed Tank (N-101). It is pumped using the Nutrient Feed Pump (N-102) through a Nutrient Feed Flow Transmitter (FT-102) to the Fermentation Vessel (F-101), where it is introduced at a controlled flow rate regulated by the Nutrient Feed Flow Control Valve (FCV-102).
	•	Fermentation Vessel Operation: In the fermentation vessel, a culture of Penicillium chrysogenum is inoculated into the nutrient-rich medium. The Agitator (M-101) ensures uniform mixing and optimal contact between the cells and nutrients. The Cooling Jacket (C-101) maintains the fermenter temperature at the desired setpoint.
	•	Air Supply: Sterilized air is introduced into the vessel through the Air Compressor (A-101), regulated by the Air Flow Control Valve (FCV-101) based on the setpoint from the Fermentation Vessel Air Flow Transmitter (FT-101).
	•	Dissolved Oxygen Control: The Dissolved Oxygen Transmitter (DO-101) measures the oxygen concentration. The Dissolved Oxygen Controller (PC-101) adjusts the agitator speed and air flow rate to maintain dissolved oxygen at 5 ppm ± 0.5 ppm.
	•	pH Control: The pH Transmitter (pH-101) continuously monitors the pH level in the vessel. The pH is adjusted by adding acid or base through the pH Control Valve (pH-102), controlled to maintain the pH at 6.5 ± 0.2.
	•	Temperature Control: The Temperature Transmitter (TT-101) monitors the fermenter temperature. The Temperature Controller (TC-101) adjusts the flow of cooling water through the Cooling Jacket (C-101) to maintain the temperature at 27°C ± 1°C.
	•	Pressure Control: The Pressure Transmitter (PT-101) monitors the internal pressure. The vent system opens if the pressure exceeds 1.2 bar, maintaining a safe operating range.
	2.	Broth Separation Stage
	•	After fermentation is complete, the broth is transferred to the Broth Separator (B-101), where the cells are separated from the fermentation broth using centrifugal force.
	•	The separated broth is monitored by the Broth Separator Temperature Transmitter (TT-102) to ensure it remains within 25°C ± 2°C.
	3.	Product Extraction Stage
	•	The clarified broth is sent to the Extraction Unit (E-101), where penicillin is extracted using a suitable solvent.
	•	The Extraction Unit Temperature Transmitter (TT-103) monitors the extraction process temperature and ensures it is maintained at 20°C ± 1°C.
	4.	Product Storage and Waste Management
	•	The extracted penicillin is stored in the Product Tank (T-101). The level is monitored by the Product Tank Level Transmitter (LT-102) and pressure is controlled by the Product Tank Pressure Transmitter (PT-102).
	•	The waste is directed to the Waste Tank (T-102) for further treatment.

5. Control Philosophy

The penicillin fermentation process involves maintaining precise control over key parameters to optimize production yield. The primary control loops are:

	1.	Nutrient Feed Flow Control Loop (FIC-102):
	•	FT-102 measures the flow rate.
	•	FCV-102 adjusts the flow based on the nutrient demand.
	2.	Dissolved Oxygen Control Loop (DOC-101):
	•	DO-101 measures dissolved oxygen.
	•	PC-101 controls the air flow rate and agitator speed.
	3.	pH Control Loop (pHIC-101):
	•	pH-101 measures the pH.
	•	pH-102 adjusts acid/base addition to maintain the desired setpoint.
	4.	Fermenter Temperature Control Loop (TIC-101):
	•	TT-101 measures temperature.
	•	TC-101 adjusts cooling water flow.
	5.	Fermenter Level Control Loop (LIC-101):
	•	LT-101 measures the vessel level.
	•	LC-101 adjusts the feed flow rate to maintain a stable liquid level.

6. Textual Notation

N-101 (Nutrient Feed Tank) -> N-102 (Nutrient Feed Pump) -> [FT-102] -> [FCV-102] -> F-101 (Fermentation Vessel)
F-101 -> [LT-101] -> [LC-101] -> [FT-102]
F-101 -> [DO-101] -> [PC-101] -> [FT-101] -> [FCV-101]
F-101 -> [TT-101] -> [TC-101] -> C-101 (Cooling Jacket)
F-101 -> [pH-101] -> [pH-102]
F-101 -> B-101 (Broth Separator)
B-101 -> [TT-102] -> E-101 (Extraction Unit)
E-101 -> [TT-103] -> T-101 (Product Tank)
E-101 -> T-102 (Waste Tank)

