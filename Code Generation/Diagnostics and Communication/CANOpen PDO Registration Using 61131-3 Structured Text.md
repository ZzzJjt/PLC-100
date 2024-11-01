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
