```
#include <open62541/client.h>
#include <open62541/client_config_default.h>
#include <string.h>

typedef struct {
    bool execute;
    char serverUrl[256];
    uint32_t timeout; // Timeout in milliseconds
    bool done;
    bool busy;
    bool error;
    uint32_t errorID;
} OPCUA_ClientType;

void OPCUA_ConnectToServer(OPCUA_ClientType *params) {
    if (!params->execute) {
        params->done = false;
        params->busy = false;
        params->error = false;
        params->errorID = 0;
        return;
    }

    if (params->busy) {
        return; // Avoid re-execution if already in progress
    }

    params->busy = true;
    UA_Client *client = UA_Client_new();
    UA_ClientConfig_setDefault(UA_Client_getConfig(client));

    UA_StatusCode retval = UA_Client_connect(client, params->serverUrl);
    if (retval == UA_STATUSCODE_GOOD) {
        params->done = true;
    } else {
        params->error = true;
        params->errorID = retval;
    }

    UA_Client_disconnect(client);
    UA_Client_delete(client);

    params->busy = false;
}
```

```
FUNCTION_BLOCK FB_OPCUA_Client
VAR
    (* Input Variables *)
    Execute : BOOL; (* Triggers the connection process *)
    ServerUrl : STRING[255]; (* OPC UA Server URL *)
    Timeout : TIME; (* Timeout for the connection process *)

    (* Output Variables *)
    Done : BOOL; (* Indicates successful connection *)
    Busy : BOOL; (* Indicates the connection is in progress *)
    Error : BOOL; (* Indicates an error during connection *)
    ErrorID : DWORD; (* Error identifier if an error occurs *)
END_VAR

VAR
    (* Internal Variables for Calling the C Function *)
    opcuaParams : POINTER TO OPCUA_ClientType; (* Pointer to the C function block parameters *)
    serverUrlArray : ARRAY[0..255] OF BYTE; (* Array to convert STRING to C-compatible format *)
    timeoutMs : DWORD; (* Timeout in milliseconds *)
END_VAR

(* Convert TIME to milliseconds *)
timeoutMs := TIME_TO_DWORD(Timeout);

(* Convert ServerUrl STRING to C-compatible array *)
FOR i := 1 TO LEN(ServerUrl) DO
    serverUrlArray[i-1] := BYTE_TO_INT(STRING_TO_BYTE(ServerUrl[i]));
END_FOR

(* Null-terminate the C string *)
serverUrlArray[LEN(ServerUrl)] := 0;

(* Set parameters for the C function block *)
opcuaParams^.execute := Execute;
MEMCPY(opcuaParams^.serverUrl, serverUrlArray, LEN(ServerUrl) + 1); (* Copy URL to C structure *)
opcuaParams^.timeout := timeoutMs;

(* Call the C function block *)
OPCUA_ConnectToServer(opcuaParams);

(* Map results back to structured text outputs *)
Done := opcuaParams^.done;
Busy := opcuaParams^.busy;
Error := opcuaParams^.error;
ErrorID := opcuaParams^.errorID;
```
```
PROGRAM Main
VAR
    myOPCUAClient : FB_OPCUA_Client; (* Instance of the OPC UA client function block *)
    serverUrl : STRING[255] := 'opc.tcp://127.0.0.1:4840'; (* URL of the OPC UA server *)
    timeout : TIME := T#5000ms; (* Connection timeout of 5000 ms *)
END_VAR

(* Set inputs for the function block *)
myOPCUAClient.Execute := TRUE; (* Trigger connection *)
myOPCUAClient.ServerUrl := serverUrl; (* Set the OPC UA server URL *)
myOPCUAClient.Timeout := timeout; (* Set timeout *)

(* Call the function block *)
myOPCUAClient();

(* Check outputs and handle results *)
IF myOPCUAClient.Done THEN
    WriteString('OPC UA Client connected successfully.');
ELSIF myOPCUAClient.Error THEN
    WriteString('OPC UA Client connection failed. Error ID: ', DWORD_TO_STRING(myOPCUAClient.ErrorID));
END_IF
```
