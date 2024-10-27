1. Control Flow Keywords

Control flow keywords are used to define the logic and execution flow in Structured Text programs.

	•	IF, THEN, ELSE, ELSIF, END_IF
	•	Used for conditional branching.
	•	Example:

```
IF temperature > 100.0 THEN
    fan := TRUE;
ELSIF temperature > 80.0 THEN
    fan := FALSE;
ELSE
    heater := TRUE;
END_IF;
```

	•	CASE, OF, END_CASE
	•	Used for multi-way branching based on an integer or enumerated value.
	•	Example:
```
CASE state OF
    0: startMotor := TRUE;
    1: stopMotor := TRUE;
    2: alarm := TRUE;
ELSE
    reset := TRUE;
END_CASE;
```

FOR, TO, BY, DO, END_FOR
	•	Looping construct to iterate over a range of values.
	•	Example:
```
FOR i := 1 TO 10 DO
    sum := sum + i;
END_FOR;
```
	•	WHILE, DO, END_WHILE
	•	Looping construct that executes as long as the condition is true.
	•	Example:
```
WHILE counter < 100 DO
    counter := counter + 1;
END_WHILE;
```
	•	REPEAT, UNTIL, END_REPEAT
	•	Executes the loop body at least once and repeats until the condition is true.
	•	Example:
```
REPEAT
    value := value * 2;
UNTIL value > 100
END_REPEAT;
```
EXIT
	•	Exits from the innermost loop.
	•	Example:
```
FOR i := 1 TO 10 DO
    IF sensorError THEN
        EXIT; // Exit the loop if an error is detected
    END_IF;
END_FOR;
```
RETURN
	•	Exits a function or method and returns control to the caller.
	•	Example:

```
FUNCTION CalculateSum: INT
VAR_INPUT
    a: INT;
    b: INT;
END_VAR
CalculateSum := a + b;
RETURN;
END_FUNCTION
```

2. Data Type Keywords

Data type keywords define the types of variables used in the program.


Elementary Data Types

	•	BOOL: Boolean value (TRUE or FALSE).
	•	INT: 16-bit signed integer.
	•	DINT: 32-bit signed integer.
	•	REAL: 32-bit floating point.
	•	LREAL: 64-bit floating point.
	•	STRING: String of characters.
	•	TIME: Represents time values and intervals.
	•	DATE: Represents calendar date values.
	•	TIME_OF_DAY: Time without date component.
	•	DATE_AND_TIME: Combines both date and time.
 
```
VAR
    sensorActive: BOOL;           // Boolean variable
    counter: INT := 0;            // Integer variable with initial value
    temperature: REAL := 25.5;    // Real (floating point) variable
    message: STRING := 'Hello';   // String variable
    duration: TIME := T#5s;       // Time variable for 5 seconds
END_VAR
```
Structured Data Types

	•	ARRAY
	•	Array of elements.
	•	Example:
```
VAR
    temperatureArray: ARRAY[1..10] OF REAL;  // Array of 10 REAL values
END_VAR
```
