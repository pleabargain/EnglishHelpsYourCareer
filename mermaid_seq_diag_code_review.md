
```mermaid
sequenceDiagram

trainee->>pull request: request code review

code reviewer->>pull request: check trainee code

code reviewer->>trainee: discuss code

trainee->>code reviewer: clarify request

code reviewer->>trainee: request changes

trainee->>pull request: submit changes

code reviewer->>pull request: check pull request

code reviewer->>pull request: approve

trainee->>pull request: merge changes

```
