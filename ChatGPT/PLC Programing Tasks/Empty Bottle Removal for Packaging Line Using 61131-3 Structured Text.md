Here’s a self-contained 61131-3 Structured Text program to automate the removal of empty bottles in a packaging line. The program uses two proximity sensors to detect empty and filled bottles and controls a pneumatic cylinder to remove empty bottles from the conveyor.

```
PROGRAM EmptyBottleRemoval
    // Variable declarations for inputs, outputs, and control logic
    VAR
        // Input sensors
        BottleDetected: BOOL := FALSE;           // Proximity sensor to detect the presence of any bottle
        EmptyBottleDetected: BOOL := FALSE;      // Proximity sensor to detect only empty bottles

        // Output actuators
        ConveyorMotor: BOOL := FALSE;            // Control signal for the conveyor motor
        PneumaticCylinder: BOOL := FALSE;        // Control signal for the pneumatic cylinder to remove empty bottles

        // Control flags
        EmptyBottlePresent: BOOL := FALSE;       // Flag to indicate the presence of an empty bottle
        RemoveEmptyBottle: BOOL := FALSE;        // Flag to indicate that the empty bottle should be removed

        // Timing variables
        CylinderExtendTime: TIME := T#1S;        // Time to extend the pneumatic cylinder (1 second)
        CylinderTimer: TIME := T#0S;             // Timer to control the pneumatic cylinder operation

        // Process status variables
        SystemReady: BOOL := TRUE;               // System status to indicate the line is ready for operation
    END_VAR

    // ---------------------- System Initialization ----------------------
    IF NOT BottleDetected THEN
        // Ensure the conveyor starts running when no bottle is detected
        ConveyorMotor := TRUE;
        PneumaticCylinder := FALSE;              // Ensure the pneumatic cylinder is retracted
        SystemReady := TRUE;                     // Set the system to ready state
    END_IF

    // ---------------------- Bottle Detection Logic ----------------------
    // Detect when a bottle is present on the conveyor
    IF BottleDetected THEN
        // Check if the detected bottle is empty
        IF EmptyBottleDetected THEN
            EmptyBottlePresent := TRUE;          // Set the flag if an empty bottle is detected
            RemoveEmptyBottle := TRUE;           // Indicate that the empty bottle should be removed
        ELSE
            EmptyBottlePresent := FALSE;         // Reset flag if the bottle is not empty
            RemoveEmptyBottle := FALSE;          // No removal needed for filled bottles
        END_IF
    END_IF

    // ---------------------- Empty Bottle Removal Logic ----------------------
    IF RemoveEmptyBottle AND SystemReady THEN
        // Stop the conveyor and activate the pneumatic cylinder to remove the empty bottle
        ConveyorMotor := FALSE;                  // Stop the conveyor to position the empty bottle for removal
        PneumaticCylinder := TRUE;               // Activate the pneumatic cylinder to push the empty bottle
        CylinderTimer := CylinderExtendTime;     // Set the timer for cylinder operation
        SystemReady := FALSE;                    // Set system ready status to false during removal
    END_IF

    // ---------------------- Cylinder Timing and Reset Logic ----------------------
    IF CylinderTimer > T#0S THEN
        // Decrease the timer for the pneumatic cylinder
        CylinderTimer := CylinderTimer - T#100MS; // Decrease the timer by 100ms per scan cycle
    ELSE
        // When the timer reaches zero, retract the cylinder and resume normal operation
        IF PneumaticCylinder THEN
            PneumaticCylinder := FALSE;          // Retract the pneumatic cylinder
            ConveyorMotor := TRUE;               // Restart the conveyor motor after removing the empty bottle
            RemoveEmptyBottle := FALSE;          // Reset the empty bottle removal flag
            SystemReady := TRUE;                 // Set system ready status to true
        END_IF
    END_IF

    // ---------------------- Output Control Mapping ----------------------
    // ConveyorMotor: Controls the conveyor motor (TRUE = ON, FALSE = OFF)
    // PneumaticCylinder: Controls the pneumatic cylinder (TRUE = Extend, FALSE = Retract)

END_PROGRAM
```
Explanation:

	1.	Input Variables:
	•	BottleDetected: Detects the presence of any bottle on the conveyor.
	•	EmptyBottleDetected: Detects whether the detected bottle is empty.
	2.	Output Variables:
	•	ConveyorMotor: Controls the conveyor motor to move bottles toward the packaging station.
	•	PneumaticCylinder: Controls the pneumatic cylinder to push empty bottles off the conveyor.
	3.	Control Flags:
	•	EmptyBottlePresent: Indicates whether the detected bottle is empty.
	•	RemoveEmptyBottle: A flag to initiate the empty bottle removal process.
	4.	Timing Variables:
	•	CylinderExtendTime: Set to 1 second, representing the time needed to extend and retract the pneumatic cylinder.
	•	CylinderTimer: Tracks the timer for controlling the duration of the pneumatic cylinder operation.
	5.	Process Logic:
	•	The conveyor starts in a running state (ConveyorMotor = TRUE).
	•	When BottleDetected is activated:
	•	If EmptyBottleDetected is also active, the program sets the EmptyBottlePresent and RemoveEmptyBottle flags.
	•	When RemoveEmptyBottle is set:
	•	The program stops the conveyor (ConveyorMotor = FALSE), extends the pneumatic cylinder (PneumaticCylinder = TRUE), and starts the timer (CylinderTimer = CylinderExtendTime).
	•	After the timer elapses:
	•	The cylinder retracts (PneumaticCylinder = FALSE), the conveyor resumes (ConveyorMotor = TRUE), and the removal process is reset.
	6.	Output Control Mapping:
	•	The ConveyorMotor and PneumaticCylinder signals control the conveyor and pneumatic cylinder operations, respectively.
