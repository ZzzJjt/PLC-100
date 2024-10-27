A gas turbine in a power plant operates under complex and high-energy conditions, requiring comprehensive safety and control measures to prevent equipment damage and ensure safe operation. The following interlocks are critical for managing the various parameters that affect the turbine’s safe and efficient functioning. Each interlock monitors a specific parameter and triggers an appropriate response to prevent hazardous situations.

**List of Gas Turbine Interlocks and Their Actions**

	1.	Overtemperature Interlock:
	•	Cause: Exhaust gas temperature exceeds the predefined safe limit (e.g., > 650°C).
	•	Action: Initiate an immediate shutdown of the turbine.
	•	Purpose: Prevents thermal damage to turbine components such as blades and combustion chamber liners, reducing the risk of fire and mechanical deformation.
	2.	Overspeed Interlock:
	•	Cause: Turbine rotor speed exceeds 105% of nominal operating speed.
	•	Action: Trigger an emergency stop (E-Stop) and activate the overspeed protection system.
	•	Purpose: Protects the rotor, bearings, and mechanical components from damage due to excessive centrifugal forces.
	3.	Overpressure Interlock:
	•	Cause: Combustion chamber pressure exceeds safe levels (e.g., > 30 bar).
	•	Action: Open the combustion chamber pressure relief valve and initiate a controlled shutdown.
	•	Purpose: Prevents overpressure damage or catastrophic failure in the combustion chamber, protecting the turbine shell and connected piping systems.
	4.	Low Lubrication Pressure Interlock:
	•	Cause: Lubrication oil pressure falls below the minimum safe operating limit (e.g., < 1.5 bar).
	•	Action: Stop the turbine and trigger a lubrication system alarm.
	•	Purpose: Avoids bearing and rotor damage due to insufficient lubrication, ensuring that the turbine’s rotating components are adequately protected.
	5.	High Vibration Interlock:
	•	Cause: Excessive vibration detected in the turbine casing or rotor (e.g., vibration amplitude > 10 mm/s).
	•	Action: Shutdown the turbine and log a high vibration alarm.
	•	Purpose: Prevents mechanical damage due to imbalance, rotor misalignment, or bearing wear, protecting against catastrophic rotor failures.
	6.	Flame Failure Interlock:
	•	Cause: Flame in the combustion chamber is extinguished.
	•	Action: Immediately stop fuel flow and trigger a flame failure alarm.
	•	Purpose: Prevents unburned fuel accumulation in the combustion chamber, reducing the risk of explosion or fire upon re-ignition.
	7.	Fuel Gas Pressure Low Interlock:
	•	Cause: Fuel gas pressure falls below the required minimum operating limit (e.g., < 2 bar).
	•	Action: Close the fuel gas supply valve and stop the turbine.
	•	Purpose: Prevents incomplete combustion, which could lead to unstable operation, misfires, or damage to combustion hardware.
	8.	Cooling Water Flow Interlock:
	•	Cause: Cooling water flow rate falls below the safe flow rate (e.g., < 200 L/min).
	•	Action: Shutdown the turbine and activate the emergency cooling system.
	•	Purpose: Ensures that critical components (e.g., bearings and the generator) do not overheat, protecting them from thermal damage.
	9.	Compressor Surge Interlock:
	•	Cause: Compressor experiences a surge condition (e.g., sudden backflow or pressure drop).
	•	Action: Open the compressor bypass valve and reduce turbine load.
	•	Purpose: Prevents compressor blade damage, loss of performance, and mechanical failures due to unstable airflow conditions.
	10.	Emergency Stop (E-Stop) Interlock:
	•	Cause: Operator or automated system activates the E-Stop button due to a critical malfunction.
	•	Action: Immediately shuts down the turbine, isolates fuel supply, and vents residual gases.
	•	Purpose: Provides a manual override to bring the turbine to a safe state during an emergency, protecting personnel and equipment from severe damage.


**Integration of Interlocks into the Gas Turbine Control System**

	1.	Distributed Control System (DCS) Integration:
	•	All interlocks are integrated into the gas turbine’s Distributed Control System (DCS), which continuously monitors the critical parameters using inputs from sensors such as pressure transmitters (PT), temperature transmitters (TT), and vibration sensors.
	•	The DCS processes these inputs in real-time and automatically triggers interlock actions when safety limits are breached. This automation reduces the response time during emergencies, ensuring immediate protection.
	2.	Safety Instrumented System (SIS):
	•	The Safety Instrumented System (SIS) is a dedicated layer within the control system specifically designed to handle safety-critical interlocks. The SIS ensures that, in the event of a critical failure, the appropriate interlocks are triggered independently of the main control system.
	•	This redundancy enhances system reliability and ensures that safety actions are carried out even if the DCS fails.
	3.	Human-Machine Interface (HMI) and Alarm Management:
	•	Interlocks are displayed on the Human-Machine Interface (HMI), providing operators with real-time status updates and alarm notifications.
	•	If an interlock is activated, the HMI highlights the triggered condition, enabling operators to quickly identify the issue and take corrective action.
	4.	Sequential Shutdown Logic:
	•	The interlock system is configured to initiate a sequential shutdown rather than an abrupt stop, depending on the severity of the condition.
	•	For example, during a high vibration event, the system first reduces load and then initiates a controlled shutdown to minimize mechanical stress.
	5.	Manual Reset Requirements:
	•	Many interlocks, such as the overspeed or overtemperature interlocks, require a manual reset before the turbine can be restarted. This feature ensures that the issue is addressed and safe conditions are verified before resuming operation.
