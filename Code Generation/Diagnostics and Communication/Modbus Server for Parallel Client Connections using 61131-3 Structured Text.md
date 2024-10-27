The following Structured Text code outlines a basic Modbus server that can handle up to 10 parallel client connections using Modbus TCP. It supports the Modbus function codes specified:

```
FUNCTION_BLOCK FB_ModbusServer
VAR
    (* Network Variables *)
    tcpServer : TCP_Server; (* TCP server for managing connections *)
    tcpClient : ARRAY[1..10] OF TCP_Client; (* Array to handle up to 10 clients *)
    
    (* Modbus Data Storage *)
    coils : ARRAY[1..100] OF BOOL; (* Coil data storage *)
    discreteInputs : ARRAY[1..100] OF BOOL; (* Discrete inputs storage *)
    holdingRegisters : ARRAY[1..100] OF INT; (* Holding registers storage *)
    inputRegisters : ARRAY[1..100] OF INT; (* Input registers storage *)

    (* Modbus Communication Variables *)
    requestBuffer : ARRAY[1..256] OF BYTE; (* Buffer to store incoming requests *)
    responseBuffer : ARRAY[1..256] OF BYTE; (* Buffer to store outgoing responses *)
    
    (* Status and Control *)
    connectedClients : INT; (* Number of active clients *)
    i : INT; (* Loop index *)
    errorFlag : BOOL; (* Error status *)
END_VAR

VAR_INPUT
    serverPort : INT; (* Modbus TCP server port, e.g., 502 *)
END_VAR

VAR_OUTPUT
    serverStatus : BOOL; (* Server running status *)
END_VAR

(* Initialize the Modbus server and listen for connections *)
IF NOT serverStatus THEN
    tcpServer.Initialize(serverPort);
    serverStatus := TRUE;
END_IF

(* Accept new connections and handle multiple clients *)
FOR i := 1 TO 10 DO
    IF NOT tcpClient[i].IsConnected THEN
        tcpClient[i].Connect(tcpServer);
    END_IF
END_FOR

(* Handle Modbus requests for each connected client *)
FOR i := 1 TO 10 DO
    IF tcpClient[i].IsConnected THEN
        tcpClient[i].Receive(requestBuffer); (* Receive Modbus request *)
        (* Process Modbus request based on function code *)
        CASE requestBuffer[7] OF
            1: ReadCoils(requestBuffer, responseBuffer, coils);
            2: ReadDiscreteInputs(requestBuffer, responseBuffer, discreteInputs);
            3: ReadHoldingRegisters(requestBuffer, responseBuffer, holdingRegisters);
            4: ReadInputRegisters(requestBuffer, responseBuffer, inputRegisters);
            5: WriteSingleCoil(requestBuffer, responseBuffer, coils);
            6: WriteSingleRegister(requestBuffer, responseBuffer, holdingRegisters);
            15: WriteMultipleCoils(requestBuffer, responseBuffer, coils);
            16: WriteMultipleRegisters(requestBuffer, responseBuffer, holdingRegisters);
            23: ReadWriteMultipleRegisters(requestBuffer, responseBuffer, holdingRegisters);
        ELSE
            (* Unsupported function code *)
            errorFlag := TRUE;
        END_CASE;

        IF NOT errorFlag THEN
            tcpClient[i].Send(responseBuffer); (* Send response back to the client *)
        ELSE
            (* Handle error response *)
            tcpClient[i].SendErrorResponse(requestBuffer, responseBuffer);
        END_IF
    END_IF
END_FOR
```

**Description of the ReadCoils Method**

The ReadCoils method is responsible for processing client requests to read the status of coils (binary outputs) from the server. The method maps client requests to a subset of the coil data array and formats the response according to the Modbus TCP protocol.

**Steps for ReadCoils Method:**

	1.	Extract Request Information:
	•	Parse the Modbus request from the requestBuffer.
	•	Extract starting address and number of coils requested.
	2.	Validate Coil Range:
	•	Ensure the requested range falls within the bounds of the defined coil array. If the range is invalid, set an error flag.
	3.	Read Coil Data:
	•	Traverse the coils array and read the requested coil states.
	•	Pack the coil data into the responseBuffer in the appropriate format (LSB first).
	4.	Construct the Modbus TCP Response:
	•	Construct a Modbus TCP response header with the function code 0x01.
	•	Include the byte count and the requested coil values in the response.
	5.	Send the Response:
	•	The constructed response is sent back to the client using the TCP client interface.

**Example of the ReadCoils Method**
```
FUNCTION ReadCoils : BOOL
VAR_INPUT
    requestBuffer : ARRAY[1..256] OF BYTE;
    responseBuffer : ARRAY[1..256] OF BYTE;
    coilData : ARRAY[1..100] OF BOOL;
END_VAR
VAR
    startAddress : INT;
    quantityOfCoils : INT;
    byteCount : INT;
    coilIndex : INT;
    coilByte : BYTE;
    i : INT;
END_VAR

(* Extract start address and number of coils from request *)
startAddress := requestBuffer[9] * 256 + requestBuffer[10];
quantityOfCoils := requestBuffer[11] * 256 + requestBuffer[12];

(* Validate range *)
IF (startAddress < 1) OR (startAddress + quantityOfCoils - 1 > 100) THEN
    RETURN FALSE; (* Invalid range *)
END_IF

(* Read coils and pack into response buffer *)
byteCount := (quantityOfCoils + 7) / 8; (* Calculate number of bytes needed *)
coilIndex := startAddress;
FOR i := 1 TO byteCount DO
    coilByte := 0;
    FOR j := 0 TO 7 DO
        IF coilIndex <= startAddress + quantityOfCoils - 1 THEN
            IF coilData[coilIndex] THEN
                coilByte := coilByte OR (1 SHL j);
            END_IF
            coilIndex := coilIndex + 1;
        END_IF
    END_FOR
    responseBuffer[10 + i] := coilByte; (* Store packed coil data *)
END_FOR

(* Construct Modbus TCP response *)
responseBuffer[8] := 0x01; (* Function code *)
responseBuffer[9] := byteCount; (* Byte count *)
RETURN TRUE; (* Read successful *)
```

Explanation

	•	The ReadCoils function processes the Modbus 0x01 request, extracts the starting address and coil quantity, reads the coils, packs them into bytes, and constructs the response message.
	•	The method checks the validity of the request, ensuring that it does not exceed the coil array’s boundaries.
	•	After constructing the response, it returns a TRUE status if successful or a FALSE status if there’s an error.
