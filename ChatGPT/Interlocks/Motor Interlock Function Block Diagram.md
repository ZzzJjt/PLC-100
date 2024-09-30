**Function Block Diagram Description:**

	1.	Inputs:
	•	MotorStartCommand: Command signal to start the motor (e.g., from the operator or automatic sequence).
	•	EquipmentRunning[1]: Status input from the first associated equipment (TRUE if running, FALSE if stopped).
	•	EquipmentRunning[2]: Status input from the second associated equipment (TRUE if running, FALSE if stopped).
	•	EquipmentRunning[3]: Status input from the third associated equipment (TRUE if running, FALSE if stopped).
	2.	Logic:
	•	The motor should only start if all EquipmentRunning inputs are FALSE, indicating that no associated equipment is currently in operation.
	•	If any of the EquipmentRunning inputs are TRUE, the motor interlock will prevent the motor from starting by blocking the start command.
	3.	Output:
	•	MotorStartAllowed: Output to the motor start circuit (TRUE = Motor can start, FALSE = Motor cannot start).
```
(* IEC 61131-3 Structured Text Program: Motor Interlock Function Block *)

FUNCTION_BLOCK MotorInterlock
VAR_INPUT
    MotorStartCommand : BOOL;           (* Input: Start command for the motor *)
    EquipmentRunning1 : BOOL;           (* Input: Status of associated equipment 1 *)
    EquipmentRunning2 : BOOL;           (* Input: Status of associated equipment 2 *)
    EquipmentRunning3 : BOOL;           (* Input: Status of associated equipment 3 *)
END_VAR

VAR_OUTPUT
    MotorStartAllowed : BOOL;           (* Output: TRUE if motor can start, FALSE otherwise *)
END_VAR

(* Logic to check interlock conditions *)
IF MotorStartCommand = TRUE THEN
    (* Motor can only start if no associated equipment is running *)
    IF (EquipmentRunning1 = FALSE) AND 
       (EquipmentRunning2 = FALSE) AND 
       (EquipmentRunning3 = FALSE) THEN
        MotorStartAllowed := TRUE;      (* Allow motor to start *)
    ELSE
        MotorStartAllowed := FALSE;     (* Block motor start *)
    END_IF
ELSE
    MotorStartAllowed := FALSE;         (* Reset motor start allowance if no start command *)
END_IF
```
**Function Block Explanation**

	1.	Inputs:
	•	MotorStartCommand: Represents the command signal to start the motor. The motor should only start if this input is set to TRUE.
	•	EquipmentRunning1, EquipmentRunning2, EquipmentRunning3: Status indicators for associated equipment. These inputs monitor if other equipment is running. If any of these inputs are TRUE, it means the corresponding equipment is still operational.
	2.	Logic:
	•	The function block checks if MotorStartCommand is TRUE.
	•	If MotorStartCommand is TRUE, it evaluates the statuses of EquipmentRunning1, EquipmentRunning2, and EquipmentRunning3.
	•	If all equipment statuses are FALSE (indicating that all associated equipment is stopped), MotorStartAllowed is set to TRUE, allowing the motor to start.
	•	If any of the equipment statuses are TRUE, the output remains FALSE, preventing the motor from starting.
	3.	Output:
	•	MotorStartAllowed: The function block sets this output to TRUE only when all equipment statuses are FALSE and a start command is present, allowing the motor to start safely.
