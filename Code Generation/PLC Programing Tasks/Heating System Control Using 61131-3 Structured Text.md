Here’s a self-contained 61131-3 Structured Text program to control a heating system based on three temperature sensors. The program ensures smooth regulation of the temperature to maintain a set range between 20°C and 22°C. It also includes logic for minimizing frequent switching, handling sensor faults, and implementing safety measures in the event of temperature deviations beyond safe limits.

```
PROGRAM HeatingSystemControl
    // Variables for system inputs and control
    VAR
        // Temperature sensors
        Sensor1_Temperature: REAL := 0.0;      // Temperature from Sensor 1 (°C)
        Sensor2_Temperature: REAL := 0.0;      // Temperature from Sensor 2 (°C)
        Sensor3_Temperature: REAL := 0.0;      // Temperature from Sensor 3 (°C)

        // Control setpoints and hysteresis values
        Target_LowerLimit: REAL := 20.0;       // Minimum temperature setpoint (°C)
        Target_UpperLimit: REAL := 22.0;       // Maximum temperature setpoint (°C)
        Hysteresis: REAL := 0.5;               // Hysteresis for smooth regulation (°C)

        // System control variables
        AverageTemperature: REAL := 0.0;       // Average temperature from three sensors
        HeatingOn: BOOL := FALSE;              // Heating system status (ON/OFF)
        HeatingStable: BOOL := FALSE;          // Status to indicate stable heating condition
        SensorFault: BOOL := FALSE;            // Fault status for sensor values
        SafetyShutdown: BOOL := FALSE;         // Safety shutdown status for critical conditions

        // Time control for smooth switching
        LastSwitchTime: TIME := T#0S;          // Time of the last switch operation
        MinSwitchInterval: TIME := T#10S;      // Minimum time interval between switches
        CurrentTime: TIME;                     // Current system time
    END_VAR

    // Calculate the average temperature from three sensors
    AverageTemperature := (Sensor1_Temperature + Sensor2_Temperature + Sensor3_Temperature) / 3.0;

    // Safety check: Detect sensor fault if any sensor reads unrealistic values (e.g., below -50°C or above 100°C)
    IF (Sensor1_Temperature < -50.0 OR Sensor1_Temperature > 100.0) OR
       (Sensor2_Temperature < -50.0 OR Sensor2_Temperature > 100.0) OR
       (Sensor3_Temperature < -50.0 OR Sensor3_Temperature > 100.0) THEN
        SensorFault := TRUE;
        HeatingOn := FALSE;                    // Turn off heating if any sensor fault is detected
    ELSE
        SensorFault := FALSE;
    END_IF

    // Safety shutdown if temperature deviates beyond safe limits (e.g., below 10°C or above 30°C)
    IF AverageTemperature < 10.0 OR AverageTemperature > 30.0 THEN
        SafetyShutdown := TRUE;                // Trigger safety shutdown if temperature is out of safe range
        HeatingOn := FALSE;                    // Turn off heating during safety shutdown
    ELSE
        SafetyShutdown := FALSE;
    END_IF

    // Heating control logic with hysteresis to prevent frequent switching
    IF NOT SensorFault AND NOT SafetyShutdown THEN
        IF HeatingOn THEN
            // Turn off heating if average temperature exceeds upper limit + hysteresis
            IF AverageTemperature > Target_UpperLimit + Hysteresis THEN
                HeatingOn := FALSE;
                HeatingStable := TRUE;          // Indicate stable condition for smooth operation
                LastSwitchTime := CurrentTime;  // Record the time of this switch operation
            END_IF
        ELSE
            // Turn on heating if average temperature falls below lower limit - hysteresis
            IF AverageTemperature < Target_LowerLimit - Hysteresis THEN
                IF (CurrentTime - LastSwitchTime) >= MinSwitchInterval THEN
                    HeatingOn := TRUE;          // Turn on heating only if minimum switch interval is satisfied
                    HeatingStable := FALSE;     // Reset stable condition status when heating is turned on
                    LastSwitchTime := CurrentTime;  // Record the time of this switch operation
                END_IF
            END_IF
        END_IF
    END_IF

    // Output heating system status and safety indications
    (* Outputs can be linked to external indicators, actuators, or alarms *)
    (* HeatingOn indicates whether the heating system is active or inactive *)
    (* HeatingStable can be used for smooth operation monitoring *)
    (* SensorFault and SafetyShutdown can trigger alarms or system diagnostics *)

END_PROGRAM
```
Explanation:

	1.	Variables:
	•	Sensor1_Temperature, Sensor2_Temperature, and Sensor3_Temperature: Readings from three temperature sensors.
	•	Target_LowerLimit and Target_UpperLimit: Define the desired temperature range between 20°C and 22°C.
	•	Hysteresis: Used to prevent frequent switching by defining a buffer around the setpoints.
	•	AverageTemperature: Calculates the average temperature from all three sensors to control the heating.
	•	HeatingOn: Status of the heating system.
	•	HeatingStable: Indicates stable heating conditions for smooth operation.
	•	SensorFault: Flag for sensor fault detection based on unrealistic values.
	•	SafetyShutdown: Triggered when temperature goes beyond safe limits (e.g., below 10°C or above 30°C).
	•	LastSwitchTime and MinSwitchInterval: Used to prevent frequent on-off switching of the heating system.
	2.	Temperature Regulation:
	•	The program calculates the average temperature from three sensors and uses this value to control the heating system.
	•	The heating system turns ON if the average temperature falls below Target_LowerLimit - Hysteresis.
	•	The heating system turns OFF if the average temperature exceeds Target_UpperLimit + Hysteresis.
	•	The use of a hysteresis range prevents the system from toggling frequently between on and off states.
	3.	Safety Measures:
	•	Sensor faults are detected if any temperature reading is out of realistic bounds (below -50°C or above 100°C).
	•	If a sensor fault is detected, the heating system is turned off to avoid unsafe conditions.
	•	Safety shutdown is triggered if the average temperature is below 10°C or above 30°C, turning off the heating to prevent hazardous conditions.
	4.	Smooth Switching:
	•	The MinSwitchInterval ensures that the heating system does not switch on and off too frequently, which could reduce the system’s lifespan and efficiency.
	•	The last switch time (LastSwitchTime) is recorded, and the program checks that the interval since the last switch is greater than or equal to MinSwitchInterval before allowing another switch.
