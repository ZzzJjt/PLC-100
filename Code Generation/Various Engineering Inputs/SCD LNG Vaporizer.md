NORSOK System Control Diagram (SCD) for LNG Vaporizer System

1. System Overview

The LNG Vaporizer System is used to convert liquefied natural gas (LNG) from its cryogenic state to gaseous natural gas (NG) for use in power generation, distribution, or other applications. The system typically includes a feed pump, LNG vaporizer, heat exchanger, temperature control system, pressure regulation system, and safety interlocks. This SCD describes the control loops, instrumentation, interlocks, and piping necessary to ensure safe and efficient operation of the LNG vaporizer system.

2. Equipment List

	•	LNG-P-101: LNG Feed Pump
	•	LNG-V-101: LNG Vaporizer
	•	HE-101: Heat Exchanger
	•	NG-R-101: Natural Gas (NG) Receiving Vessel
	•	VLV-101: LNG Inlet Control Valve
	•	VLV-102: NG Outlet Control Valve

3. Instrumentation List

	•	PT-101: LNG Feed Pump Inlet Pressure Transmitter (bar)
	•	FT-101: LNG Feed Flow Transmitter (kg/hr)
	•	FCV-101: LNG Flow Control Valve (% Open)
	•	LT-101: Vaporizer Level Transmitter (%)
	•	LC-101: Vaporizer Level Controller (PID)
	•	LAL-101: Low-Level Alarm (Vaporizer) (%)
	•	LAV-101: High-Level Alarm (Vaporizer) (%)
	•	TT-101: LNG Vaporizer Outlet Temperature Transmitter (°C)
	•	TC-101: Temperature Controller (PID)
	•	PT-102: Vaporizer Outlet Pressure Transmitter (bar)
	•	PCV-101: Vaporizer Outlet Pressure Control Valve (% Open)
	•	TT-102: NG Outlet Temperature Transmitter (°C)
	•	FT-102: NG Outlet Flow Transmitter (kg/hr)
	•	PAH-102: High Pressure Alarm (Vaporizer) (bar)
	•	PAL-102: Low Pressure Alarm (Vaporizer) (bar)
	•	XV-101: Emergency Shutoff Valve (ESD) (Open/Close)
	•	SDV-101: Safety Shutoff Valve for LNG Inlet (Open/Close)
	•	SDV-102: Safety Shutoff Valve for NG Outlet (Open/Close)

4. Control Loops and Interlocks

	1.	LNG Feed Flow Control Loop (FIC-101):
	•	FT-101 measures the LNG flow rate entering the vaporizer.
	•	FCV-101 adjusts the LNG feed rate based on the setpoint.
	•	Setpoint: 10,000 kg/hr ± 500 kg/hr.
	•	Control Action: Adjusts FCV-101 to maintain steady LNG flow.
	2.	Vaporizer Level Control Loop (LIC-101):
	•	LT-101 measures the liquid level in the vaporizer.
	•	LC-101 regulates the liquid level by adjusting FCV-101.
	•	Setpoint: 50% ± 5%.
	•	LAV-101 triggers a high-level alarm at 90%.
	•	LAL-101 triggers a low-level alarm at 20%.
	•	Control Action: Adjusts FCV-101 to maintain set level.
	3.	Vaporizer Temperature Control Loop (TIC-101):
	•	TT-101 measures the outlet temperature of the vaporizer.
	•	TC-101 adjusts the steam or hot water flow rate to the HE-101 (Heat Exchanger) to maintain the gas temperature.
	•	Setpoint: 10°C ± 2°C (Superheated NG).
	•	Control Action: Regulates heat exchanger flow rate to ensure proper vaporization.
	4.	Vaporizer Outlet Pressure Control Loop (PIC-101):
	•	PT-102 measures the vaporizer outlet pressure.
	•	PCV-101 regulates the pressure to maintain the required gas supply pressure.
	•	Setpoint: 30 bar ± 2 bar.
	•	PAH-102 triggers a high-pressure alarm at 35 bar.
	•	PAL-102 triggers a low-pressure alarm at 25 bar.
	•	Control Action: Adjusts PCV-101 to regulate downstream pressure.
	5.	NG Outlet Flow Control Loop (FIC-102):
	•	FT-102 measures the NG flow rate at the outlet of the vaporizer system.
	•	VLV-102 regulates the outlet flow to the NG Receiving Vessel.
	•	Setpoint: 9,500 kg/hr ± 300 kg/hr.
	•	Control Action: Adjusts VLV-102 to match the demand downstream.

5. Safety Interlocks

	1.	Low Level Interlock (LLI-101):
	•	LAL-101 triggers when the vaporizer level falls below 20%.
	•	Action: Closes SDV-101 (LNG Inlet Valve) and SDV-102 (NG Outlet Valve) to prevent damage.
	2.	High Level Interlock (HLI-101):
	•	LAV-101 triggers when the vaporizer level exceeds 90%.
	•	Action: Closes XV-101 (ESD Valve) and opens SDV-101 (LNG Inlet Valve) to avoid overflow.
	3.	High Pressure Interlock (HPI-102):
	•	PAH-102 triggers when the vaporizer outlet pressure exceeds 35 bar.
	•	Action: Closes PCV-101 and opens SDV-102 to release pressure.
	4.	Low Pressure Interlock (LPI-102):
	•	PAL-102 triggers when the vaporizer outlet pressure falls below 25 bar.
	•	Action: Closes SDV-102 to maintain minimum pressure for downstream operations.
	5.	Emergency Shutoff (ESD-101):
	•	Manual or automatic initiation during any abnormal condition.
	•	Action: Closes XV-101, SDV-101, and SDV-102 to isolate the LNG and NG lines.

6. Textual Notation
LNG Feed Pump (LNG-P-101) -> [PT-101] -> [FT-101] -> [FCV-101] -> LNG Vaporizer (LNG-V-101)
LNG Vaporizer -> [LT-101] -> [LC-101] -> FCV-101
LNG Vaporizer -> [TT-101] -> [TC-101] -> Heat Exchanger (HE-101)
LNG Vaporizer -> [PT-102] -> [PCV-101] -> NG Receiving Vessel (NG-R-101)
NG Receiving Vessel -> [TT-102] -> [FT-102] -> [VLV-102] -> Downstream
NG Receiving Vessel -> [PAH-102], [PAL-102]
Safety Shutoff Valves -> [SDV-101] (LNG Inlet), [SDV-102] (NG Outlet)
Emergency Shutoff Valve -> [XV-101]
