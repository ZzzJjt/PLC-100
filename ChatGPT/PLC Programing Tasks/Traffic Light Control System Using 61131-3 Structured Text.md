Here’s a self-contained 61131-3 Structured Text program to control a traffic light system with pedestrian push button and emergency vehicle detection. The program ensures safe pedestrian crossings, smooth traffic flow, and prioritizes emergency vehicles by adjusting the light sequence to provide a clear path.

```
PROGRAM TrafficLightControl
    // Variables for system inputs, outputs, and control logic
    VAR
        // Traffic light states for Main and Side roads
        MainRoad_Light: INT := 0;             // 0 = RED, 1 = GREEN, 2 = YELLOW
        SideRoad_Light: INT := 0;             // 0 = RED, 1 = GREEN, 2 = YELLOW

        // Pedestrian request button states
        PedestrianButton_Main: BOOL := FALSE; // Pedestrian request for Main road crossing
        PedestrianButton_Side: BOOL := FALSE; // Pedestrian request for Side road crossing

        // Emergency vehicle detection
        EmergencyDetected: BOOL := FALSE;     // TRUE if an emergency vehicle is detected

        // Timing control variables
        LightTimer: TIME := T#0S;             // Timer for light transitions
        GreenTime: TIME := T#30S;             // Standard green light duration
        YellowTime: TIME := T#5S;             // Standard yellow light duration
        PedestrianGreenTime: TIME := T#15S;   // Pedestrian green light duration

        // Traffic light control states
        State: INT := 0;                      // Current state of the system (0 = Initial, 1 = Main Green, 2 = Main Yellow, 3 = Side Green, 4 = Side Yellow, 5 = Pedestrian Crossing)

        // Time tracking variables
        StateStartTime: TIME := T#0S;         // Time when the state started
        CurrentTime: TIME;                    // Current system time
    END_VAR

    // Define constants for light states
    CONST
        RED: INT := 0;                        // RED light state
        GREEN: INT := 1;                      // GREEN light state
        YELLOW: INT := 2;                     // YELLOW light state
    END_CONST

    // State machine for traffic light control
    CASE State OF
        0: // Initial State: Set main road to GREEN, side road to RED
            MainRoad_Light := GREEN;
            SideRoad_Light := RED;
            State := 1;
            StateStartTime := CurrentTime;

        1: // Main Road GREEN state
            IF EmergencyDetected THEN
                // If emergency is detected, give priority to main road GREEN
                MainRoad_Light := GREEN;
                SideRoad_Light := RED;
                State := 1;                    // Remain in this state as long as emergency is present
                StateStartTime := CurrentTime;
            ELSIF (CurrentTime - StateStartTime >= GreenTime) THEN
                // Transition to main road YELLOW state after GREEN time elapses
                MainRoad_Light := YELLOW;
                SideRoad_Light := RED;
                State := 2;
                StateStartTime := CurrentTime;
            END_IF

        2: // Main Road YELLOW state
            IF (CurrentTime - StateStartTime >= YellowTime) THEN
                // Transition to side road GREEN after YELLOW time elapses
                MainRoad_Light := RED;
                SideRoad_Light := GREEN;
                State := 3;
                StateStartTime := CurrentTime;
            END_IF

        3: // Side Road GREEN state
            IF EmergencyDetected THEN
                // If emergency is detected, switch to main road GREEN immediately
                MainRoad_Light := GREEN;
                SideRoad_Light := RED;
                State := 1;
                StateStartTime := CurrentTime;
            ELSIF (CurrentTime - StateStartTime >= GreenTime) THEN
                // Transition to side road YELLOW state after GREEN time elapses
                MainRoad_Light := RED;
                SideRoad_Light := YELLOW;
                State := 4;
                StateStartTime := CurrentTime;
            END_IF

        4: // Side Road YELLOW state
            IF (CurrentTime - StateStartTime >= YellowTime) THEN
                // Transition to Main road GREEN after YELLOW time elapses
                MainRoad_Light := GREEN;
                SideRoad_Light := RED;
                State := 1;
                StateStartTime := CurrentTime;
            END_IF

        5: // Pedestrian Crossing state
            IF (CurrentTime - StateStartTime >= PedestrianGreenTime) THEN
                // Return to main road GREEN after pedestrian crossing time elapses
                MainRoad_Light := GREEN;
                SideRoad_Light := RED;
                State := 1;
                StateStartTime := CurrentTime;
            END_IF
    END_CASE

    // Check for pedestrian button presses to initiate pedestrian crossing
    IF PedestrianButton_Main AND (State = 1) AND NOT EmergencyDetected THEN
        // Initiate pedestrian crossing on Main road
        MainRoad_Light := RED;
        SideRoad_Light := RED;
        State := 5;                           // Move to pedestrian crossing state
        StateStartTime := CurrentTime;
    ELSIF PedestrianButton_Side AND (State = 3) AND NOT EmergencyDetected THEN
        // Initiate pedestrian crossing on Side road
        MainRoad_Light := RED;
        SideRoad_Light := RED;
        State := 5;                           // Move to pedestrian crossing state
        StateStartTime := CurrentTime;
    END_IF

    // Output traffic light states for external connections
    (* Outputs can be linked to actual light indicators *)
    (* MainRoad_Light and SideRoad_Light can be mapped to specific physical lights *)

END_PROGRAM
```

Explanation:

	1.	Variables:
	•	MainRoad_Light and SideRoad_Light: Represent the current light state for the main and side roads (0 = RED, 1 = GREEN, 2 = YELLOW).
	•	PedestrianButton_Main and PedestrianButton_Side: Boolean values representing pedestrian request buttons.
	•	EmergencyDetected: Indicates the presence of an emergency vehicle.
	•	Timing variables (LightTimer, GreenTime, YellowTime, and PedestrianGreenTime): Control the timing for light transitions.
	•	State: Represents the current state of the traffic light system.
	•	StateStartTime and CurrentTime: Track the time for each state transition.
	2.	Light States:
	•	The program uses a state machine approach to control light sequences.
	•	Main Road GREEN: Normal traffic flow for the main road.
	•	Main Road YELLOW: Transition period before switching to the side road.
	•	Side Road GREEN: Normal traffic flow for the side road.
	•	Side Road YELLOW: Transition period before switching back to the main road.
	•	Pedestrian Crossing: Allows pedestrians to cross when a button is pressed.
	3.	Emergency Vehicle Handling:
	•	The system gives priority to emergency vehicles by keeping the main road GREEN.
	•	If an emergency is detected, the program immediately switches to or maintains the main road GREEN, regardless of the current state.
	4.	Pedestrian Crossing:
	•	If a pedestrian button is pressed on either the main or side road, the system switches to the pedestrian crossing state (State = 5), which turns both roads RED for safe pedestrian passage.
	•	After the pedestrian crossing time elapses, the program transitions back to the normal sequence.
	5.	Timing Control:
	•	GreenTime and YellowTime define the duration for each state.
	•	PedestrianGreenTime specifies the duration for safe pedestrian crossing.
