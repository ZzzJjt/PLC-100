Here’s a self-contained function block in IEC 61131-3 Structured Text for performing a binary search on an array of 100 integers. The function block includes input validation, efficient handling of search boundaries, and returns the index of the found element or an indicator if the element is not present.

```
FUNCTION_BLOCK FB_BinarySearch
VAR_INPUT
    SearchValue : INT;             // The value to search for
    Array       : ARRAY[1..100] OF INT;  // Input array of 100 integers (assumed to be sorted)
    StartIndex  : INT;             // Start index of the array to search in (1-based)
    EndIndex    : INT;             // End index of the array to search in (1-based)
END_VAR

VAR_OUTPUT
    FoundIndex  : INT;             // Index of the found value (1-based), 0 if not found
    Found       : BOOL;            // TRUE if the value is found, FALSE otherwise
    ValidInput  : BOOL;            // Indicates if the input parameters are valid
END_VAR

VAR
    MidIndex    : INT;             // Midpoint index for binary search
    Low         : INT;             // Lower boundary for search
    High        : INT;             // Upper boundary for search
END_VAR

// Input validation
IF (StartIndex >= 1) AND (EndIndex <= 100) AND (StartIndex <= EndIndex) THEN
    ValidInput := TRUE;
ELSE
    ValidInput := FALSE;
    Found := FALSE;
    FoundIndex := 0;  // Set to 0 to indicate not found
    RETURN;
END_IF;

// Binary Search Algorithm
Low := StartIndex;
High := EndIndex;
Found := FALSE;       // Initially, set Found to FALSE

WHILE (Low <= High) AND (NOT Found) DO
    // Calculate midpoint
    MidIndex := (Low + High) / 2;
    
    IF Array[MidIndex] = SearchValue THEN
        // Value found
        Found := TRUE;
        FoundIndex := MidIndex;
    ELSIF Array[MidIndex] < SearchValue THEN
        // Search in the right half
        Low := MidIndex + 1;
    ELSE
        // Search in the left half
        High := MidIndex - 1;
    END_IF;
END_WHILE;

// If not found, set FoundIndex to 0
IF NOT Found THEN
    FoundIndex := 0;  // Set to 0 to indicate not found
END_IF;

END_FUNCTION_BLOCK
```

Key Features:

	1.	Input Parameters:
	•	SearchValue: The value to be searched in the array.
	•	Array: An array of 100 integers, which must be sorted in ascending order before performing the binary search.
	•	StartIndex and EndIndex: Define the search boundaries within the array (1-based index). By default, they should be set to 1 and 100, respectively, if searching the entire array.
	2.	Output Parameters:
	•	FoundIndex: The index of the found value (1-based index). Returns 0 if the value is not found.
	•	Found: TRUE if the value is found, FALSE otherwise.
	•	ValidInput: Indicates if the input parameters (StartIndex and EndIndex) are within valid bounds.
	3.	Binary Search Algorithm:
	•	The function block uses a WHILE loop to implement the binary search algorithm. It repeatedly divides the search range by calculating the midpoint (MidIndex) until the value is found or the search range is exhausted.
	•	Depending on the value at the MidIndex, it narrows the search to the left or right half of the array.
	4.	Efficient Search Boundaries Handling:
	•	Low and High are used to keep track of the current search boundaries. Adjustments are made based on the comparison with SearchValue.
	•	If Array[MidIndex] < SearchValue, the search range is updated to the right half (Low := MidIndex + 1).
	•	If Array[MidIndex] > SearchValue, the search range is updated to the left half (High := MidIndex - 1).
	5.	Edge Case Handling:
	•	Input validation checks if StartIndex and EndIndex are within the valid range of 1 to 100 and if StartIndex is less than or equal to EndIndex.
	•	If the input is invalid, the function sets FoundIndex to 0 and ValidInput to FALSE, and exits early.

Usage Example:

To use this function block, configure the input parameters as follows:

```
VAR
    MyArray      : ARRAY[1..100] OF INT := [1, 2, 3, 4, ..., 100];  // Presorted array
    SearchValue  : INT := 45;         // Value to find in the array
    Index        : INT;               // To capture the found index
    IsFound      : BOOL;              // To indicate if the value is found
    IsValid      : BOOL;              // To indicate if the inputs are valid
END_VAR

// Example usage
FB_BinarySearch(SearchValue := SearchValue, 
                Array := MyArray, 
                StartIndex := 1, 
                EndIndex := 100, 
                FoundIndex => Index, 
                Found => IsFound, 
                ValidInput => IsValid);
```

Important Note:

The array must be sorted in ascending order for the binary search to work correctly. If the array is not sorted, the function block will not provide accurate results.
