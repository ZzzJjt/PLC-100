**1. Variable Declarations:**

The function block uses separate status flags, error codes, and alarm variables for each protocol. An internal timer is used to periodically check each connection.
```
FUNCTION_BLOCK FB_CommMonitoring
VAR
    (* Input Variables for Server Connection Status *)
    OPCUA_Connected : BOOL; (* OPC UA connection status *)
    Modbus_Connected : BOOL; (* Modbus connection status *)
    Profinet_Connected : BOOL; (* Profinet connection status *)

    (* Error Codes for Each Protocol *)
    OPCUA_ErrorCode : DWORD; (* Error code for OPC UA connection *)
    Modbus_ErrorCode : DWORD; (* Error code for Modbus connection *)
    Profinet_ErrorCode : DWORD; (* Error code for Profinet connection *)

    (* Output Alarms *)
    OPCUA_Alarm : BOOL; (* Alarm for OPC UA connection failure *)
    Modbus_Alarm : BOOL; (* Alarm for Modbus connection failure *)
    Profinet_Alarm : BOOL; (* Alarm for Profinet connection failure *)

    (* Audit Trail Variables *)
    AuditTrail : ARRAY[1..100] OF STRING[255]; (* Array to store audit trail entries *)
    auditIndex : INT := 1; (* Index for the next audit entry *)

    (* Internal Control Variables *)
    commCheckTimer : TON; (* Timer for periodic communication checks *)
    timerInterval : TIME := T#5s; (* Timer interval for communication checks *)
    logMessage : STRING[255]; (* Temporary variable to construct log messages *)
END_VAR

VAR_INPUT
    Execute : BOOL; (* Trigger to enable communication monitoring *)
END_VAR

VAR_OUTPUT
    MonitoringActive : BOOL; (* TRUE if communication monitoring is active *)
END_VAR
```

**2. Initialization and Timer Setup:**

The monitoring logic is triggered using the Execute input. A timer (commCheckTimer) is used to execute the monitoring routine every 5 seconds.

```
(* Initialization *)
IF Execute THEN
    IF NOT MonitoringActive THEN
        MonitoringActive := TRUE; (* Activate monitoring *)
        commCheckTimer(IN := TRUE, PT := timerInterval); (* Start the timer *)
    END_IF
ELSE
    MonitoringActive := FALSE; (* Deactivate monitoring *)
    commCheckTimer(IN := FALSE); (* Stop the timer *)
    RETURN;
END_IF
```

**3. Monitoring Logic for Each Protocol:**

The function block checks the connection status of each protocol and handles alarms and audit trail entries based on connection status and error codes.
```
(* Check Connection Status on Timer Trigger *)
IF commCheckTimer.Q THEN
    (* Reset the timer for the next check *)
    commCheckTimer(IN := FALSE);
    commCheckTimer(IN := TRUE);

    (* OPC UA Connection Monitoring *)
    IF NOT OPCUA_Connected THEN
        OPCUA_Alarm := TRUE; (* Set alarm for OPC UA connection failure *)
        logMessage := CONCAT('OPC UA Connection Lost: Error Code ', DWORD_TO_STRING(OPCUA_ErrorCode));
        AuditTrail[auditIndex] := logMessage;
        auditIndex := auditIndex + 1;
    ELSE
        OPCUA_Alarm := FALSE; (* Reset alarm if connection is restored *)
    END_IF

    (* Modbus Connection Monitoring *)
    IF NOT Modbus_Connected THEN
        Modbus_Alarm := TRUE; (* Set alarm for Modbus connection failure *)
        logMessage := CONCAT('Modbus Connection Lost: Error Code ', DWORD_TO_STRING(Modbus_ErrorCode));
        AuditTrail[auditIndex] := logMessage;
        auditIndex := auditIndex + 1;
    ELSE
        Modbus_Alarm := FALSE; (* Reset alarm if connection is restored *)
    END_IF

    (* Profinet Connection Monitoring *)
    IF NOT Profinet_Connected THEN
        Profinet_Alarm := TRUE; (* Set alarm for Profinet connection failure *)
        logMessage := CONCAT('Profinet Connection Lost: Error Code ', DWORD_TO_STRING(Profinet_ErrorCode));
        AuditTrail[auditIndex] := logMessage;
        auditIndex := auditIndex + 1;
    ELSE
        Profinet_Alarm := FALSE; (* Reset alarm if connection is restored *)
    END_IF
END_IF
```
**4. Audit Trail Management:**

The AuditTrail array stores up to 100 entries. If the array is full, it wraps around to the beginning, overwriting old entries.
```
(* Manage Audit Trail Overflow *)
IF auditIndex > 100 THEN
    auditIndex := 1; (* Wrap around if the audit trail is full *)
END_IF
```
**5. Implementation Details:**

	1.	Input Variables:
	•	OPCUA_Connected, Modbus_Connected, and Profinet_Connected: Boolean flags indicating the connection status of each protocol.
	•	OPCUA_ErrorCode, Modbus_ErrorCode, and Profinet_ErrorCode: Error codes corresponding to connection failures for each protocol.
	2.	Output Variables:
	•	OPCUA_Alarm, Modbus_Alarm, and Profinet_Alarm: Alarm flags that are set when a corresponding protocol’s connection fails.
	•	MonitoringActive: Indicates whether the communication monitoring function block is actively monitoring the connections.
	3.	Audit Trail Array:
	•	The AuditTrail array stores the log messages for each communication failure, including the reason for failure and the associated error code.
	•	The array index (auditIndex) is incremented each time a new message is added, wrapping around if the index exceeds the maximum size.
	4.	Timer Control:
	•	A timer (commCheckTimer) is used to periodically check each protocol’s connection status.
	•	The timer runs every 5 seconds (timerInterval := T#5s), ensuring that the monitoring function block performs regular checks.

**6. Example of Function Block Integration:**
```
PROGRAM Main
VAR
    commMonitor : FB_CommMonitoring; (* Instance of the communication monitoring function block *)
    execute : BOOL := TRUE; (* Trigger to start monitoring *)
    opcuaStatus : BOOL := TRUE; (* Example OPC UA connection status *)
    modbusStatus : BOOL := FALSE; (* Example Modbus connection status *)
    profinetStatus : BOOL := TRUE; (* Example Profinet connection status *)
    opcuaError : DWORD := 16#00010001; (* Example OPC UA error code *)
    modbusError : DWORD := 16#00020002; (* Example Modbus error code *)
    profinetError : DWORD := 16#00030003; (* Example Profinet error code *)
END_VAR

(* Set inputs for the function block *)
commMonitor.Execute := execute;
commMonitor.OPCUA_Connected := opcuaStatus;
commMonitor.Modbus_Connected := modbusStatus;
commMonitor.Profinet_Connected := profinetStatus;
commMonitor.OPCUA_ErrorCode := opcuaError;
commMonitor.Modbus_ErrorCode := modbusError;
commMonitor.Profinet_ErrorCode := profinetError;

(* Call the function block *)
commMonitor();

(* Check and display the alarm and audit trail status *)
IF commMonitor.OPCUA_Alarm THEN
    WriteString('OPC UA Alarm Triggered');
END_IF

IF commMonitor.Modbus_Alarm THEN
    WriteString('Modbus Alarm Triggered');
END_IF

IF commMonitor.Profinet_Alarm THEN
    WriteString('Profinet Alarm Triggered');
END_IF

(* Display the audit trail *)
FOR i := 1 TO 100 DO
    IF LEN(commMonitor.AuditTrail[i]) > 0 THEN
        WriteString('Audit Trail Entry ', INT_TO_STRING(i), ': ', commMonitor.AuditTrail[i]);
    END_IF
END_FOR
```
