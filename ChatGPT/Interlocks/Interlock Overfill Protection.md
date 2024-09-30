Below is an implementation of an IEC 61131-3 structured text program to provide overfill protection for a vessel using an interlock system. The program uses a level sensor (Level_Sensor) to monitor the liquid level in the vessel and controls an inlet valve (Inlet_Valve) to prevent overfilling. The logic includes fail-safe mechanisms to ensure that the system defaults to a safe state in case of sensor failure or valve malfunction.

```
(* IEC 61131-3 Structured Text Program: Overfill Protection Interlock *)

(* Declare variables *)
VAR
    Level_Sensor : REAL;            (* Current level from the level sensor (0 to 100%) *)
    High_Level_Setpoint : REAL := 85.0;  (* High-level setpoint in % *)
    Low_Level_Reset : REAL := 75.0;      (* Low-level reset point in % *)
    Inlet_Valve : BOOL := FALSE;         (* Inlet valve control (TRUE = Open, FALSE = Closed) *)
    Sensor_Fault : BOOL := FALSE;        (* Sensor fault indicator *)
    Valve_Fault : BOOL := FALSE;         (* Valve fault indicator *)
    Interlock_Active : BOOL := FALSE;    (* Interlock status (TRUE = Interlock Engaged) *)
END_VAR

(* Monitor level sensor and engage interlock if high level is reached *)
IF Level_Sensor >= High_Level_Setpoint THEN
    Interlock_Active := TRUE;     (* Activate interlock *)
    Inlet_Valve := FALSE;         (* Close inlet valve to prevent overfill *)
END_IF

(* Reset interlock if level drops below the low-level reset point *)
IF (Level_Sensor < Low_Level_Reset) AND (NOT Sensor_Fault) AND (NOT Valve_Fault) THEN
    Interlock_Active := FALSE;    (* Deactivate interlock *)
END_IF

(* Fail-safe mechanisms for sensor or valve malfunction *)
IF Sensor_Fault OR Valve_Fault THEN
    Inlet_Valve := FALSE;         (* Close inlet valve to default safe state *)
    Interlock_Active := TRUE;     (* Keep interlock active until manual reset *)
END_IF

(* Safety notes *)
(* If the level sensor or valve indicates a fault, the system defaults to a safe state by closing the inlet valve *)
```
**Program Logic Explanation**

	1.	Level Monitoring and Interlock Activation:
	•	The program continuously monitors the liquid level in the vessel using the Level_Sensor variable.
	•	If the level reaches or exceeds the High_Level_Setpoint (set to 85% of the vessel capacity), the interlock (Interlock_Active) is engaged.
	•	The inlet valve (Inlet_Valve) is closed immediately to prevent further liquid from entering the vessel.
	2.	Interlock Reset Condition:
	•	The interlock remains engaged until the liquid level drops below the Low_Level_Reset setpoint (set to 75%).
	•	The reset condition also checks that no sensor (Sensor_Fault) or valve (Valve_Fault) faults are present.
	3.	Fail-Safe Mechanisms:
	•	If a sensor or valve fault is detected, the interlock is engaged, and the inlet valve is forced to close to ensure the system defaults to a safe state.
	•	Fault detection is critical to prevent potential hazards in the event of equipment failure.
