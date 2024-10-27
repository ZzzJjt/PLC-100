Here’s an implementation of a self-contained function block for comparing two real numbers up to n decimal places in IEC 61131-3 Structured Text. This function block includes configurable precision, input validation, and error handling.

```
FUNCTION_BLOCK FB_RealComparator
VAR_INPUT
    Real1     : REAL;   // First real number input
    Real2     : REAL;   // Second real number input
    Precision : INT;    // Number of decimal places for comparison
END_VAR

VAR_OUTPUT
    IsEqual   : BOOL;   // TRUE if Real1 and Real2 are equal up to specified decimal places
    ValidInput: BOOL;   // Indicates if the inputs are valid
END_VAR

VAR
    Factor    : REAL;   // Multiplication factor based on Precision
    Temp1     : REAL;   // Temporary variable for rounded Real1
    Temp2     : REAL;   // Temporary variable for rounded Real2
END_VAR

// Input validation
IF (Precision >= 0) AND (Precision <= 10) THEN
    ValidInput := TRUE;

    // Calculate multiplication factor based on precision (10^Precision)
    Factor := POWER(10.0, REAL(Precision));

    // Round both inputs to the specified precision
    Temp1 := REAL_TO_INT(Real1 * Factor) / Factor;
    Temp2 := REAL_TO_INT(Real2 * Factor) / Factor;

    // Compare the rounded values
    IF Temp1 = Temp2 THEN
        IsEqual := TRUE;
    ELSE
        IsEqual := FALSE;
    END_IF;
ELSE
    // Invalid precision input
    ValidInput := FALSE;
    IsEqual := FALSE;
END_IF;

END_FUNCTION_BLOCK
```

Key Features:

	1.	Configurable Precision:
	•	Precision: Specifies the number of decimal places for the comparison, ranging from 0 to 10.
	•	The function uses this value to calculate a multiplication factor (e.g., for 2 decimal places, it multiplies by 100) and then rounds the inputs accordingly.
	2.	Comparison Logic:
	•	Real1 and Real2 are rounded to the specified precision by converting them to an integer format temporarily and then back to real numbers.
	•	After rounding, the two values are compared for equality.
	3.	Input Validation:
	•	The block validates that the Precision input is within an acceptable range (0 to 10). If it is outside this range, ValidInput is set to FALSE, and the comparison is not performed.
	4.	Output Signals:
	•	IsEqual: Indicates if Real1 and Real2 are equal up to the specified number of decimal places.
	•	ValidInput: Indicates if the Precision value is valid.

This function block ensures precision control and robust handling of floating-point comparison issues, making it suitable for scenarios where accurate comparisons are critical.
