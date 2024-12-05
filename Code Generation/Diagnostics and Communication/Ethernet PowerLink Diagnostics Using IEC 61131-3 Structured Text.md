```
FUNCTION_BLOCK FB_PowerLinkDiagnostics
VAR
    (* Input Variables *)
    Execute : BOOL; (* Triggers the diagnostic data retrieval *)
    NodeID : INT; (* ID of the PowerLink node to be monitored *)
    MN_ID : INT; (* ID of the PowerLink managing node *)
    Timeout : TIME := T#3s; (* Timeout for diagnostic data retrieval *)

    (* Output Variables *)
    CommunicationStatus : BOOL; (* TRUE if communication is active *)
    NodeHealth : STRING[50]; (* Health status of the node *)
    ErrorDetected : BOOL; (* TRUE if an error is detected *)
    ErrorCode : DWORD; (* Error code associated with the node, if any *)
    NodeStatusDescription : STRING[255]; (* Detailed description of node status *)

    (* Internal Variables *)
    diagBuffer : ARRAY[1..64] OF BYTE; (* Buffer to store raw diagnostic data *)
    diagRequest : BOOL; (* Flag to indicate a diagnostic request is active *)
    commTimer : TON; (* Timer for managing communication timeout *)
    requestInProgress : BOOL; (* Indicates whether a diagnostic request is ongoing *)
    tempString : STRING[255]; (* Temporary variable for building status messages *)
END_VAR
```
```
(* Step 1: Trigger Diagnostic Request *)
IF Execute THEN
    IF NOT requestInProgress THEN
        (* Initiate diagnostic request *)
        diagRequest := TRUE;
        requestInProgress := TRUE;
        commTimer(IN := TRUE, PT := Timeout); (* Start timeout timer *)
        CommunicationStatus := FALSE; (* Default to inactive communication status *)
        ErrorDetected := FALSE; (* Reset error flag *)
        NodeHealth := 'Requesting Diagnostics...';
    END_IF
END_IF

(* Step 2: Manage Communication Timer *)
IF commTimer.Q THEN
    (* If the timer elapses, set communication failure *)
    diagRequest := FALSE;
    requestInProgress := FALSE;
    CommunicationStatus := FALSE;
    ErrorDetected := TRUE;
    ErrorCode := 16#00010000; (* Timeout error code *)
    NodeStatusDescription := CONCAT('Diagnostic Timeout for Node ID: ', INT_TO_STRING(NodeID));
    NodeHealth := 'Communication Failure';
END_IF

(* Step 3: Retrieve Diagnostic Data from the PowerLink Managing Node *)
IF diagRequest THEN
    (* Simulated function call to retrieve diagnostic data from the MN *)
    ReadDiagnostics(MN_ID, NodeID, diagBuffer);

    (* Check diagnostic response *)
    IF diagBuffer[1] = 0 THEN (* Assume first byte indicates status *)
        CommunicationStatus := TRUE; (* Communication successful *)
        ErrorDetected := FALSE; (* No errors detected *)
        ErrorCode := 0;
        NodeHealth := 'Node Operating Normally';
        
        (* Parse detailed diagnostic information *)
        CASE diagBuffer[2] OF
            0: NodeStatusDescription := 'No Errors Detected';
            1: 
                NodeStatusDescription := 'Minor Warning Detected';
                NodeHealth := 'Minor Warning';
            2:
                NodeStatusDescription := 'Major Warning Detected';
                NodeHealth := 'Major Warning';
            3:
                NodeStatusDescription := 'Critical Fault Detected';
                NodeHealth := 'Critical Fault';
                ErrorDetected := TRUE;
                ErrorCode := 16#00020001; (* Critical fault error code *)
            4:
                NodeStatusDescription := 'Node Communication Error';
                NodeHealth := 'Communication Error';
                ErrorDetected := TRUE;
                ErrorCode := 16#00030002; (* Communication error code *)
            ELSE
                NodeStatusDescription := 'Unknown Status';
                NodeHealth := 'Unknown';
        END_CASE;

    ELSE
        (* If status is not zero, treat it as a communication failure *)
        CommunicationStatus := FALSE;
        ErrorDetected := TRUE;
        ErrorCode := 16#00040003; (* General communication error code *)
        NodeStatusDescription := 'Failed to Retrieve Diagnostics';
        NodeHealth := 'Communication Failure';
    END_IF
    (* Clear the diagnostic request and stop the timer *)
    diagRequest := FALSE;
    commTimer(IN := FALSE);
    requestInProgress := FALSE;
END_IF
```
