Here’s an implementation of a self-contained function block for a digital counter in IEC 61131-3 Structured Text. The counter supports both up and down counting modes, and includes configurable initial value, step size, and overflow handling.

```
FUNCTION_BLOCK FB_Counter
VAR_INPUT
    Enable    : BOOL;    // Enable signal for the counter
    Mode      : BOOL;    // Mode selection: TRUE = Up counting, FALSE = Down counting
    StepSize  : INT;     // Step size for increment/decrement
    Reset     : BOOL;    // Reset signal to set counter back to InitialValue
END_VAR

VAR_OUTPUT
    Count     : INT;     // Current count value
    Overflow  : BOOL;    // Overflow indicator
END_VAR

VAR
    InitialValue : INT := 0;  // Configurable initial value of the counter
    MaxValue     : INT := 32767;  // Maximum counter value for overflow detection
    MinValue     : INT := -32768; // Minimum counter value for overflow detection
END_VAR

VAR_TEMP
    PreviousEnable : BOOL;    // Stores the previous state of Enable
END_VAR

// Counter logic
IF Reset THEN
    // Reset counter to the initial value
    Count := InitialValue;
    Overflow := FALSE;

ELSIF Enable AND NOT PreviousEnable THEN
    // If Enable rises (false to true), update count based on mode
    IF Mode THEN
        // Up counting mode
        IF Count + StepSize > MaxValue THEN
            Count := MinValue; // Wrap around to the minimum value if overflow occurs
            Overflow := TRUE;
        ELSE
            Count := Count + StepSize;
            Overflow := FALSE;
        END_IF;
    ELSE
        // Down counting mode
        IF Count - StepSize < MinValue THEN
            Count := MaxValue; // Wrap around to the maximum value if underflow occurs
            Overflow := TRUE;
        ELSE
            Count := Count - StepSize;
            Overflow := FALSE;
        END_IF;
    END_IF;
END_IF;

// Store the current state of Enable
PreviousEnable := Enable;

END_FUNCTION_BLOCK
```

Key Features:

	1.	Configurable Parameters:
	•	InitialValue: The starting value of the counter, can be configured.
	•	StepSize: Configurable step size for both up and down counting.
	2.	Modes:
	•	Mode: Determines the counting direction.
	•	TRUE = Up counting.
	•	FALSE = Down counting.
	3.	Overflow Handling:
	•	The counter wraps around to the opposite extreme when an overflow or underflow condition occurs.
	4.	Reset:
	•	The counter can be reset to its initial value using the Reset signal.

 This function block is designed to be flexible and easily adapted for various counter applications.
