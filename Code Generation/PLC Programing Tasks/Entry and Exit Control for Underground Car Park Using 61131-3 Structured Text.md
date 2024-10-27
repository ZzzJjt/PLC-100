Here’s a self-contained 61131-3 Structured Text program to control the entry and exit of an underground car park using the provided sensors and actuators. The program manages car movement based on the status of photoelectric switches and intermediate variables, ensuring only one car can pass through the single-lane passage at a time.

```
PROGRAM CarParkControl
    // Variable declarations for inputs, outputs, and intermediate states
    VAR
        // Input sensors (Photoelectric switches)
        X1: BOOL := FALSE;               // Photoelectric switch at the ground floor entry/exit
        X2: BOOL := FALSE;               // Photoelectric switch at the basement entry/exit

        // Intermediate variables triggered for one scan cycle
        M1: BOOL := FALSE;               // Triggered when a car from ground floor passes X1
        M2: BOOL := FALSE;               // Triggered when a car from basement passes X1
        M3: BOOL := FALSE;               // Triggered when a car from basement passes X2
        M4: BOOL := FALSE;               // Triggered when a car from ground floor passes X2

        // Process variables for car movement in the passage
        M20: BOOL := FALSE;              // Active when a car is entering the passage from the ground floor
        M30: BOOL := FALSE;              // Active when a car is entering the passage from the basement

        // Output devices (Traffic lights)
        Y1: BOOL := FALSE;               // Red lights at the entry/exit of the ground floor and basement
        Y2: BOOL := TRUE;                // Green lights at the entry/exit of the ground floor and basement (Initially ON)
    END_VAR

    // Process Description and Logic

    // 1. Detect cars entering the passage from the ground floor
    IF X1 AND NOT M20 AND NOT M30 THEN
        M1 := TRUE;                      // Car entering from ground floor
        M20 := TRUE;                     // Set the flag for ground floor entry in process
    END_IF

    // 2. Detect cars entering the passage from the basement
    IF X2 AND NOT M20 AND NOT M30 THEN
        M3 := TRUE;                      // Car entering from basement
        M30 := TRUE;                     // Set the flag for basement entry in process
    END_IF

    // 3. Handle car movement from ground floor to basement
    IF M1 THEN
        Y1 := TRUE;                      // Turn on red lights at both ground floor and basement
        Y2 := FALSE;                     // Turn off green lights at both ground floor and basement
        M1 := FALSE;                     // Reset M1 after detection
    END_IF

    // 4. Car reaches basement from ground floor
    IF X2 AND M20 THEN
        M4 := TRUE;                      // Car exiting the passage to the basement
        M20 := FALSE;                    // Reset ground floor entry flag
    END_IF

    // 5. Handle car movement from basement to ground floor
    IF M3 THEN
        Y1 := TRUE;                      // Turn on red lights at both ground floor and basement
        Y2 := FALSE;                     // Turn off green lights at both ground floor and basement
        M3 := FALSE;                     // Reset M3 after detection
    END_IF

    // 6. Car reaches ground floor from basement
    IF X1 AND M30 THEN
        M2 := TRUE;                      // Car exiting the passage to the ground floor
        M30 := FALSE;                    // Reset basement entry flag
    END_IF

    // 7. Passage is clear; allow free movement
    IF M2 OR M4 THEN
        Y1 := FALSE;                     // Turn off red lights at both ground floor and basement
        Y2 := TRUE;                      // Turn on green lights at both ground floor and basement
        M2 := FALSE;                     // Reset M2
        M4 := FALSE;                     // Reset M4
    END_IF

    // Output mapping
    (* Y1: Red light control at both entry points (TRUE = ON, FALSE = OFF) *)
    (* Y2: Green light control at both entry points (TRUE = ON, FALSE = OFF) *)

END_PROGRAM
```

Explanation:

	1.	Input Variables:
	•	X1: Photoelectric switch at the ground floor entry/exit. It will be ON when a car passes through this point.
	•	X2: Photoelectric switch at the basement entry/exit. It will be ON when a car passes through this point.
	2.	Intermediate Variables:
	•	M1: Triggered for one scan cycle when a car enters the passage from the ground floor (passing through X1).
	•	M2: Triggered for one scan cycle when a car exits the passage to the ground floor.
	•	M3: Triggered for one scan cycle when a car enters the passage from the basement (passing through X2).
	•	M4: Triggered for one scan cycle when a car exits the passage to the basement.
	•	M20: Set when a car is entering the passage from the ground floor.
	•	M30: Set when a car is entering the passage from the basement.
	3.	Output Variables:
	•	Y1: Red lights at both entry/exit points to stop cars from entering the passage (initially OFF).
	•	Y2: Green lights at both entry/exit points to allow cars to move freely (initially ON).
	4.	Process Description:
	•	When a car is detected entering the passage from either the ground floor (X1) or basement (X2), the red lights (Y1) turn ON at both ends, and the green lights (Y2) turn OFF to prevent any other cars from entering until the passage is clear.
	•	The flags M20 and M30 are used to track car movement through the passage.
	•	When the car exits the passage, the corresponding flag (M2 for ground floor exit, M4 for basement exit) is set.
	•	After the car exits and the passage is clear, the green lights (Y2) turn ON again, allowing free movement.
	5.	State Management:
	•	The system uses intermediate flags (M1, M2, M3, M4, M20, M30) to manage and track car movement through the single-lane passage.
	•	Each stage of car movement (entry, passage, exit) is monitored to ensure safe control of the lights.
	6.	Initial State:
	•	The program starts with Y1 (red lights) set to OFF and Y2 (green lights) set to ON, allowing cars to enter and exit freely when the passage is clear.
