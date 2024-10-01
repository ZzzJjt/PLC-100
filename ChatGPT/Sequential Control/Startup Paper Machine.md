System Overview:

The press section of a Valmet paper machine consists of various components such as press rolls, nip presses, and conveyors. During the startup process, it is crucial to ensure smooth transitions between different phases, maintaining proper synchronization, and gradually ramping up to full operating speed. Key control variables include:

	•	Press Roll Speed: The speed at which the press rolls rotate.
	•	Nip Pressure: The pressure applied between the press rolls to remove moisture from the paper sheet.
	•	Temperature Settings: Roll surface temperature to ensure proper moisture removal and sheet quality.

Key Parameters for the Press Section:

	1.	Initial Roll Speed: 5 m/min
	2.	Operational Roll Speed: 200 m/min
	3.	Nip Pressure Setpoint: 100 kN/m (initial), gradually increased to 300 kN/m
	4.	Temperature Setpoint: 85°C

Startup Sequence:

	1.	Stage 1: System Initialization
	•	Check safety interlocks and ensure all components are in the safe state.
	•	Ensure nip pressure is set to 0 kN/m.
	•	Set initial roll speed to 5 m/min.
	2.	Stage 2: Pre-Heating the Press Rolls
	•	Activate the heating elements and increase the surface temperature to 85°C.
	•	Ensure the temperature is stable before moving to the next stage.
	3.	Stage 3: Gradual Roll Speed Ramp-Up
	•	Start with the initial roll speed of 5 m/min.
	•	Gradually increase speed in increments of 10 m/min every 30 seconds until the operational speed of 200 m/min is reached.
	•	Synchronize the speed of the press rolls and conveyors to maintain uniform sheet tension.
	4.	Stage 4: Apply Initial Nip Pressure
	•	Increase the nip pressure to 100 kN/m.
	•	Monitor the paper sheet for any signs of damage or instability.
	5.	Stage 5: Gradual Increase to Operational Nip Pressure
	•	Gradually increase nip pressure from 100 kN/m to 300 kN/m in increments of 20 kN/m every 30 seconds.
	•	Ensure uniform pressure distribution across the rolls.
	6.	Stage 6: Steady-State Operation
	•	Monitor all variables and ensure the system is running at operational setpoints.
	•	Perform safety checks and log any deviations.

IEC 61131-3 Structured Text Program for Press Section Startup

The following structured text program implements the startup sequence for the press section of the Valmet paper machine, ensuring smooth transitions, safety checks, and proper synchronization.

```
PROGRAM PressSection_Startup
VAR
    StepIndex : INT := 0;                     // Tracks the current step in the startup sequence.
    TimerStep : TON;                          // General timer for step durations.
    RollSpeed : REAL := 5.0;                  // Current roll speed (m/min).
    NipPressure : REAL := 0.0;                // Current nip pressure (kN/m).
    Temperature : REAL := 25.0;               // Current roll surface temperature (°C).
    SpeedSetpoint : REAL := 200.0;            // Target operational roll speed (m/min).
    PressureSetpoint : REAL := 300.0;         // Target operational nip pressure (kN/m).
    TempSetpoint : REAL := 85.0;              // Target roll surface temperature (°C).
    SafetyInterlock : BOOL := TRUE;           // Safety interlock status.
    HeaterOn : BOOL := FALSE;                 // Heater status for the press rolls.
    NipPressureValve : BOOL := FALSE;         // Nip pressure control valve status.
    ConveyorSpeed : REAL;                     // Conveyor speed (synchronized with rolls).
END_VAR

// Main Control Logic for Startup Sequence
CASE StepIndex OF
    // Step 0: System Initialization and Safety Checks
    0:
        IF SafetyInterlock THEN
            RollSpeed := 5.0;                  // Set initial roll speed.
            NipPressure := 0.0;                // Set initial nip pressure.
            Temperature := 25.0;               // Initial temperature.
            HeaterOn := FALSE;                 // Ensure heaters are off.
            NipPressureValve := FALSE;         // Ensure pressure valves are closed.
            StepIndex := StepIndex + 1;        // Move to pre-heating step.
        ELSE
            StepIndex := 0;                    // Wait until interlocks are cleared.
        END_IF

    // Step 1: Pre-Heating the Press Rolls
    1:
        HeaterOn := TRUE;                      // Activate heating elements.
        IF Temperature < TempSetpoint THEN
            Temperature := Temperature + 0.5;  // Incrementally increase temperature.
        ELSE
            HeaterOn := FALSE;                 // Turn off heaters once setpoint is reached.
            StepIndex := StepIndex + 1;        // Move to roll speed ramp-up.
        END_IF

    // Step 2: Gradual Roll Speed Ramp-Up
    2:
        IF RollSpeed < SpeedSetpoint THEN
            RollSpeed := RollSpeed + 10.0;     // Increase roll speed by 10 m/min every 30 seconds.
            TimerStep(IN := TRUE, PT := T#30S); // Wait 30 seconds before next increment.
            IF TimerStep.Q THEN
                TimerStep(IN := FALSE);        // Reset timer for next increment.
            END_IF
        ELSE
            RollSpeed := SpeedSetpoint;        // Set to operational speed.
            ConveyorSpeed := RollSpeed;        // Synchronize conveyor speed.
            StepIndex := StepIndex + 1;        // Move to initial nip pressure step.
        END_IF

    // Step 3: Apply Initial Nip Pressure
    3:
        NipPressureValve := TRUE;              // Open nip pressure control valve.
        IF NipPressure < 100.0 THEN
            NipPressure := NipPressure + 10.0; // Increase nip pressure gradually.
            TimerStep(IN := TRUE, PT := T#10S); // Wait 10 seconds before next increment.
            IF TimerStep.Q THEN
                TimerStep(IN := FALSE);        // Reset timer.
            END_IF
        ELSE
            StepIndex := StepIndex + 1;        // Move to operational nip pressure step.
        END_IF

    // Step 4: Gradual Increase to Operational Nip Pressure
    4:
        IF NipPressure < PressureSetpoint THEN
            NipPressure := NipPressure + 20.0; // Increase nip pressure by 20 kN/m every 30 seconds.
            TimerStep(IN := TRUE, PT := T#30S); // Wait 30 seconds.
            IF TimerStep.Q THEN
                TimerStep(IN := FALSE);        // Reset timer.
            END_IF
        ELSE
            StepIndex := StepIndex + 1;        // Move to steady-state operation.
        END_IF

    // Step 5: Steady-State Operation
    5:
        // Monitor all variables and log deviations.
        IF NipPressure = PressureSetpoint AND RollSpeed = SpeedSetpoint THEN
            // System is running at operational setpoints.
            StepIndex := 5;                    // Stay in steady-state.
        ELSE
            StepIndex := 0;                    // Error or deviation, restart sequence.
        END_IF

ELSE
    StepIndex := 0;                            // Error or end of sequence.
END_CASE

END_PROGRAM
```

The following function controls the nip pressure, ensuring it increases gradually and stays within safe limits.
```
FUNCTION MaintainNipPressure
VAR_INPUT
    CurrentPressure : REAL;        // Current nip pressure (kN/m).
    PressureSetpoint : REAL;       // Desired nip pressure (kN/m).
END_VAR
VAR
    PressureValve : BOOL;          // Pressure valve control.
END_VAR

BEGIN
    // Increase nip pressure gradually if below setpoint
    IF CurrentPressure < PressureSetpoint THEN
        PressureValve := TRUE;     // Open valve to increase pressure.
    ELSE
        PressureValve := FALSE;    // Close valve once setpoint is reached.
    END_IF

END_FUNCTION
```

Importance of Maintaining Optimal Nip Pressure and Temperature

	1.	Nip Pressure:
	•	Proper nip pressure is essential for removing moisture from the paper sheet. Too low a pressure results in poor moisture removal, while too high a pressure can damage the sheet and the rolls.
	2.	Temperature Control:
	•	Maintaining the correct temperature ensures efficient moisture removal and prevents thermal damage to the sheet. Any deviation in temperature can lead to quality defects in the paper.
