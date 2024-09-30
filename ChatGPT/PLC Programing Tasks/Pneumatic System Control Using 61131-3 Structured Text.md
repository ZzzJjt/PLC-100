Here is a self-contained 61131-3 Structured Text program to control a pneumatic system. This program runs at a control loop frequency of 100 milliseconds and regulates the flow of air to maintain a desired flow rate of 50 standard liters per minute (SLPM) while ensuring that the pressure remains between 5.5 and 6 bar. Safety checks are included to handle deviations in flow or pressure, ensuring efficient and reliable operation.

```
PROGRAM PneumaticSystemControl
    // Variables for system inputs, outputs, and control logic
    VAR
        // Input signals
        FlowRate_Input: REAL := 0.0;         // Current flow rate in standard liters per minute (SLPM)
        Pressure_Input: REAL := 0.0;         // Current system pressure in bar
        LoadCondition: BOOL := FALSE;        // Input to indicate varying load conditions (e.g., TRUE for high load)

        // Control setpoints
        DesiredFlowRate: REAL := 50.0;       // Target flow rate (SLPM)
        PressureLowerLimit: REAL := 5.5;     // Minimum acceptable pressure (bar)
        PressureUpperLimit: REAL := 6.0;     // Maximum acceptable pressure (bar)

        // System outputs
        FlowControlValve: REAL := 0.0;       // Output control value for flow regulation (0.0 - 100.0%)
        PressureControlValve: REAL := 0.0;   // Output control value for pressure regulation (0.0 - 100.0%)

        // Control parameters
        FlowPID_P: REAL := 1.0;              // Proportional gain for flow control
        FlowPID_I: REAL := 0.1;              // Integral gain for flow control
        FlowPID_D: REAL := 0.01;             // Derivative gain for flow control
        PressurePID_P: REAL := 1.0;          // Proportional gain for pressure control
        PressurePID_I: REAL := 0.1;          // Integral gain for pressure control
        PressurePID_D: REAL := 0.01;         // Derivative gain for pressure control

        // PID loop variables for flow control
        FlowError: REAL := 0.0;              // Error in flow rate
        FlowIntegral: REAL := 0.0;           // Integral component of flow control
        FlowDerivative: REAL := 0.0;         // Derivative component of flow control
        FlowPrevError: REAL := 0.0;          // Previous flow error for derivative calculation
        FlowPID_Output: REAL := 0.0;         // PID output for flow control

        // PID loop variables for pressure control
        PressureError: REAL := 0.0;          // Error in pressure
        PressureIntegral: REAL := 0.0;       // Integral component of pressure control
        PressureDerivative: REAL := 0.0;     // Derivative component of pressure control
        PressurePrevError: REAL := 0.0;      // Previous pressure error for derivative calculation
        PressurePID_Output: REAL := 0.0;     // PID output for pressure control

        // Safety and fault indicators
        FlowFault: BOOL := FALSE;            // Indicates a fault in flow regulation
        PressureFault: BOOL := FALSE;        // Indicates a fault in pressure regulation
        SafetyShutdown: BOOL := FALSE;       // Indicates a system safety shutdown condition
    END_VAR

    // Calculate flow rate error
    FlowError := DesiredFlowRate - FlowRate_Input;

    // Flow control PID calculation
    FlowIntegral := FlowIntegral + FlowError * 0.1; // Integral calculation
    FlowDerivative := (FlowError - FlowPrevError) / 0.1; // Derivative calculation based on 100ms loop time
    FlowPID_Output := (FlowPID_P * FlowError) + (FlowPID_I * FlowIntegral) + (FlowPID_D * FlowDerivative);

    // Update previous flow error
    FlowPrevError := FlowError;

    // Calculate pressure error
    PressureError := 0.0; // Default to zero
    IF Pressure_Input < PressureLowerLimit THEN
        PressureError := PressureLowerLimit - Pressure_Input; // Pressure too low
    ELSIF Pressure_Input > PressureUpperLimit THEN
        PressureError := PressureUpperLimit - Pressure_Input; // Pressure too high
    END_IF

    // Pressure control PID calculation
    PressureIntegral := PressureIntegral + PressureError * 0.1; // Integral calculation
    PressureDerivative := (PressureError - PressurePrevError) / 0.1; // Derivative calculation based on 100ms loop time
    PressurePID_Output := (PressurePID_P * PressureError) + (PressurePID_I * PressureIntegral) + (PressurePID_D * PressureDerivative);

    // Update previous pressure error
    PressurePrevError := PressureError;

    // Regulate the flow control valve output based on the flow PID output
    FlowControlValve := FlowPID_Output;

    // Regulate the pressure control valve output based on the pressure PID output
    PressureControlValve := PressurePID_Output;

    // Saturation limits for valve outputs (0.0 to 100.0%)
    IF FlowControlValve > 100.0 THEN
        FlowControlValve := 100.0;
    ELSIF FlowControlValve < 0.0 THEN
        FlowControlValve := 0.0;
    END_IF

    IF PressureControlValve > 100.0 THEN
        PressureControlValve := 100.0;
    ELSIF PressureControlValve < 0.0 THEN
        PressureControlValve := 0.0;
    END_IF

    // Safety checks for flow and pressure
    IF FlowRate_Input > DesiredFlowRate + 10.0 OR FlowRate_Input < DesiredFlowRate - 10.0 THEN
        FlowFault := TRUE;                   // Trigger fault if flow deviates beyond +/-10 SLPM from setpoint
    ELSE
        FlowFault := FALSE;
    END_IF

    IF Pressure_Input < PressureLowerLimit - 0.5 OR Pressure_Input > PressureUpperLimit + 0.5 THEN
        PressureFault := TRUE;               // Trigger fault if pressure deviates beyond +/-0.5 bar from limits
    ELSE
        PressureFault := FALSE;
    END_IF

    // Safety shutdown if any fault is detected
    IF FlowFault OR PressureFault THEN
        SafetyShutdown := TRUE;              // Trigger safety shutdown
        FlowControlValve := 0.0;             // Set all valves to 0% to stop flow
        PressureControlValve := 0.0;
    ELSE
        SafetyShutdown := FALSE;
    END_IF

    // Output system status for external diagnostics
    (* Outputs like FlowControlValve and PressureControlValve can be linked to actuators *)
    (* SafetyShutdown, FlowFault, and PressureFault can be linked to alarms or indicators *)

END_PROGRAM
```

Explanation:

	1.	Variables:
	•	FlowRate_Input and Pressure_Input: Inputs representing the current flow rate and pressure in the system.
	•	DesiredFlowRate: The setpoint flow rate that the system should maintain (50 SLPM).
	•	PressureLowerLimit and PressureUpperLimit: The acceptable pressure range (5.5 to 6.0 bar).
	•	FlowControlValve and PressureControlValve: Outputs that control the flow and pressure regulating valves (range 0-100%).
	•	FlowPID_* and PressurePID_*: PID control parameters and variables for flow and pressure regulation.
	2.	PID Control:
	•	The program uses PID control to adjust the flow and pressure control valves.
	•	The FlowPID_Output and PressurePID_Output values are calculated based on the current error, integral, and derivative terms.
	•	The control outputs are constrained between 0% and 100% to ensure they are within the valid operating range.
	3.	Safety Checks:
	•	Flow Regulation: If the flow rate deviates more than ±10 SLPM from the setpoint, a flow fault is triggered.
	•	Pressure Regulation: If the pressure goes below 5.0 bar or above 6.5 bar, a pressure fault is triggered.
	•	Safety Shutdown: If either a flow fault or a pressure fault occurs, the system shuts down all control valves.
	4.	Control Loop Frequency:
	•	The program is designed to run at a 100 ms control loop frequency, ensuring timely updates to the PID control loops.
