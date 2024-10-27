Here’s a self-contained PID controller function block implemented in IEC 61131-3 Structured Text. This function block includes configurable parameters for proportional, integral, and derivative gains, error handling, and manual tuning capability.

```
FUNCTION_BLOCK FB_PIDController
VAR_INPUT
    Setpoint   : REAL;      // Desired value (target value)
    ProcessVar : REAL;      // Current value of the process variable
    Kp         : REAL;      // Proportional gain
    Ki         : REAL;      // Integral gain
    Kd         : REAL;      // Derivative gain
    Ts         : REAL;      // Sampling time in seconds (e.g., Ts = 1.0 for 1 second)
    Mode       : BOOL;      // TRUE = Automatic, FALSE = Manual
    ManualOutput : REAL;    // Output value in manual mode
END_VAR

VAR_OUTPUT
    PIDOutput  : REAL;      // Output value of the PID controller
    Error      : REAL;      // Error between Setpoint and ProcessVar
    ValidInput : BOOL;      // Indicates if the input parameters are valid
END_VAR

VAR
    PrevError  : REAL;      // Previous error value (for derivative calculation)
    Integral   : REAL;      // Accumulated integral term
    Derivative : REAL;      // Derivative term
    Output     : REAL;      // Calculated PID output
    MaxOutput  : REAL := 100.0;  // Maximum output limit
    MinOutput  : REAL := -100.0; // Minimum output limit
END_VAR

// Input validation
IF (Kp >= 0.0) AND (Ki >= 0.0) AND (Kd >= 0.0) AND (Ts > 0.0) THEN
    ValidInput := TRUE;
ELSE
    ValidInput := FALSE;
    PIDOutput := 0.0;
    RETURN;
END_IF;

// Calculate error
Error := Setpoint - ProcessVar;

IF Mode THEN
    // Automatic mode: PID calculations
    // Proportional term
    Output := Kp * Error;

    // Integral term
    Integral := Integral + (Ki * Error * Ts);

    // Anti-windup: Limit the integral term to prevent overshoot
    IF Integral > MaxOutput THEN
        Integral := MaxOutput;
    ELSIF Integral < MinOutput THEN
        Integral := MinOutput;
    END_IF;

    // Derivative term
    Derivative := Kd * (Error - PrevError) / Ts;

    // Calculate PID output
    Output := Output + Integral + Derivative;

    // Apply output limits
    IF Output > MaxOutput THEN
        Output := MaxOutput;
    ELSIF Output < MinOutput THEN
        Output := MinOutput;
    END_IF;

    // Store PID output in PIDOutput
    PIDOutput := Output;
ELSE
    // Manual mode: Directly use manual output
    PIDOutput := ManualOutput;
END_IF;

// Store the current error as previous error for next cycle
PrevError := Error;

END_FUNCTION_BLOCK
```

Key Features:

	1.	Configurable PID Parameters:
	•	Kp: Proportional gain.
	•	Ki: Integral gain.
	•	Kd: Derivative gain.
	•	Ts: Sampling time interval, used to calculate the integral and derivative terms.
	2.	Modes of Operation:
	•	Mode: Selects between Automatic (PID control) and Manual mode.
	•	TRUE = Automatic mode: The function block performs the PID calculations.
	•	FALSE = Manual mode: The output is directly controlled using the ManualOutput input.
	3.	PID Calculations:
	•	Proportional Term (Kp * Error): Reacts proportionally to the current error.
	•	Integral Term (Ki * Error * Ts): Accounts for accumulated error over time.
	•	Anti-windup mechanism limits the integral term to avoid excessive overshoot.
	•	Derivative Term (Kd * (Error - PrevError) / Ts): Predicts future error changes based on the rate of change.
	4.	Output Limits:
	•	MaxOutput and MinOutput are set to 100.0 and -100.0 by default, but can be adjusted based on the system requirements.
	•	Ensures that the calculated output does not exceed the defined boundaries.
	5.	Input Validation:
	•	The function block checks that all gain values and the sampling time are non-negative and that the sampling time is greater than zero.
	•	If any parameter is invalid, ValidInput is set to FALSE and the PID calculations are bypassed.
	6.	Output Signals:
	•	PIDOutput: The calculated or manually set output value.
	•	Error: The difference between the Setpoint and the ProcessVar.
	•	ValidInput: Indicates if the provided input parameters are valid for PID calculations.
