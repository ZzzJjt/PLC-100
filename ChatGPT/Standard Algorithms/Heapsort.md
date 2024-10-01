Here’s an implementation of a self-contained function block in IEC 61131-3 Structured Text for performing the heapsort algorithm on an array of integers. This implementation avoids recursion and does not use the DOWNTO keyword in loops, making it compatible with PLC environments that might have such restrictions.

```
FUNCTION_BLOCK FB_Heapsort
VAR_INPUT
    UnsortedArray : ARRAY[1..100] OF INT;   // Input array to be sorted
    ArrayLength   : INT := 100;             // Length of the array to be sorted
END_VAR

VAR_OUTPUT
    SortedArray   : ARRAY[1..100] OF INT;   // Output array with sorted elements
    IsSorted      : BOOL;                   // Indicates if the array is sorted
    ValidInput    : BOOL;                   // Indicates if the input parameters are valid
END_VAR

VAR
    i, j, k       : INT;                    // Loop indices
    Parent, Child : INT;                    // Indices for heap construction
    Temp          : INT;                    // Temporary variable for swapping
END_VAR

// --- Input Validation ---
IF (ArrayLength < 1) OR (ArrayLength > 100) THEN
    ValidInput := FALSE;
    IsSorted := FALSE;
    RETURN;
ELSE
    ValidInput := TRUE;
END_IF;

// --- Copy input array to output array ---
FOR i := 1 TO ArrayLength DO
    SortedArray[i] := UnsortedArray[i];
END_FOR;

// --- Heap Construction Phase ---
i := ArrayLength / 2;
WHILE i >= 1 DO
    Parent := i;
    WHILE 2 * Parent <= ArrayLength DO
        Child := 2 * Parent;
        
        // Select the larger child
        IF (Child < ArrayLength) AND (SortedArray[Child] < SortedArray[Child + 1]) THEN
            Child := Child + 1;
        END_IF;
        
        // If parent is smaller than the largest child, swap them
        IF SortedArray[Parent] < SortedArray[Child] THEN
            Temp := SortedArray[Parent];
            SortedArray[Parent] := SortedArray[Child];
            SortedArray[Child] := Temp;
            
            // Move down the heap
            Parent := Child;
        ELSE
            EXIT;  // Break loop if the heap property is satisfied
        END_IF;
    END_WHILE;
    
    i := i - 1;  // Equivalent to DOWNTO without using DOWNTO
END_WHILE;

// --- Sorting Phase ---
FOR i := ArrayLength TO 2 BY -1 DO
    // Swap the first element (largest) with the last unsorted element
    Temp := SortedArray[1];
    SortedArray[1] := SortedArray[i];
    SortedArray[i] := Temp;
    
    // Restore the heap property for the reduced heap
    Parent := 1;
    WHILE 2 * Parent < i DO
        Child := 2 * Parent;
        
        // Select the larger child
        IF (Child < (i - 1)) AND (SortedArray[Child] < SortedArray[Child + 1]) THEN
            Child := Child + 1;
        END_IF;
        
        // If parent is smaller than the largest child, swap them
        IF SortedArray[Parent] < SortedArray[Child] THEN
            Temp := SortedArray[Parent];
            SortedArray[Parent] := SortedArray[Child];
            SortedArray[Child] := Temp;
            
            // Move down the heap
            Parent := Child;
        ELSE
            EXIT;  // Break loop if the heap property is satisfied
        END_IF;
    END_WHILE;
END_FOR;

// --- Set output signal to indicate sorting completion ---
IsSorted := TRUE;

END_FUNCTION_BLOCK
```

Key Features:

	1.	Input Parameters:
	•	UnsortedArray: The input array containing up to 100 integers to be sorted.
	•	ArrayLength: Specifies the number of elements in the input array that need to be sorted (e.g., set to 100 for sorting all elements).
	2.	Output Parameters:
	•	SortedArray: Contains the sorted elements after the heapsort operation.
	•	IsSorted: Indicates if the sorting operation is complete and successful.
	•	ValidInput: Indicates if the ArrayLength is within a valid range (1 to 100).
	3.	Heapsort Algorithm:
	•	Heap Construction:
	•	Constructs a max heap from the input array by starting from the middle of the array and adjusting the heap downwards.
	•	Avoids using DOWNTO by decrementing the loop index i manually.
	•	Sorting:
	•	The largest element (root of the heap) is repeatedly swapped with the last unsorted element, reducing the heap size by one.
	•	The heap property is restored for the reduced heap by re-heapifying from the root downwards.
	4.	Efficient Heap Operations:
	•	The function block uses index calculations to efficiently manage heap properties:
	•	Parent: Current node being checked.
	•	Child: The left child of the Parent, and the larger child is selected if a right child exists.
	•	Swaps are performed to maintain the heap property, and the loop breaks early when no further swaps are needed, reducing unnecessary operations.
	5.	Avoids DOWNTO and Recursion:
	•	The code implements heap construction and sorting using WHILE and FOR loops without DOWNTO.
	•	Manually manages loop indices to avoid DOWNTO, making it compatible with stricter programming environments.
	6.	Edge Case Handling:
	•	If ArrayLength is out of bounds (<1 or >100), the function block sets ValidInput to FALSE and exits early.
	•	This prevents unnecessary operations on invalid inputs.

Usage Example:

To use this function block, configure the input parameters as follows:
```
VAR
    InputArray   : ARRAY[1..100] OF INT := [33, 12, 78, 42, 56, 9, 23, 17, 91, 47];  // Example unsorted array
    OutputArray  : ARRAY[1..100] OF INT;  // Array to hold the sorted values
    Sorted       : BOOL;                  // To indicate if sorting is completed
    InputValid   : BOOL;                  // To indicate if the input is valid
END_VAR

// Example usage
FB_Heapsort(UnsortedArray := InputArray, 
            ArrayLength := 10, 
            SortedArray => OutputArray, 
            IsSorted => Sorted, 
            ValidInput => InputValid);
```

Important Considerations:

	•	Ensure that the input array size does not exceed 100 elements, as the function block is designed to handle a fixed array size.
	•	If the array is smaller than 100 elements, specify ArrayLength accordingly to avoid unnecessary operations.
