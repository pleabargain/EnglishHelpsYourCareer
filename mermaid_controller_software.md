```mermaid
sequenceDiagram

developer ->>+ dev_pc: init hardware

developer ->>+ dev_pc: program controller with firmware

dev_pc->>+dev_pc_config_script: manipulate firmware

dev_pc_config_script->>+controller: commands

controller->>controller: API

controller->>controller: performs scripted behavior

controller->>controller: feedback

controller->>developer: data

```