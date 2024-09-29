The following structured text code outlines a function block that registers or deletes a Process Data Object (PDO) or CAN Layer 2 message for reception by the CAN network layer based on a specified CAN Object Identifier (COBID). It handles registration, deletion, and clearing of messages in the network layer’s buffer based on the value of the REGISTER input.

```
FUNCTION_BLOCK CAN_REGISTER_COBID
VAR
    (* CAN Communication Variables *)
    registeredCOBID : ARRAY[1..100] OF DWORD; (* Array to store registered COBIDs *)
    messageBuffer : ARRAY[1..100, 1..8] OF BYTE; (* 2D Array to store messages per COBID *)
    currentCOBID : DWORD; (* Current COBID to register or delete *)
    registerIndex : INT; (* Index for registered COBID array *)
    foundIndex : INT; (* Index where the COBID is found *)
    i : INT; (* Loop index *)

    (* Control Variables *)
    isRegistered : BOOL; (* Status of registration *)
    bufferCleared : BOOL; (* Status of buffer clearing *)
    cobidFound : BOOL; (* TRUE if COBID found in registered list *)
    errorFlag : BOOL; (* Error status flag *)
END_VAR

VAR_INPUT
    REGISTER : BOOL; (* Input to register or delete a PDO or CAN message *)
    COBID : DWORD; (* CAN identifier for the PDO or Layer 2 message *)
END_VAR

VAR_OUTPUT
    operationStatus : STRING; (* Status of the registration operation *)
    errorStatus : BOOL; (* TRUE if an error occurred during operation *)
END_VAR

(* Step 1: Validate COBID Input *)
IF COBID < 0 THEN
    operationStatus := 'Invalid COBID';
    errorStatus := TRUE;
    RETURN;
END_IF

(* Step 2: Check REGISTER Input and Perform Operation *)
IF REGISTER THEN
    (* Registration Process *)
    cobidFound := FALSE;
    FOR i := 1 TO 100 DO
        IF registeredCOBID[i] = COBID THEN
            cobidFound := TRUE; (* COBID is already registered *)
            EXIT;
        END_IF
    END_FOR

    IF NOT cobidFound THEN
        (* Find first empty slot for new registration *)
        FOR i := 1 TO 100 DO
            IF registeredCOBID[i] = 0 THEN
                registeredCOBID[i] := COBID;
                isRegistered := TRUE;
                operationStatus := CONCAT('COBID Registered: ', DWORD_TO_STRING(COBID));
                EXIT;
            END_IF
        END_FOR

        IF NOT isRegistered THEN
            operationStatus := 'Registration Failed: No Empty Slot';
            errorStatus := TRUE;
        END_IF
    ELSE
        operationStatus := CONCAT('COBID Already Registered: ', DWORD_TO_STRING(COBID));
    END_IF

ELSE
    (* De-registration Process *)
    IF COBID = 0 THEN
        (* Clear All Registrations and Buffers *)
        FOR i := 1 TO 100 DO
            registeredCOBID[i] := 0;
            FILL(messageBuffer[i], 0); (* Clear each message buffer *)
        END_FOR
        bufferCleared := TRUE;
        operationStatus := 'All Registrations Cleared';
    ELSE
        (* Delete Specific COBID Registration *)
        cobidFound := FALSE;
        FOR i := 1 TO 100 DO
            IF registeredCOBID[i] = COBID THEN
                registeredCOBID[i] := 0;
                FILL(messageBuffer[i], 0); (* Clear the buffer for this COBID *)
                cobidFound := TRUE;
                operationStatus := CONCAT('COBID Deleted: ', DWORD_TO_STRING(COBID));
                EXIT;
            END_IF
        END_FOR

        IF NOT cobidFound THEN
            operationStatus := CONCAT('COBID Not Found: ', DWORD_TO_STRING(COBID));
            errorStatus := TRUE;
        END_IF
    END_IF
END_IF

(* Step 3: Error Handling *)
IF errorStatus THEN
    operationStatus := CONCAT(operationStatus, ' | Error Occurred');
ELSE
    errorStatus := FALSE;
END_IF
```

**Implementation Details**

	1.	COBID Validation:
	•	The function block first validates the input COBID. If the COBID is less than zero, it sets the operationStatus to “Invalid COBID” and the errorStatus to TRUE. This ensures that the function block only processes valid CAN identifiers.
	2.	Registration Process:
	•	When REGISTER is set to TRUE, the function block attempts to register the specified COBID.
	•	It first checks if the COBID is already registered in the registeredCOBID array.
	•	If not, it searches for the first empty slot (indicated by a 0 value) and stores the new COBID.
	•	If an empty slot is found, the operation is successful, and operationStatus is updated. If no empty slots are available, the function sets errorStatus and indicates the failure.
	3.	De-registration Process:
	•	If REGISTER is set to FALSE, the function block checks the value of COBID.
	•	If COBID = 0, it clears all entries in the registeredCOBID array and resets the messageBuffer for each entry. The operationStatus is set to “All Registrations Cleared,” and bufferCleared is set to TRUE.
	•	If COBID is non-zero, the function block searches for the COBID in the array and removes it if found, clearing the associated message buffer.
	4.	Buffer Clearing Mechanism:
	•	The FILL function is used to reset each message buffer. It sets all bytes in the corresponding message array to 0 to ensure no stale data remains after de-registration or clearing of all COBIDs.
	5.	Error Handling and Status Reporting:
	•	The function block provides detailed status reporting for each operation using the operationStatus output string.
	•	If an error occurs during registration or de-registration, the errorStatus flag is set to TRUE, and the operationStatus string is appended with an error message.


**Example Scenarios**

	1.	Registering a New PDO or CAN Message:
	•	Input: REGISTER = TRUE, COBID = 1234
	•	Output: operationStatus = "COBID Registered: 1234"
	2.	Deleting a Specific PDO:
	•	Input: REGISTER = FALSE, COBID = 1234
	•	Output: operationStatus = "COBID Deleted: 1234"
	3.	Clearing All Registrations and Buffers:
	•	Input: REGISTER = FALSE, COBID = 0
	•	Output: operationStatus = "All Registrations Cleared"
	4.	Handling an Invalid COBID:
	•	Input: REGISTER = TRUE, COBID = -1
	•	Output: operationStatus = "Invalid COBID"


