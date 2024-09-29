The implementation involves creating a custom C function block for OPC UA subscription management using the Open62541 library. This C function block is then wrapped in an IEC 61131-3 structured text (ST) function block to provide integration with standard PLC programming environments.

**1. C Function Block Implementation:**

The C code leverages Open62541 to create an OPC UA subscription and return a subscription handle. It handles the OPC UA client connection, creates a subscription, and manages error reporting.

```
#include <open62541/client.h>
#include <open62541/client_config_default.h>
#include <stdint.h>

typedef struct {
    uint8_t executed;
    uint8_t priority;
    uint32_t timeout; // Timeout in milliseconds
    uint32_t connectionHandle;
    uint32_t publishingInterval;
    uint8_t done;
    uint8_t busy;
    uint8_t error;
    uint32_t errorID;
    uint32_t subscriptionHdl;
} OPCUA_SubscriptionType;

void OPCUA_CreateSubscription(OPCUA_SubscriptionType *params) {
    UA_Client *client = (UA_Client *)(uintptr_t)params->connectionHandle;

    if (!params->executed) {
        params->done = 0;
        params->busy = 0;
        params->error = 0;
        params->errorID = 0;
        return;
    }

    if (params->busy) {
        return; // If already busy, avoid re-execution
    }

    params->busy = 1;
    UA_ClientConfig *config = UA_Client_getConfig(client);

    if (!config) {
        params->error = 1;
        params->errorID = 0x01; // Configuration error
        params->busy = 0;
        return;
    }

    UA_CreateSubscriptionRequest request = UA_CreateSubscriptionRequest_default();
    request.requestedPublishingInterval = (double)params->publishingInterval;
    request.priority = params->priority;

    UA_CreateSubscriptionResponse response = UA_Client_Subscriptions_create(client, request, NULL, NULL, NULL);
    if (response.responseHeader.serviceResult == UA_STATUSCODE_GOOD) {
        params->subscriptionHdl = response.subscriptionId;
        params->done = 1;
    } else {
        params->error = 1;
        params->errorID = response.responseHeader.serviceResult;
    }

    params->busy = 0;
}
```

**2. IEC 61131-3 Structured Text Wrapper:**

The C function block is wrapped using IEC 61131-3 structured text code to integrate it into a typical PLC environment. This wrapper calls the C function and manages the inputs and outputs in a standardized manner.

```
FUNCTION_BLOCK FB_OPCUA_Subscription
VAR
    (* Input Variables *)
    executed : BOOL; (* Trigger for executing the subscription creation *)
    priority : BYTE; (* Priority of the subscription *)
    timeout : TIME; (* Timeout for the operation *)
    connectionHandle : DWORD; (* Handle to the OPC UA connection *)

    (* IN/OUT Variables *)
    PublishingInterval : TIME; (* Publishing interval for the subscription *)
    
    (* Output Variables *)
    Done : BOOL; (* TRUE if the subscription is created successfully *)
    Busy : BOOL; (* TRUE if the subscription is in progress *)
    Error : BOOL; (* TRUE if an error occurs *)
    ErrorID : DWORD; (* Error identifier if an error occurs *)
    SubscriptionHdl : DWORD; (* Subscription handle for the created subscription *)
END_VAR

VAR
    (* Internal Variables for Calling the C Function *)
    opcuaParams : POINTER TO OPCUA_SubscriptionType; (* Pointer to the C function block parameters *)
    intervalMs : DWORD; (* Publishing interval in milliseconds *)
END_VAR

(* Convert TIME to milliseconds *)
intervalMs := TIME_TO_DWORD(PublishingInterval);

(* Set parameters for the C function block *)
opcuaParams^.executed := executed;
opcuaParams^.priority := priority;
opcuaParams^.timeout := TIME_TO_DWORD(timeout); (* Convert TIME to DWORD *)
opcuaParams^.connectionHandle := connectionHandle;
opcuaParams^.publishingInterval := intervalMs;

(* Call the C function block *)
OPCUA_CreateSubscription(opcuaParams);

(* Map results back to structured text outputs *)
Done := opcuaParams^.done;
Busy := opcuaParams^.busy;
Error := opcuaParams^.error;
ErrorID := opcuaParams^.errorID;
SubscriptionHdl := opcuaParams^.subscriptionHdl;
```

**3. Calling the Function Block in a Structured Text Program:**

The structured text program can instantiate and use the FB_OPCUA_Subscription function block within a larger automation control logic.
```
PROGRAM Main
VAR
    mySubscription : FB_OPCUA_Subscription; (* Instance of the OPC UA subscription function block *)
    connHandle : DWORD := 16#A1B2C3D4; (* Simulated connection handle *)
    interval : TIME := T#1000ms; (* Subscription interval of 1000 ms *)
    timeout : TIME := T#5000ms; (* Timeout for operation *)
END_VAR

(* Set inputs for the function block *)
mySubscription.executed := TRUE; (* Trigger subscription creation *)
mySubscription.priority := 1; (* Set priority *)
mySubscription.timeout := timeout; (* Set timeout *)
mySubscription.connectionHandle := connHandle; (* Pass the connection handle *)
mySubscription.PublishingInterval := interval; (* Set the publishing interval *)

(* Call the function block *)
mySubscription();

(* Check outputs *)
IF mySubscription.Done THEN
    (* Subscription successfully created *)
    WriteString('Subscription created successfully. Subscription Handle: ', DWORD_TO_STRING(mySubscription.SubscriptionHdl));
ELSIF mySubscription.Error THEN
    (* Handle the error *)
    WriteString('Error creating subscription. Error ID: ', DWORD_TO_STRING(mySubscription.ErrorID));
END_IF
```
**4. Explanation of the Implementation**

**Inputs and Outputs:**

	•	Input Variables:
	•	executed: A flag to initiate the subscription creation process.
	•	priority: The priority level of the OPC UA subscription.
	•	timeout: The maximum time the function block should wait before timing out.
	•	connectionHandle: A DWORD handle representing the active OPC UA client connection.
	•	IN/OUT Variable:
	•	PublishingInterval: A TIME type variable that allows dynamic adjustment of the subscription’s publishing interval.
	•	Output Variables:
	•	Done: Indicates the successful creation of the subscription.
	•	Busy: Shows if the function block is currently executing the subscription request.
	•	Error: Indicates whether an error occurred.
	•	ErrorID: Holds the error code if Error is set to TRUE.
	•	SubscriptionHdl: The handle for the newly created OPC UA subscription.
