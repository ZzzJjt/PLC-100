Here’s an implementation of a self-contained function block in IEC 61131-3 Structured Text for performing the quicksort algorithm on an array of integers. This function block includes efficient partitioning and recursive handling using an internal stack-based approach, as IEC 61131-3 Structured Text does not directly support recursive function calls.

```
FUNCTION_BLOCK FB_Quicksort
VAR_INPUT
    UnsortedArray : ARRAY[1..100] OF INT;   // Input array to be sorted
    StartIndex    : INT := 1;               // Starting index of the array (1-based index)
    EndIndex      : INT := 100;             // Ending index of the array (1-based index)
END_VAR

VAR_OUTPUT
    SortedArray   : ARRAY[1..100] OF INT;   // Output array with sorted elements
    IsSorted      : BOOL;                  // Indicates if the array is sorted
    ValidInput    : BOOL;                  // Indicates if the input parameters are valid
END_VAR

VAR
    Stack : ARRAY[1..200] OF INT;    // Stack for storing start and end indices for sub-arrays
    Top   : INT := 0;                // Top of the stack
    Left  : INT;                     // Left index for partitioning
    Right : INT;                     // Right index for partitioning
    Pivot : INT;                     // Pivot element for partitioning
    Temp  : INT;                     // Temporary variable for swapping
    i, j  : INT;                     // Loop indices for partitioning
END_VAR

// --- Input Validation ---
IF (StartIndex < 1) OR (EndIndex > 100) OR (StartIndex >= EndIndex) THEN
    ValidInput := FALSE;
    IsSorted := FALSE;
    RETURN;
ELSE
    ValidInput := TRUE;
END_IF;

// --- Copy input array to output array ---
FOR i := 1 TO 100 DO
    SortedArray[i] := UnsortedArray[i];
END_FOR;

// --- Initialize stack with initial indices ---
Top := 0;
Top := Top + 1;  // Push StartIndex onto stack
Stack[Top] := StartIndex;

Top := Top + 1;  // Push EndIndex onto stack
Stack[Top] := EndIndex;

// --- Iterative QuickSort using a stack ---
WHILE Top > 0 DO
    // Pop EndIndex and StartIndex
    EndIndex := Stack[Top];
    Top := Top - 1;

    StartIndex := Stack[Top];
    Top := Top - 1;

    // Set the initial left and right indices
    Left := StartIndex;
    Right := EndIndex;

    // Select pivot as the middle element
    Pivot := SortedArray[(StartIndex + EndIndex) / 2];

    // Partitioning the array
    WHILE Left <= Right DO
        // Move left index until finding an element greater than or equal to the pivot
        WHILE SortedArray[Left] < Pivot DO
            Left := Left + 1;
        END_WHILE;

        // Move right index until finding an element less than or equal to the pivot
        WHILE SortedArray[Right] > Pivot DO
            Right := Right - 1;
        END_WHILE;

        // Swap elements at Left and Right indices if Left <= Right
        IF Left <= Right THEN
            Temp := SortedArray[Left];
            SortedArray[Left] := SortedArray[Right];
            SortedArray[Right] := Temp;

            // Move indices inward
            Left := Left + 1;
            Right := Right - 1;
        END_IF;
    END_WHILE;

    // Push the left and right sub-arrays onto the stack if needed
    IF StartIndex < Right THEN
        Top := Top + 1;
        Stack[Top] := StartIndex;  // Push left sub-array start index
        Top := Top + 1;
        Stack[Top] := Right;       // Push left sub-array end index
    END_IF;

    IF Left < EndIndex THEN
        Top := Top + 1;
        Stack[Top] := Left;        // Push right sub-array start index
        Top := Top + 1;
        Stack[Top] := EndIndex;    // Push right sub-array end index
    END_IF;
END_WHILE;

// --- Set output signal to indicate sorting completion ---
IsSorted := TRUE;

END_FUNCTION_BLOCK
```

Key Features:

	1.	Input Parameters:
	•	UnsortedArray: The input array containing up to 100 integers to be sorted.
	•	StartIndex and EndIndex: Define the sub-array range to be sorted. By default, these should be set to 1 and 100 if sorting the entire array.
	2.	Output Parameters:
	•	SortedArray: Contains the sorted elements after the quicksort operation.
	•	IsSorted: Indicates if the sorting operation is complete and successful.
	•	ValidInput: Indicates if the input indices are within a valid range (1 to 100).
	3.	Iterative Quicksort Implementation:
	•	Instead of using recursion (which is not directly supported in IEC 61131-3 Structured Text), the function block uses a stack-based iterative approach to handle the quicksort partitions.
	•	The stack (Stack array) stores the start and end indices of sub-arrays that need to be sorted.
	•	The loop continues until the stack is empty, meaning all partitions are sorted.
	4.	Partitioning Logic:
	•	The partitioning is performed by selecting the pivot as the middle element of the sub-array.
	•	The elements are rearranged so that those smaller than the pivot are on the left and those greater are on the right.
	•	If Left is less than or equal to Right, the elements are swapped, and the indices are moved inward.
	5.	Efficient Handling of Sub-arrays:
	•	After partitioning, the stack is updated with indices for left and right sub-arrays if they exist (i.e., StartIndex < Right and Left < EndIndex).
	6.	Edge Case Handling:
	•	The function block performs validation to ensure StartIndex and EndIndex are within valid bounds (1 to 100) and that StartIndex is less than EndIndex.
	•	If the validation fails, the function block sets IsSorted to FALSE and exits early.

Usage Example:

To use this function block, configure the input parameters as follows:
```
VAR
    InputArray   : ARRAY[1..100] OF INT := [100, 90, 80, ..., 10, 1];  // An example unsorted array
    OutputArray  : ARRAY[1..100] OF INT;  // Array to hold the sorted values
    Sorted       : BOOL;                  // To indicate if sorting is completed
    InputValid   : BOOL;                  // To indicate if the input is valid
END_VAR

// Example usage
FB_Quicksort(UnsortedArray := InputArray, 
             StartIndex := 1, 
             EndIndex := 100, 
             SortedArray => OutputArray, 
             IsSorted => Sorted, 
             ValidInput => InputValid);
```
Important Considerations:

	•	The input array should contain elements within the supported range of the INT data type to avoid overflow or underflow.
	•	Ensure the array is appropriately sized (100 elements), as hardcoded indices are used for simplicity.
 
