I/O List for Feedwater Control in a Steam-Water Cycle

| **Name**                          | **Signal Tag Number** | **Analog/Digital** | **Engineering Unit** | **Range**                   | **Setpoint**          | **P&ID Reference**    |
|-----------------------------------|-----------------------|-------------------|----------------------|----------------------------|-----------------------|----------------------|
| **Feedwater Flow Transmitter**     | FT-101                | Analog            | kg/hr                | 0 - 100,000                | 50,000                | P&ID-001             |
| **Feedwater Flow Control Valve**   | FCV-101               | Digital           | % Open               | 0 - 100                    | Auto - Adjusted       | P&ID-002             |
| **Feedwater Pressure Transmitter** | PT-102                | Analog            | bar                  | 0 - 120                    | 90                     | P&ID-003             |
| **Feedwater Temperature Transmitter** | TT-103              | Analog            | °C                   | 0 - 250                    | 180                    | P&ID-004             |
| **Boiler Drum Level Transmitter**  | LT-104                | Analog            | %                    | 0 - 100                    | 50%                   | P&ID-005             |
| **Feedwater Pump On/Off**          | P-101                 | Digital           | On/Off               | 0 = Off, 1 = On            | On                    | P&ID-006             |
| **High Drum Level Alarm**          | LAH-104               | Digital           | -                    | 90% (High)                 | Alarm                 | P&ID-005             |
| **Low Drum Level Alarm**           | LAL-104               | Digital           | -                    | 30% (Low)                  | Alarm                 | P&ID-005             |
| **Feedwater Flow Low Alarm**       | FAH-101               | Digital           | -                    | 10,000 (Low)               | Alarm                 | P&ID-001             |
| **Feedwater Isolation Valve**      | XV-105                | Digital           | Open/Close           | 0 = Close, 1 = Open        | Auto - Adjusted       | P&ID-002             |
| **Feedwater Bypass Valve**         | BV-106                | Digital           | % Open               | 0 - 100                    | Manual - 30%          | P&ID-002             |
| **Boiler Outlet Pressure Transmitter** | PT-107             | Analog            | bar                  | 0 - 200                    | 170                   | P&ID-003             |
| **Condensate Flow Transmitter**    | FT-108                | Analog            | kg/hr                | 0 - 100,000                | 40,000                | P&ID-007             |
| **Condensate Pump On/Off**         | P-102                 | Digital           | On/Off               | 0 = Off, 1 = On            | On                    | P&ID-007             |
| **Deaerator Tank Level Transmitter** | LT-109              | Analog            | %                    | 0 - 100                    | 60%                   | P&ID-008             |
| **Deaerator Pressure Transmitter** | PT-110                | Analog            | bar                  | 0 - 10                     | 5                     | P&ID-008             |
| **Boiler Feed Pump Speed Control** | SC-111                | Analog            | RPM                  | 0 - 3000                   | Auto - Adjusted       | P&ID-009             |
| **Steam Drum Pressure Transmitter**| PT-112                | Analog            | bar                  | 0 - 120                    | 90                    | P&ID-005             |
| **Steam Outlet Flow Transmitter**  | FT-113                | Analog            | kg/hr                | 0 - 200,000                | 150,000               | P&ID-010             |
| **Feedwater Control PLC**          | PLC-114               | Digital           | Status               | 0 = Offline, 1 = Online    | Online                | P&ID-011             |

