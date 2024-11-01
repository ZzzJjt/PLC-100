```
(* Define EtherCAT State Constants *)
VAR CONSTANT
    STATE_INIT : INT := 1; (* INIT state *)
    STATE_PREOP : INT := 2; (* PRE-OPERATIONAL state *)
    STATE_SAFEOP : INT := 4; (* SAFE-OPERATIONAL state *)
    STATE_OP : INT := 8; (* OPERATIONAL state *)
    STATE_BOOT : INT := 3; (* BOOT state, if required *)
END_VAR
```
```
VAR
    (* EtherCAT State Machine Variables *)
    currentState : INT; (* Current state of the EtherCAT slave *)
    nextState : INT; (* Next state to transition to *)
    esmControl : FB_ESM_Control; (* EtherCAT State Machine function block *)
    
    (* Status Flags *)
    stateTransitionDone : BOOL; (* TRUE when the state transition is complete *)
    stateError : BOOL; (* Error flag for any failed state transitions *)

    (* Timer for State Delay *)
    stateTimer : TON; (* Timer to control the 5-second delay between states *)
    timerStarted : BOOL; (* Indicates whether the timer is running *)

    (* Control Flags *)
    initTransition : BOOL; (* TRUE if initial transition sequence started *)
END_VAR
```
```
FUNCTION_BLOCK FB_ESM_Control
VAR_INPUT
    (* Inputs for the EtherCAT State Machine *)
    SlaveID : INT; (* EtherCAT slave device ID *)
    RequestedState : INT; (* State to transition to *)
    Execute : BOOL; (* Trigger for the state change *)
END_VAR

VAR_OUTPUT
    (* Outputs for State Control *)
    Done : BOOL; (* TRUE if the state change is completed successfully *)
    Busy : BOOL; (* TRUE if the state change is in progress *)
    Error : BOOL; (* TRUE if an error occurs during the state change *)
    ErrorID : DWORD; (* Error ID if any issues are detected *)
END_VAR
```
```
PROGRAM Main
VAR
    slaveID : INT := 1; (* EtherCAT slave ID *)
END_VAR

(* Initialize the State Machine if not started *)
IF NOT initTransition THEN
    currentState := STATE_INIT;
    nextState := STATE_PREOP;
    initTransition := TRUE;
END_IF

(* State Transition Logic *)
CASE currentState OF
    STATE_INIT:
        (* Transition to PREOP after 5 seconds *)
        IF NOT timerStarted THEN
            stateTimer(IN := TRUE, PT := T#5s);
            timerStarted := TRUE;
        ELSIF stateTimer.Q THEN
            stateTimer(IN := FALSE);
            esmControl.SlaveID := slaveID;
            esmControl.RequestedState := STATE_PREOP;
            esmControl.Execute := TRUE;
            IF esmControl.Done THEN
                currentState := STATE_PREOP;
                nextState := STATE_SAFEOP;
                timerStarted := FALSE;
            ELSIF esmControl.Error THEN
                stateError := TRUE;
            END_IF
        END_IF

    STATE_PREOP:
        (* Transition to SAFEOP after 5 seconds *)
        IF NOT timerStarted THEN
            stateTimer(IN := TRUE, PT := T#5s);
            timerStarted := TRUE;
        ELSIF stateTimer.Q THEN
            stateTimer(IN := FALSE);
            esmControl.SlaveID := slaveID;
            esmControl.RequestedState := STATE_SAFEOP;
            esmControl.Execute := TRUE;
            IF esmControl.Done THEN
                currentState := STATE_SAFEOP;
                nextState := STATE_OP;
                timerStarted := FALSE;
            ELSIF esmControl.Error THEN
                stateError := TRUE;
            END_IF
        END_IF

    STATE_SAFEOP:
        (* Transition to OP after 5 seconds *)
        IF NOT timerStarted THEN
            stateTimer(IN := TRUE, PT := T#5s);
            timerStarted := TRUE;
        ELSIF stateTimer.Q THEN
            stateTimer(IN := FALSE);
            esmControl.SlaveID := slaveID;
            esmControl.RequestedState := STATE_OP;
            esmControl.Execute := TRUE;
            IF esmControl.Done THEN
                currentState := STATE_OP;
                nextState := STATE_OP; (* Final operational state *)
                timerStarted := FALSE;
            ELSIF esmControl.Error THEN
                stateError := TRUE;
            END_IF
        END_IF

    STATE_OP:
        (* EtherCAT Slave is now in OPERATIONAL state *)
        stateTransitionDone := TRUE;

    ELSE
        stateError := TRUE; (* Unsupported state *)
END_CASE
```
