```mermaid
stateDiagram-v2

[*] --> Still

Still --> Moving

Moving --> Still

Moving --> fault

Moving --> halt_operations

halt_operations --> [*]

fault --> Crash

Crash--> [*]
```