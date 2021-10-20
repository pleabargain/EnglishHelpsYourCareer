
```mermaid
sequenceDiagram
    participant Ana
    participant Bob
    Ana->>Bob: Hello Bob, what's the status of our project?
    loop StatusQuery
        Bob->>Bob: Fight against yelling that nothing has changed since she last asked
    end
    Note right of Bob: Rational thoughts <br/>prevail!
    Bob -->>Ana: Great!
    John->>Bob: How is the project going?
    loop StatusQuery
        Bob->>Bob: Is everyone going to ask the same question today?
            end
    Note right of Bob: Secure negative emotions <br/>prevail!
    Bob-->>John: Jolly good!
```