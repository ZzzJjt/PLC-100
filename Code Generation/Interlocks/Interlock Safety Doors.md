Below is an IEC 61131-3 Structured Text program that implements safety door interlocks for a chemical reactor. The program monitors the status of multiple safety doors around the reactor. If any safety door is open, the reactor will not start or continue its operation. During operation, if a door is opened, the interlock logic triggers an emergency shutdown, which immediately deactivates the reactor and stops all hazardous processes.

```
(* IEC 61131-3 Structured Text Program: Safety Door Interlocks for Chemical Reactor *)

FUNCTION_BLOCK SafetyDoorInterlock
VAR_INPUT
    SafetyDoor1 : BOOL;              (* Status of Safety Door 1 (TRUE = Closed, FALSE = Open) *)
    SafetyDoor2 : BOOL;              (* Status of Safety Door 2 (TRUE = Closed, FALSE = Open) *)
    SafetyDoor3 : BOOL;              (* Status of Safety Door 3 (TRUE = Closed, FALSE = Open) *)
    ReactorStartCommand : BOOL;      (* Start command for the reactor (TRUE = Start, FALSE = Stop) *)
END_VAR

VAR_OUTPUT
    ReactorRunning : BOOL := FALSE;  (* Output: Reactor running status (TRUE = Running, FALSE = Stopped) *)
    EmergencyShutdown : BOOL := FALSE; (* Output: Emergency shutdown indicator (TRUE = Shutdown Active) *)
END_VAR

VAR
    AllDoorsClosed : BOOL;           (* Internal variable to monitor if all safety doors are closed *)
END_VAR

(* Check if all safety doors are closed *)
AllDoorsClosed := SafetyDoor1 AND SafetyDoor2 AND SafetyDoor3;

(* Interlock Logic *)
IF NOT AllDoorsClosed THEN
    (* If any safety door is open, trigger emergency shutdown and stop reactor *)
    ReactorRunning := FALSE;         (* Stop reactor operation *)
    EmergencyShutdown := TRUE;       (* Activate emergency shutdown *)
ELSE
    (* If all safety doors are closed, allow reactor operation *)
    IF ReactorStartCommand AND (NOT EmergencyShutdown) THEN
        ReactorRunning := TRUE;      (* Start reactor if command is given and no shutdown active *)
    ELSE
        ReactorRunning := FALSE;     (* Keep reactor stopped if no start command or emergency shutdown *)
    END_IF
END_IF

(* Maintain Emergency Shutdown State until Manually Reset *)
IF EmergencyShutdown AND NOT ReactorStartCommand THEN
    EmergencyShutdown := TRUE;       (* Keep emergency shutdown active even if doors close again *)
END_IF

(* Safety Notes *)
(* 1. The reactor will only start or continue operating if all safety doors are closed. *)
(* 2. If any door is opened during operation, an emergency shutdown is triggered. *)
(* 3. Manual intervention is required to restart the reactor after an emergency shutdown. *)
```

Program Explanation

	1.	Input Variables:
	•	SafetyDoor1, SafetyDoor2, SafetyDoor3: These inputs represent the status of each safety door. A value of TRUE means the door is securely closed, and FALSE indicates the door is open.
	•	ReactorStartCommand: Command input to start the reactor (e.g., from the operator or an automated sequence).
	2.	Output Variables:
	•	ReactorRunning: Indicates whether the reactor is currently operating. TRUE means the reactor is running, and FALSE means it is stopped.
	•	EmergencyShutdown: Indicates whether the system is in an emergency shutdown state due to a door being open.
	3.	Internal Variables:
	•	AllDoorsClosed: An internal variable used to determine if all safety doors are securely closed.
	4.	Interlock Logic:
	•	The interlock logic first checks if all safety doors are closed using the AllDoorsClosed variable.
	•	If any safety door is open, the reactor is immediately stopped (ReactorRunning := FALSE), and an emergency shutdown is activated (EmergencyShutdown := TRUE).
	•	If all doors are closed and there is a valid start command (ReactorStartCommand := TRUE), the reactor starts running (ReactorRunning := TRUE).
	•	The program ensures that, once the emergency shutdown is triggered, the reactor cannot restart automatically, even if all safety doors are closed again. Manual intervention is required to reset the system.
