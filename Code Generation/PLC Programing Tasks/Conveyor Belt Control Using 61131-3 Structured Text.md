Here’s a self-contained 61131-3 Structured Text program to control a conveyor belt system with three stations. The program manages the automatic and manual control modes, ensures the conveyor runs at a fixed speed of 2 meters per second, and prioritizes safety by stopping the conveyor whenever a stop command is issued or objects are not detected by the sensors.

```
PROGRAM ConveyorBeltControl
    // Variables for control inputs and sensors
    VAR
        // Manual control inputs from stations
        Station1_StopCmd: BOOL := FALSE;   // Stop command from Station 1
        Station2_StopCmd: BOOL := FALSE;   // Stop command from Station 2
        Station3_StopCmd: BOOL := FALSE;   // Stop command from Station 3

        // Sensors detecting object presence on the conveyor belt
        Sensor1: BOOL := FALSE;            // Sensor 1 detecting object
        Sensor2: BOOL := FALSE;            // Sensor 2 detecting object
        Sensor3: BOOL := FALSE;            // Sensor 3 detecting object
        Sensor4: BOOL := FALSE;            // Sensor 4 detecting object
        Sensor5: BOOL := FALSE;            // Sensor 5 detecting object

        // System status and control mode variables
        ConveyorSpeed: REAL := 0.0;        // Current conveyor speed (meters per second)
        ConveyorRunning: BOOL := FALSE;    // Conveyor running status
        ManualMode: BOOL := FALSE;         // Manual control mode
        AutoMode: BOOL := TRUE;            // Automatic control mode (default)
    END_VAR

    // Logic to switch between manual and automatic modes
    IF ManualMode THEN
        AutoMode := FALSE;                 // Disable automatic mode if manual mode is active
    ELSE
        AutoMode := TRUE;                  // Enable automatic mode if manual mode is not active
    END_IF

    // Manual Mode Logic: Control based on Station Stop Commands
    IF ManualMode THEN
        IF Station1_StopCmd OR Station2_StopCmd OR Station3_StopCmd THEN
            ConveyorRunning := FALSE;      // Stop the conveyor if any station stop command is active
        ELSE
            ConveyorRunning := TRUE;       // Run the conveyor if no stop commands are active
        END_IF
    END_IF

    // Automatic Mode Logic: Control based on Object Presence
    IF AutoMode THEN
        IF Sensor1 AND Sensor2 AND Sensor3 AND Sensor4 AND Sensor5 THEN
            ConveyorRunning := TRUE;       // Run the conveyor if all sensors detect objects
        ELSE
            ConveyorRunning := FALSE;      // Stop the conveyor if any sensor does not detect an object
        END_IF
    END_IF

    // Safety Override: Stop the conveyor if any manual stop command is triggered in any mode
    IF Station1_StopCmd OR Station2_StopCmd OR Station3_StopCmd THEN
        ConveyorRunning := FALSE;          // Stop the conveyor for safety if any stop command is active
    END_IF

    // Control the conveyor speed
    IF ConveyorRunning THEN
        ConveyorSpeed := 2.0;              // Set conveyor speed to 2 meters per second
    ELSE
        ConveyorSpeed := 0.0;              // Set conveyor speed to 0 if not running
    END_IF

    // Output conveyor status
    (* Outputs can be linked to external indicators or actuators here *)
    (* ConveyorRunning and ConveyorSpeed can be mapped to the conveyor motor control *)
    
END_PROGRAM
```

Explanation:

	1.	Variables:
	•	Control inputs (Station1_StopCmd, Station2_StopCmd, and Station3_StopCmd): Receive stop commands from three stations.
	•	Sensors (Sensor1 to Sensor5): Detect the presence of objects on the conveyor belt.
	•	ConveyorSpeed and ConveyorRunning: Monitor the conveyor’s speed and operational status.
	•	ManualMode and AutoMode: Determine whether the system is in manual or automatic control mode.
	2.	Control Modes:
	•	Manual Mode: The conveyor runs or stops based on manual stop commands from the stations.
	•	Automatic Mode: The conveyor runs only if all sensors detect the presence of objects.
	3.	Safety Logic:
	•	The conveyor immediately stops if any station triggers a stop command, irrespective of the control mode.
	•	The conveyor also stops if any sensor does not detect an object in automatic mode, ensuring safe operation.
	4.	Conveyor Speed:
	•	When the conveyor is running, it maintains a constant speed of 2 meters per second.
	•	If stopped, the speed is set to 0.
