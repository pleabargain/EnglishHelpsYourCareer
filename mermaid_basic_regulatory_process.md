```mermaid
sequenceDiagram

customer->>+reg co: We have a product

customer->>+reg co: We have a process.

reg co->>+customer: Do you need register to your product?

customer->>+reg co: Yes.

reg co->>+customer: Where do you need to register to your product?

customer->> reg co: Ukraine.

reg co->>+customer: Is the first time you have registered a product?

customer->>+reg co: Yes.

reg co->>+customer: What comapany did you use before?

reg co->>+customer: {describe requirements to the customer}

customer->> reg co: How long will it take?

customer->> reg co: How much will it cost?

reg co ->> customer: {begin negotiations}

reg co ->> reg company legal dept: request contract

reg company legal dept->>reg company legal dept: prepare contract

reg company legal dept->> customer: send contract

customer->> customer: debate | sign contract

customer->> reg company legal dept: send contract

reg co ->>reg co: start work
```

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgY3VzdG9tZXItPj4rcmVnIGNvOiBXZSBoYXZlIGEgcHJvZHVjdFxuICAgIGN1c3RvbWVyLT4-K3JlZyBjbzogV2UgaGF2ZSBhIHByb2Nlc3MuXG4gICAgcmVnIGNvLT4-K2N1c3RvbWVyOiBEbyB5b3UgbmVlZCByZWdpc3RlciB0byB5b3VyIHByb2R1Y3Q_XG4gICAgY3VzdG9tZXItPj4rcmVnIGNvOiBZZXMuXG4gICAgcmVnIGNvLT4-K2N1c3RvbWVyOiBXaGVyZSBkbyB5b3UgbmVlZCB0byByZWdpc3RlciB0byB5b3VyIHByb2R1Y3Q_XG4gICAgY3VzdG9tZXItPj4gcmVnIGNvOiBVa3JhaW5lLlxuICAgIHJlZyBjby0-PitjdXN0b21lcjogSXMgdGhlIGZpcnN0IHRpbWUgeW91IGhhdmUgcmVnaXN0ZXJlZCBhIHByb2R1Y3Q_XG4gICAgY3VzdG9tZXItPj4rcmVnIGNvOiBZZXMuXG4gICAgcmVnIGNvLT4-K2N1c3RvbWVyOiBXaGF0IGNvbWFwYW55IGRpZCB5b3UgdXNlIGJlZm9yZT9cbiAgICByZWcgY28tPj4rY3VzdG9tZXI6IHtkZXNjcmliZSByZXF1aXJlbWVudHMgdG8gdGhlIGN1c3RvbWVyfVxuICAgIGN1c3RvbWVyLT4-IHJlZyBjbzogSG93IGxvbmcgd2lsbCBpdCB0YWtlP1xuICAgIGN1c3RvbWVyLT4-IHJlZyBjbzogSG93IG11Y2ggd2lsbCBpdCBjb3N0P1xuICAgIHJlZyBjbyAtPj4gY3VzdG9tZXI6IHtiZWdpbiBuZWdvdGlhdGlvbnN9XG4gICAgcmVnIGNvIC0-PiByZWcgY29tcGFueSBsZWdhbCBkZXB0OiByZXF1ZXN0IGNvbnRyYWN0XG4gICAgcmVnIGNvbXBhbnkgbGVnYWwgZGVwdC0-PnJlZyBjb21wYW55IGxlZ2FsIGRlcHQ6IHByZXBhcmUgY29udHJhY3RcbiAgICByZWcgY29tcGFueSBsZWdhbCBkZXB0LT4-IGN1c3RvbWVyOiBzZW5kIGNvbnRyYWN0XG4gICAgY3VzdG9tZXItPj4gY3VzdG9tZXI6IGRlYmF0ZSB8IHNpZ24gY29udHJhY3RcbiAgICBjdXN0b21lci0-PiByZWcgY29tcGFueSBsZWdhbCBkZXB0OiBzZW5kIGNvbnRyYWN0XG4gICAgcmVnIGNvIC0-PnJlZyBjbzogc3RhcnQgd29ya1xuXG5cblxuXG4gICAgICAgICAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgY3VzdG9tZXItPj4rcmVnIGNvOiBXZSBoYXZlIGEgcHJvZHVjdFxuICAgIGN1c3RvbWVyLT4-K3JlZyBjbzogV2UgaGF2ZSBhIHByb2Nlc3MuXG4gICAgcmVnIGNvLT4-K2N1c3RvbWVyOiBEbyB5b3UgbmVlZCByZWdpc3RlciB0byB5b3VyIHByb2R1Y3Q_XG4gICAgY3VzdG9tZXItPj4rcmVnIGNvOiBZZXMuXG4gICAgcmVnIGNvLT4-K2N1c3RvbWVyOiBXaGVyZSBkbyB5b3UgbmVlZCB0byByZWdpc3RlciB0byB5b3VyIHByb2R1Y3Q_XG4gICAgY3VzdG9tZXItPj4gcmVnIGNvOiBVa3JhaW5lLlxuICAgIHJlZyBjby0-PitjdXN0b21lcjogSXMgdGhlIGZpcnN0IHRpbWUgeW91IGhhdmUgcmVnaXN0ZXJlZCBhIHByb2R1Y3Q_XG4gICAgY3VzdG9tZXItPj4rcmVnIGNvOiBZZXMuXG4gICAgcmVnIGNvLT4-K2N1c3RvbWVyOiBXaGF0IGNvbWFwYW55IGRpZCB5b3UgdXNlIGJlZm9yZT9cbiAgICByZWcgY28tPj4rY3VzdG9tZXI6IHtkZXNjcmliZSByZXF1aXJlbWVudHMgdG8gdGhlIGN1c3RvbWVyfVxuICAgIGN1c3RvbWVyLT4-IHJlZyBjbzogSG93IGxvbmcgd2lsbCBpdCB0YWtlP1xuICAgIGN1c3RvbWVyLT4-IHJlZyBjbzogSG93IG11Y2ggd2lsbCBpdCBjb3N0P1xuICAgIHJlZyBjbyAtPj4gY3VzdG9tZXI6IHtiZWdpbiBuZWdvdGlhdGlvbnN9XG4gICAgcmVnIGNvIC0-PiByZWcgY29tcGFueSBsZWdhbCBkZXB0OiByZXF1ZXN0IGNvbnRyYWN0XG4gICAgcmVnIGNvbXBhbnkgbGVnYWwgZGVwdC0-PnJlZyBjb21wYW55IGxlZ2FsIGRlcHQ6IHByZXBhcmUgY29udHJhY3RcbiAgICByZWcgY29tcGFueSBsZWdhbCBkZXB0LT4-IGN1c3RvbWVyOiBzZW5kIGNvbnRyYWN0XG4gICAgY3VzdG9tZXItPj4gY3VzdG9tZXI6IGRlYmF0ZSB8IHNpZ24gY29udHJhY3RcbiAgICBjdXN0b21lci0-PiByZWcgY29tcGFueSBsZWdhbCBkZXB0OiBzZW5kIGNvbnRyYWN0XG4gICAgcmVnIGNvIC0-PnJlZyBjbzogc3RhcnQgd29yXG5cblxuXG5cbiAgICAgICAgICAgICIsIm1lcm1haWQiOiJ7XG4gIFwidGhlbWVcIjogXCJkZWZhdWx0XCJcbn0iLCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)