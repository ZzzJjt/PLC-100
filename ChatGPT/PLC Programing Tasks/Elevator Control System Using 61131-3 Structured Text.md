Here’s a self-contained 61131-3 structured text program to control an elevator system in a 5-floor building. The program uses limit switches to detect the elevator’s position and implements door control logic based on passenger requests. It prioritizes elevator movement based on the current direction and call buttons from each floor, while ensuring the door remains open for a specified duration.

```
PROGRAM ElevatorControl
    // Variables for system inputs, outputs, and control logic
    VAR
        // Elevator position inputs (limit switches)
        LimitSwitch_Floor1_Top: BOOL := FALSE;   // Top limit switch at Floor 1
        LimitSwitch_Floor1_Bottom: BOOL := FALSE; // Bottom limit switch at Floor 1
        LimitSwitch_Floor2_Top: BOOL := FALSE;   // Top limit switch at Floor 2
        LimitSwitch_Floor2_Bottom: BOOL := FALSE; // Bottom limit switch at Floor 2
        LimitSwitch_Floor3_Top: BOOL := FALSE;   // Top limit switch at Floor 3
        LimitSwitch_Floor3_Bottom: BOOL := FALSE; // Bottom limit switch at Floor 3
        LimitSwitch_Floor4_Top: BOOL := FALSE;   // Top limit switch at Floor 4
        LimitSwitch_Floor4_Bottom: BOOL := FALSE; // Bottom limit switch at Floor 4
        LimitSwitch_Floor5_Top: BOOL := FALSE;   // Top limit switch at Floor 5
        LimitSwitch_Floor5_Bottom: BOOL := FALSE; // Bottom limit switch at Floor 5

        // Call buttons on each floor
        CallButton_Up_Floor1: BOOL := FALSE;     // Up call button on Floor 1
        CallButton_Up_Floor2: BOOL := FALSE;     // Up call button on Floor 2
        CallButton_Up_Floor3: BOOL := FALSE;     // Up call button on Floor 3
        CallButton_Up_Floor4: BOOL := FALSE;     // Up call button on Floor 4
        CallButton_Down_Floor2: BOOL := FALSE;   // Down call button on Floor 2
        CallButton_Down_Floor3: BOOL := FALSE;   // Down call button on Floor 3
        CallButton_Down_Floor4: BOOL := FALSE;   // Down call button on Floor 4
        CallButton_Down_Floor5: BOOL := FALSE;   // Down call button on Floor 5

        // Elevator cabin buttons for each floor
        CabinButton_Floor1: BOOL := FALSE;       // Button for Floor 1 inside the elevator
        CabinButton_Floor2: BOOL := FALSE;       // Button for Floor 2 inside the elevator
        CabinButton_Floor3: BOOL := FALSE;       // Button for Floor 3 inside the elevator
        CabinButton_Floor4: BOOL := FALSE;       // Button for Floor 4 inside the elevator
        CabinButton_Floor5: BOOL := FALSE;       // Button for Floor 5 inside the elevator

        // Control outputs for the elevator
        ElevatorUp: BOOL := FALSE;               // Elevator moving up
        ElevatorDown: BOOL := FALSE;             // Elevator moving down
        ElevatorStop: BOOL := TRUE;              // Elevator stopped
        DoorOpen: BOOL := FALSE;                 // Elevator door open
        DoorClose: BOOL := TRUE;                 // Elevator door closed

        // Timer variables for door control
        DoorTimer: TIME := T#0S;                 // Timer for door open duration
        DoorOpenTime: TIME := T#7S;              // Default door open duration
        ExtendedDoorOpenTime: TIME := T#10S;     // Extended door open duration if no cabin button is pressed

        // Elevator position tracking and direction
        CurrentFloor: INT := 0;                  // Current floor of the elevator (1-5)
        RequestedFloor: INT := 0;                // Requested floor based on buttons
        DirectionUp: BOOL := TRUE;               // TRUE = Up, FALSE = Down

        // Status flags
        DoorExtendedOpen: BOOL := FALSE;         // Indicates if the door is in the extended open state
    END_VAR

    // Detect the current floor based on limit switches
    IF LimitSwitch_Floor1_Top AND LimitSwitch_Floor1_Bottom THEN
        CurrentFloor := 1;
    ELSIF LimitSwitch_Floor2_Top AND LimitSwitch_Floor2_Bottom THEN
        CurrentFloor := 2;
    ELSIF LimitSwitch_Floor3_Top AND LimitSwitch_Floor3_Bottom THEN
        CurrentFloor := 3;
    ELSIF LimitSwitch_Floor4_Top AND LimitSwitch_Floor4_Bottom THEN
        CurrentFloor := 4;
    ELSIF LimitSwitch_Floor5_Top AND LimitSwitch_Floor5_Bottom THEN
        CurrentFloor := 5;
    END_IF

    // Determine requested floor based on call and cabin buttons
    IF CabinButton_Floor1 OR CallButton_Up_Floor1 THEN
        RequestedFloor := 1;
    ELSIF CabinButton_Floor2 OR CallButton_Up_Floor2 OR CallButton_Down_Floor2 THEN
        RequestedFloor := 2;
    ELSIF CabinButton_Floor3 OR CallButton_Up_Floor3 OR CallButton_Down_Floor3 THEN
        RequestedFloor := 3;
    ELSIF CabinButton_Floor4 OR CallButton_Up_Floor4 OR CallButton_Down_Floor4 THEN
        RequestedFloor := 4;
    ELSIF CabinButton_Floor5 OR CallButton_Down_Floor5 THEN
        RequestedFloor := 5;
    END_IF

    // Determine elevator direction based on current and requested floor
    IF RequestedFloor > CurrentFloor THEN
        DirectionUp := TRUE;
    ELSIF RequestedFloor < CurrentFloor THEN
        DirectionUp := FALSE;
    END_IF

    // Elevator movement logic
    IF CurrentFloor = RequestedFloor THEN
        ElevatorStop := TRUE;
        ElevatorUp := FALSE;
        ElevatorDown := FALSE;

        // Door control logic
        IF NOT DoorOpen THEN
            DoorOpen := TRUE;
            DoorClose := FALSE;
            DoorTimer := DoorOpenTime;           // Start the door open timer
            DoorExtendedOpen := FALSE;           // Reset the extended open flag
        ELSE
            // Check if any cabin button is pressed within 7 seconds
            IF (CabinButton_Floor1 OR CabinButton_Floor2 OR CabinButton_Floor3 OR CabinButton_Floor4 OR CabinButton_Floor5) AND (DoorTimer > T#0S) THEN
                DoorTimer := T#0S;               // Reset the door timer if a button is pressed
            END_IF

            // Check for door open timer expiry
            IF DoorTimer <= T#0S AND NOT DoorExtendedOpen THEN
                // If no button was pressed, keep door open for an additional 10 seconds
                DoorExtendedOpen := TRUE;
                DoorTimer := ExtendedDoorOpenTime; // Set the extended open time
            ELSIF DoorTimer <= T#0S AND DoorExtendedOpen THEN
                // Close the door after the extended duration
                DoorOpen := FALSE;
                DoorClose := TRUE;
            END_IF
        END_IF
    ELSE
        // Move the elevator based on the requested floor and direction
        IF DirectionUp THEN
            ElevatorUp := TRUE;
            ElevatorDown := FALSE;
            ElevatorStop := FALSE;
        ELSE
            ElevatorUp := FALSE;
            ElevatorDown := TRUE;
            ElevatorStop := FALSE;
        END_IF

        // Ensure the door is closed during movement
        DoorOpen := FALSE;
        DoorClose := TRUE;
    END_IF

    // Timer countdown logic
    IF DoorTimer > T#0S THEN
        DoorTimer := DoorTimer - T#100MS;        // Decrease the door timer every 100ms
    END_IF

    // Output elevator and door states for external connections
    (* Outputs like ElevatorUp, ElevatorDown, ElevatorStop, DoorOpen, and DoorClose can be linked to actuators or indicators *)

END_PROGRAM
```
Explanation:

	1.	Variables:
	•	Position Inputs: LimitSwitch_Floor1_Top to LimitSwitch_Floor5_Bottom represent limit switches for each floor to detect the elevator’s position.
	•	Call Buttons: CallButton_Up_Floor1 to CallButton_Down_Floor5 represent call buttons at each floor.
	•	Cabin Buttons: CabinButton_Floor1 to CabinButton_Floor5 represent the buttons inside the elevator for selecting the desired floor.
	•	Control Outputs: ElevatorUp, ElevatorDown, ElevatorStop control elevator movement, and DoorOpen, DoorClose control the door state.
	•	Timer Variables: DoorTimer manages the door open duration, and DoorOpenTime and ExtendedDoorOpenTime specify the default and extended door open times.
	•	Tracking Variables: CurrentFloor tracks the current position of the elevator, and RequestedFloor determines which floor to move to next.
	2.	Elevator Position Detection:
	•	The program identifies the elevator’s position using top and bottom limit switches at each floor.
	3.	Floor Request Handling:
	•	The elevator moves based on requests from cabin buttons and call buttons at each floor.
