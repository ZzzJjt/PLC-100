Here is a self-contained 61131-3 Structured Text (ST) program for controlling a coffee machine. The program manages three tanks (coffee, milk, and mixer) and three valves to properly mix and dispense coffee. The program implements various control buttons and includes safety features using an emergency stop.

```
PROGRAM CoffeeMakerControl
    // Variable declarations for inputs, outputs, and control logic
    VAR
        // Control buttons
        EmergencyStopButton: BOOL := FALSE;         // Button 1: Emergency Stop
        StartButton: BOOL := FALSE;                 // Button 2: Start coffee-making process
        CoffeeMilkButton: BOOL := FALSE;            // Button 3: Prepare coffee with milk
        CoffeeOnlyButton: BOOL := FALSE;            // Button 4: Prepare coffee without milk

        // Output control signals for valves and mixer
        CoffeeValve: BOOL := FALSE;                 // Controls the coffee valve
        MilkValve: BOOL := FALSE;                   // Controls the milk valve
        OutputValve: BOOL := FALSE;                 // Controls the output valve
        MixerMotor: BOOL := FALSE;                  // Controls the mixer motor

        // Tank level variables
        MixerTankLevel: REAL := 0.0;                // Current level of the mixer tank (in ml)
        MaxTankLevel: REAL := 130.0;                // Maximum capacity of the mixer tank (in ml)

        // Timing variables for the mixing process
        MixingTime: TIME := T#4S;                   // Time for mixing (4 seconds)
        MixingTimer: TIME := T#0S;                  // Timer to track mixing duration

        // Control flags for process stages
        FillingComplete: BOOL := FALSE;             // Indicates that the filling process is complete
        MixingComplete: BOOL := FALSE;              // Indicates that the mixing process is complete
        DispenseComplete: BOOL := FALSE;            // Indicates that the coffee has been dispensed
        SystemRunning: BOOL := FALSE;               // Indicates that the system is in operation

        // Safety flags
        EmergencyStopActive: BOOL := FALSE;         // Indicates that the emergency stop is active
    END_VAR

    // ---------------------- Safety: Emergency Stop Logic ----------------------
    IF EmergencyStopButton THEN
        // Trigger emergency stop: Stop all operations immediately
        CoffeeValve := FALSE;
        MilkValve := FALSE;
        OutputValve := FALSE;
        MixerMotor := FALSE;
        SystemRunning := FALSE;                     // Stop the system
        EmergencyStopActive := TRUE;                // Set emergency stop active flag
    END_IF

    // ---------------------- System Start Logic ----------------------
    IF StartButton AND NOT EmergencyStopActive THEN
        SystemRunning := TRUE;                      // Start the system if Emergency Stop is not active
        FillingComplete := FALSE;                   // Reset process flags
        MixingComplete := FALSE;
        DispenseComplete := FALSE;
    END_IF

    // ---------------------- Coffee Making Process Logic ----------------------
    IF SystemRunning AND NOT EmergencyStopActive THEN
        // ---------------------- 1. Filling Stage ----------------------
        IF NOT FillingComplete THEN
            // Handle different modes: Coffee with milk or coffee only
            IF CoffeeMilkButton THEN
                CoffeeValve := TRUE;                // Open coffee valve
                MilkValve := TRUE;                  // Open milk valve
            ELSIF CoffeeOnlyButton THEN
                CoffeeValve := TRUE;                // Open only coffee valve
                MilkValve := FALSE;                 // Ensure milk valve is closed
            END_IF

            // Simulate tank filling by incrementing the mixer tank level
            IF CoffeeValve OR MilkValve THEN
                MixerTankLevel := MixerTankLevel + 5.0; // Increment by 5 ml per scan cycle (simulation)
            END_IF

            // Check if the mixer tank is full
            IF MixerTankLevel >= MaxTankLevel THEN
                CoffeeValve := FALSE;               // Close coffee valve
                MilkValve := FALSE;                 // Close milk valve
                FillingComplete := TRUE;            // Mark filling as complete
                MixingTimer := MixingTime;          // Start the mixing timer
            END_IF
        END_IF

        // ---------------------- 2. Mixing Stage ----------------------
        IF FillingComplete AND NOT MixingComplete THEN
            MixerMotor := TRUE;                     // Start the mixer motor
            IF MixingTimer > T#0S THEN
                MixingTimer := MixingTimer - T#100MS; // Decrease the timer every scan cycle (100 ms decrement)
            ELSE
                MixingComplete := TRUE;             // Mark mixing as complete when the timer reaches 0
                MixerMotor := FALSE;                // Stop the mixer motor
            END_IF
        END_IF

        // ---------------------- 3. Dispensing Stage ----------------------
        IF MixingComplete AND NOT DispenseComplete THEN
            OutputValve := TRUE;                    // Open the output valve to dispense coffee
            IF MixerTankLevel > 0.0 THEN
                MixerTankLevel := MixerTankLevel - 5.0; // Dispense 5 ml per scan cycle (simulation)
            ELSE
                OutputValve := FALSE;               // Close the output valve when the tank is empty
                DispenseComplete := TRUE;           // Mark dispense as complete
                SystemRunning := FALSE;             // Stop the system after dispense is complete
            END_IF
        END_IF
    END_IF

    // ---------------------- Reset Logic ----------------------
    IF NOT StartButton AND NOT EmergencyStopButton THEN
        // Reset system to initial state
        SystemRunning := FALSE;                     // Ensure system is not running
        CoffeeValve := FALSE;
        MilkValve := FALSE;
        OutputValve := FALSE;
        MixerMotor := FALSE;
        MixerTankLevel := 0.0;                      // Reset tank level
        FillingComplete := FALSE;
        MixingComplete := FALSE;
        DispenseComplete := FALSE;
        EmergencyStopActive := FALSE;               // Clear emergency stop flag
    END_IF

    // ---------------------- Output Mapping ----------------------
    // CoffeeValve, MilkValve, OutputValve, and MixerMotor control the respective actuators
    // Use these signals to connect to the physical outputs for controlling the valves and motor

END_PROGRAM
```

Explanation:

	1.	Input Variables:
	•	EmergencyStopButton: Emergency stop button (Button 1).
	•	StartButton: Button to start the coffee-making process (Button 2).
	•	CoffeeMilkButton: Button to prepare coffee with milk (Button 3).
	•	CoffeeOnlyButton: Button to prepare coffee without milk (Button 4).
	2.	Output Variables:
	•	CoffeeValve: Controls the coffee valve.
	•	MilkValve: Controls the milk valve.
	•	OutputValve: Controls the output valve for dispensing coffee.
	•	MixerMotor: Controls the mixer motor.
	3.	Process Stage Flags:
	•	FillingComplete: Set when the mixer tank reaches the maximum level (130 ml).
	•	MixingComplete: Set after mixing is finished (4 seconds).
	•	DispenseComplete: Set after the coffee has been dispensed.
	•	SystemRunning: Set when the coffee-making process is active.
	4.	Safety Logic:
	•	The EmergencyStopButton stops all operations immediately by setting all output variables (CoffeeValve, MilkValve, OutputValve, MixerMotor) to FALSE and deactivating the system.
	5.	Process Logic:
	•	The program begins by filling the mixer tank based on the selected mode (CoffeeMilkButton or CoffeeOnlyButton).
	•	When the mixer tank reaches the maximum level (MaxTankLevel), the filling stage ends, and the mixing stage starts (MixerMotor = TRUE).
	•	After the 4-second mixing time (MixingTime), the mixing stage ends, and the dispensing stage begins.
	•	The dispensing stage continues until the mixer tank is empty (MixerTankLevel = 0.0), at which point the process completes.
	6.	Reset Logic:
	•	When neither StartButton nor EmergencyStopButton is active, the system returns to its initial state, resetting all flags and outputs.
