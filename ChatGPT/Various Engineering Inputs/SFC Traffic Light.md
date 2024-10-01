The Sequential Function Chart (SFC) represents the control logic of a simple traffic light system with three states: Red, Green, and Yellow. Each state will have a defined timer delay to control the timing of the lights.

─────────────────────────────────────────────────────────────────────────  
 Start ───▶┌───────────────┐          ┌───────────────┐          ┌───────────────┐  
           │  Red Light ON │          │ Green Light ON│          │ Yellow Light ON│  
           │               │          │               │          │               │  
           │  TMR = 10 sec │          │  TMR = 15 sec │          │  TMR = 3 sec  │  
           └───────┬───────┘          └───────┬───────┘          └───────┬───────┘  
                   │                          │                          │  
                   │                          │                          │  
        ┌──────────▼──────────┐      ┌────────▼──────────┐      ┌────────▼──────────┐  
        │  Transition (T1)    │      │  Transition (T2)  │      │  Transition (T3)  │  
        │                     │      │                  │      │                  │  
        │  Condition: TMR_DN  │      │ Condition: TMR_DN│      │ Condition: TMR_DN │  
        │  (Timer Done)       │      │ (Timer Done)     │      │ (Timer Done)      │  
        └──────────┬──────────┘      └────────┬─────────┘      └────────┬─────────┘  
                   │                          │                          │  
                   ▼                          ▼                          ▼  
         ┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐  
         │ Reset Red Timer │        │ Reset Green Timer│       │ Reset Yellow Timer│  
         └─────────────────┘        └─────────────────┘        └─────────────────┘  
                   │                          │                          │  
                   ▼                          ▼                          ▼  
           ┌───────────────┐          ┌───────────────┐          ┌───────────────┐  
           │  Green Light  │          │ Yellow Light  │          │  Red Light   │  
           │     ON        │          │     ON        │          │     ON        │  
           └───────────────┘          └───────────────┘          └───────────────┘  

─────────────────────────────────────────────────────────────────────────  


State Descriptions and Timer Details:

	1.	Red Light ON State:
	•	Action: Turns on the Red Light for 10 seconds.
	•	Timer: TMR = 10 sec.
	•	Transition Condition: When the timer is done (TMR_DN), the SFC transitions to the next state (Green Light ON).
	2.	Green Light ON State:
	•	Action: Turns on the Green Light for 15 seconds.
	•	Timer: TMR = 15 sec.
	•	Transition Condition: When the timer is done (TMR_DN), the SFC transitions to the next state (Yellow Light ON).
	3.	Yellow Light ON State:
	•	Action: Turns on the Yellow Light for 3 seconds.
	•	Timer: TMR = 3 sec.
	•	Transition Condition: When the timer is done (TMR_DN), the SFC transitions back to the initial state (Red Light ON).

SFC Symbols and Connections:

	•	States: Represented by rectangles (e.g., Red Light ON).
	•	Transitions: Represented by diamonds (e.g., Transition (T1)) and indicate the conditions for moving from one state to another.
	•	Actions: Include operations such as turning on/off the lights or resetting timers.
	•	Timers: Associated with each state to manage delays (e.g., TMR = 10 sec).

This SFC diagram controls a traffic light with timed sequences for each color, ensuring smooth transitions and safe traffic management. Let me know if you want to add more conditions or extend the diagram!
