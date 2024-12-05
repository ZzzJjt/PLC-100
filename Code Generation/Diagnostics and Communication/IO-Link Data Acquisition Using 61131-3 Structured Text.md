```
FUNCTION_BLOCK FB_IOLinkDataAcquisition
VAR
    (* IO-Link Communication Variables *)
    commRequest : BOOL; (* Trigger for read request *)
    commStatus : INT; (* Communication status *)
    masterAddress : INT; (* IO-Link master address *)

    (* Process Data Variables *)
    processData : ARRAY[1..5] OF REAL; (* Array to store the 5 process values *)
    processDataRaw : ARRAY[1..5] OF BYTE; (* Raw byte data read from the master *)

    (* Status Variables *)
    statusFlags : ARRAY[1..5] OF BOOL; (* Status of each process value read *)
    readSuccess : BOOL; (* Overall read success flag *)
    readError : BOOL; (* Overall read error flag *)

    (* Internal Control Variables *)
    currentIndex : INT; (* Current index for data read *)
    requestSent : BOOL; (* Flag to indicate request has been sent *)
    retryCount : INT; (* Retry counter for communication *)
    maxRetries : INT := 3; (* Maximum retries for communication *)
END_VAR

VAR_INPUT
    triggerRead : BOOL; (* Input to trigger a new read request *)
    inputMasterAddress : INT; (* Address of the remote IO-Link master *)
END_VAR

VAR_OUTPUT
    readStatus : BOOL; (* TRUE if all reads were successful *)
    commHealth : STRING; (* Communication health status *)
END_VAR

(* Step 1: Request initiation *)
IF triggerRead THEN
    IF NOT requestSent THEN
        masterAddress := inputMasterAddress;
        commRequest := TRUE; (* Trigger communication request *)
        currentIndex := 1; (* Start reading from the first process value *)
        retryCount := 0;
        readSuccess := FALSE;
        readError := FALSE;
        requestSent := TRUE;
    END_IF
END_IF

(* Step 2: Communication and data retrieval *)
IF commRequest THEN
    (* Simulated IO-Link read function: IO_Link_ReadData *)
    commStatus := IO_Link_ReadData(masterAddress, currentIndex, processDataRaw[currentIndex]);

    IF commStatus = 0 THEN
        (* Convert raw data to process value (e.g., from bytes to REAL) *)
        processData[currentIndex] := REAL_TO_REAL(processDataRaw[currentIndex]);

        (* Set status flag for this read operation *)
        statusFlags[currentIndex] := TRUE;

        (* Move to the next value or finish read operation *)
        IF currentIndex < 5 THEN
            currentIndex := currentIndex + 1; (* Increment index to read next value *)
        ELSE
            readSuccess := TRUE; (* All reads successful *)
            commRequest := FALSE; (* End communication request *)
        END_IF
    ELSE
        retryCount := retryCount + 1;
        statusFlags[currentIndex] := FALSE; (* Set error flag for this read *)
        IF retryCount >= maxRetries THEN
            readError := TRUE; (* Set error flag if max retries exceeded *)
            commRequest := FALSE;
        END_IF
    END_IF
END_IF

(* Step 3: Status reporting *)
IF readSuccess THEN
    readStatus := TRUE; (* All values were successfully read *)
    commHealth := 'Communication Successful';
ELSE
    readStatus := FALSE;
    IF readError THEN
        commHealth := 'Communication Error: Max Retries Exceeded';
    ELSE
        commHealth := 'Reading In Progress';
    END_IF
END_IF

(* Reset flags when the operation is complete or failed *)
IF NOT commRequest THEN
    requestSent := FALSE;
END_IF
```
