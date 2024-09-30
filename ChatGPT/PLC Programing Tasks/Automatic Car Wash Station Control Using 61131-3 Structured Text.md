Here’s a self-contained 61131-3 Structured Text program to control an automatic car wash station with a single wash bay. The program manages car detection, wash process initiation, and safety monitoring for human presence. If a human is detected, the wash process stops, an alarm is triggered, and the system enters a safe state until the area is clear.

```
PROGRAM CarWashControl
    // Variables for system inputs, outputs, and control logic
    VAR
        // Input sensors
        CarDetected: BOOL := FALSE;           // Sensor to detect the presence of a car in the wash bay
        HumanDetected: BOOL := FALSE;         // Sensor to detect a human in the wash area
        EmergencyStop: BOOL := FALSE;         // Emergency stop button input

        // Wash process stages
        PreWashStage: BOOL := FALSE;          // Indicates the Pre-Wash stage
        SoapStage: BOOL := FALSE;             // Indicates the Soap application stage
        BrushStage: BOOL := FALSE;            // Indicates the Brushing stage
        RinseStage: BOOL := FALSE;            // Indicates the Rinsing stage
        DryStage: BOOL := FALSE;              // Indicates the Drying stage

        // Output control signals
        ConveyorMotor: BOOL := FALSE;         // Control the conveyor to move the car through the wash stages
        PreWashSpray: BOOL := FALSE;          // Control the Pre-Wash water spray
        SoapSpray: BOOL := FALSE;             // Control the Soap application spray
        Brushes: BOOL := FALSE;               // Control the rotating brushes
        RinseSpray: BOOL := FALSE;            // Control the Rinse water spray
        Dryer: BOOL := FALSE;                 // Control the Dryers

        // Safety and alarm outputs
        Alarm: BOOL := FALSE;                 // Alarm to indicate human detected in wash area
        SafeState: BOOL := FALSE;             // Indicates the system is in a safe state
        SystemReset: BOOL := FALSE;           // System reset input to clear safe state and resume operation

        // Process timing variables
        PreWashTime: TIME := T#10S;           // Duration for Pre-Wash stage
        SoapTime: TIME := T#15S;              // Duration for Soap application stage
        BrushTime: TIME := T#20S;             // Duration for Brush stage
        RinseTime: TIME := T#10S;             // Duration for Rinse stage
        DryTime: TIME := T#15S;               // Duration for Drying stage
        StageTimer: TIME := T#0S;             // Timer for current wash stage

        // Status variables
        WashInProgress: BOOL := FALSE;        // Indicates if a wash cycle is currently in progress
    END_VAR

    // State machine to control the car wash process
    IF NOT WashInProgress THEN
        // Wait for a car to be detected and no human in the area
        IF CarDetected AND NOT HumanDetected AND NOT SafeState THEN
            WashInProgress := TRUE;           // Start the wash process
            PreWashStage := TRUE;             // Initiate Pre-Wash stage
            ConveyorMotor := TRUE;            // Start the conveyor to move car
            StageTimer := PreWashTime;        // Set the timer for Pre-Wash
        END_IF
    ELSE
        // Execute wash stages based on the current stage and timer
        IF PreWashStage THEN
            PreWashSpray := TRUE;             // Activate Pre-Wash spray
            IF StageTimer <= T#0S THEN
                PreWashSpray := FALSE;        // Stop Pre-Wash spray
                PreWashStage := FALSE;        // End Pre-Wash stage
                SoapStage := TRUE;            // Move to Soap application stage
                StageTimer := SoapTime;       // Set the timer for Soap application
            END_IF

        ELSIF SoapStage THEN
            SoapSpray := TRUE;                // Activate Soap spray
            IF StageTimer <= T#0S THEN
                SoapSpray := FALSE;           // Stop Soap spray
                SoapStage := FALSE;           // End Soap application stage
                BrushStage := TRUE;           // Move to Brushing stage
                StageTimer := BrushTime;      // Set the timer for Brushing
            END_IF

        ELSIF BrushStage THEN
            Brushes := TRUE;                  // Activate Brushes
            IF StageTimer <= T#0S THEN
                Brushes := FALSE;             // Stop Brushes
                BrushStage := FALSE;          // End Brushing stage
                RinseStage := TRUE;           // Move to Rinsing stage
                StageTimer := RinseTime;      // Set the timer for Rinsing
            END_IF

        ELSIF RinseStage THEN
            RinseSpray := TRUE;               // Activate Rinse spray
            IF StageTimer <= T#0S THEN
                RinseSpray := FALSE;          // Stop Rinse spray
                RinseStage := FALSE;          // End Rinsing stage
                DryStage := TRUE;             // Move to Drying stage
                StageTimer := DryTime;        // Set the timer for Drying
            END_IF

        ELSIF DryStage THEN
            Dryer := TRUE;                    // Activate Dryer
            IF StageTimer <= T#0S THEN
                Dryer := FALSE;               // Stop Dryer
                DryStage := FALSE;            // End Drying stage
                WashInProgress := FALSE;      // Complete the wash process
                ConveyorMotor := FALSE;       // Stop the conveyor
            END_IF
        END_IF
    END_IF

    // Timer countdown for active stages
    IF StageTimer > T#0S THEN
        StageTimer := StageTimer - T#100MS;   // Decrease the stage timer by 100ms each cycle
    END_IF

    // Safety monitoring: Stop all operations if a human is detected
    IF HumanDetected OR EmergencyStop THEN
        // Trigger safety shutdown
        Alarm := TRUE;                        // Activate the alarm
        SafeState := TRUE;                    // Set safe state to true
        WashInProgress := FALSE;              // Stop the wash process
        ConveyorMotor := FALSE;               // Stop the conveyor
        PreWashSpray := FALSE;                // Deactivate Pre-Wash
        SoapSpray := FALSE;                   // Deactivate Soap spray
        Brushes := FALSE;                     // Deactivate Brushes
        RinseSpray := FALSE;                  // Deactivate Rinse spray
        Dryer := FALSE;                       // Deactivate Dryer
    END_IF

    // System reset to clear safe state and resume operation
    IF SystemReset THEN
        SafeState := FALSE;                   // Clear safe state
        Alarm := FALSE;                       // Reset alarm
    END_IF

    // Output signals for external devices
    (* ConveyorMotor, PreWashSpray, SoapSpray, Brushes, RinseSpray, and Dryer can be connected to the respective actuators. *)
    (* Alarm can be linked to a visual or audio alert system. *)

END_PROGRAM
```

Explanation:

	1.	Variables:
	•	Input Sensors:
	•	CarDetected: Detects the presence of a car in the wash bay.
	•	HumanDetected: Detects the presence of a human in the wash area.
	•	EmergencyStop: Emergency stop button for manual intervention.
	•	Process Stages: Boolean variables (PreWashStage, SoapStage, BrushStage, RinseStage, DryStage) indicate the current stage of the car wash.
	•	Output Controls:
	•	Control signals for the conveyor motor (ConveyorMotor), water sprays (PreWashSpray, SoapSpray, RinseSpray), brushes (Brushes), and dryer (Dryer).
	•	Alarm: Activates when a human is detected or emergency stop is pressed.
	•	Timing Variables: Timers for each wash stage (PreWashTime, SoapTime, etc.) and a StageTimer to manage transitions between stages.
	•	Status Variables:
	•	WashInProgress: Indicates whether a wash cycle is in progress.
	•	SafeState: Indicates if the system is in a safe state due to human presence or emergency.
	2.	Control Logic:
	•	The program initiates a wash cycle when a car is detected (CarDetected = TRUE) and no human is present (HumanDetected = FALSE).
	•	It moves through each stage of the wash process (Pre-Wash, Soap, Brush, Rinse, and Dry) based on the set timers.
	•	When StageTimer reaches zero, the program transitions to the next stage.
	3.	Safety Measures:
	•	If a human is detected or the emergency stop is pressed, the program immediately stops all operations, sets the system to a safe state, and triggers an alarm.
	•	The system remains in the safe state until manually reset using the SystemReset input.
	4.	Reset Functionality:
	•	The SystemReset input clears the safe state and allows the program to resume normal operation if the wash area is clear.
