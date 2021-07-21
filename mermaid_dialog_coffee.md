## dialog: coffee
Ana: What kind of coffee do you prefer?

Bob: I prefer to not drink coffee at all!

Ana:  What do you like to drink?

Bob:  I like to drink herbal tea or water.

``` mermaid
sequenceDiagram

Ana->>Bob: What kind of coffee do you prefer?

loop Politeness

Bob->>Bob: Fight against rude reply

end

Note right of Bob: She's trying to be nice!

Bob->>Ana: I prefer to not drink coffee at all!

Ana->>Bob:   What do you like to drink?

Bob->>Ana: I like to drink herbal tea or water.

Ana->>Bob: Ok. I'll see if we have any.

```