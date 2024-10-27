Here’s a self-contained IEC 61131-3 function block for calculating both the mean and standard deviation of an array of 100 integers. This function block is designed to be modular, with detailed comments explaining each step of the process.

```
FUNCTION_BLOCK FB_MeanAndStdDev
    (* Input array and output statistical measures *)
    VAR_INPUT
        DataArray: ARRAY[1..100] OF INT; (* Input array of 100 integers *)
    END_VAR

    VAR_OUTPUT
        Mean: REAL;           (* Output: Mean of the input array *)
        StdDev: REAL;         (* Output: Standard deviation of the input array *)
        Error: BOOL;          (* Error flag to indicate overflow or invalid inputs *)
    END_VAR

    VAR
        Sum: DINT;            (* Sum of array elements *)
        SumOfSquares: DINT;   (* Sum of squared differences from the mean *)
        i: INT;               (* Loop counter *)
        MeanTemp: REAL;       (* Temporary mean value for calculations *)
        Deviation: REAL;      (* Deviation of each element from the mean *)
        ArrayElement: REAL;   (* Casted array element to REAL for precision *)
    END_VAR

(* Initialization *)
    Sum := 0;                (* Initialize sum to 0 *)
    SumOfSquares := 0;       (* Initialize sum of squares to 0 *)
    Error := FALSE;          (* Reset error flag *)

(* Step 1: Calculate the Mean *)
    FOR i := 1 TO 100 DO
        Sum := Sum + DataArray[i]; (* Accumulate the sum of all array elements *)
        IF Sum > 2147483647 OR Sum < -2147483647 THEN
            Error := TRUE; (* Set error flag if overflow is detected *)
            EXIT;          (* Exit loop in case of overflow *)
        END_IF;
    END_FOR;

    IF NOT Error THEN
        MeanTemp := REAL(Sum) / 100.0; (* Calculate mean as Sum / 100 *)
        Mean := MeanTemp;              (* Assign the mean to the output variable *)
    END_IF;

(* Step 2: Calculate the Standard Deviation *)
    IF NOT Error THEN
        FOR i := 1 TO 100 DO
            ArrayElement := REAL(DataArray[i]);             (* Cast the integer to REAL for precision *)
            Deviation := ArrayElement - MeanTemp;           (* Compute deviation from the mean *)
            SumOfSquares := SumOfSquares + DINT(Deviation * Deviation); (* Accumulate square of the deviation *)

            IF SumOfSquares > 2147483647 THEN
                Error := TRUE; (* Set error flag if overflow is detected *)
                EXIT;          (* Exit loop in case of overflow *)
            END_IF;
        END_FOR;

        IF NOT Error THEN
            StdDev := SQRT(REAL(SumOfSquares) / 100.0); (* Calculate standard deviation: sqrt(SumOfSquares / 100) *)
        END_IF;
    END_IF;

END_FUNCTION_BLOCK
```

Explanation:

	1.	Input Variable:
	•	DataArray: An array of 100 integers for which the mean and standard deviation are to be computed.
	2.	Output Variables:
	•	Mean: Stores the calculated mean of the input array.
	•	StdDev: Stores the calculated standard deviation of the input array.
	•	Error: A boolean flag indicating overflow or invalid input conditions.
	3.	Local Variables:
	•	Sum: A DINT variable to accumulate the sum of the array elements.
	•	SumOfSquares: A DINT variable to accumulate the sum of squared deviations from the mean.
	•	i: Loop counter used to iterate over the array elements.
	•	MeanTemp: Temporary REAL variable to hold the mean value for use in standard deviation calculation.
	•	Deviation: Stores the deviation of each array element from the mean.
	•	ArrayElement: Casts each array element to REAL for precision during calculations.
	4.	Step-by-Step Implementation:
	•	Mean Calculation:
	•	Iterate through the array elements and sum them up (Sum).
	•	Convert the sum to REAL and divide by 100 to compute the mean (Mean).
	•	Standard Deviation Calculation:
	•	Iterate through the array again, calculating the deviation of each element from the mean.
	•	Accumulate the square of each deviation into SumOfSquares.
	•	Compute the standard deviation using the formula:
 	5.	Error Handling:
	•	If overflow is detected during the summation or square accumulation (Sum or SumOfSquares), the Error flag is set, and the computation exits early.
	•	The maximum range for a DINT is ±2,147,483,647. If the sum of array elements or sum of squares exceeds this range, an overflow occurs.
