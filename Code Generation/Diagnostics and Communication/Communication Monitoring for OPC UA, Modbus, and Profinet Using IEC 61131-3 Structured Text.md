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
```
(* Manage Audit Trail Overflow *)
IF auditIndex > 100 THEN
    auditIndex := 1; (* Wrap around if the audit trail is full *)
END_IF
```
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
