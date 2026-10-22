# Visitor flows

Planning diagrams for the portfolio. They are written in Mermaid, so they render on GitHub and in most Markdown viewers.

## Actors and use cases

Actors sit outside the system boundary. Use cases sit inside it. Each use case should map to a visible section of the page.

```mermaid
flowchart LR
    Recruiter([Recruiter / hiring manager])
    Client([Potential client])
    Peer([Peer / collaborator])

    subgraph Portfolio [Portfolio site]
        UC1((Scan selected work))
        UC2((Read a case study))
        UC3((Learn about the designer))
        UC4((Check services))
        UC5((Send a message))
    end

    Recruiter --> UC1
    Recruiter --> UC2
    Recruiter --> UC3
    Client --> UC1
    Client --> UC4
    Client --> UC5
    Peer --> UC3
    Peer --> UC5
```

## Activity flow: from landing to contact

Only one start and one end. Each decision has labelled branches.

```mermaid
flowchart TD
    Start([Visitor lands on page]) --> Hero{Does the hero<br/>match what I need?}
    Hero -- No --> Leave([Leaves])
    Hero -- Yes --> Work[Scan selected work]
    Work --> Interest{Relevant project?}
    Interest -- No --> About[Read About]
    About --> Fit{Fits what I need?}
    Fit -- No --> Leave
    Fit -- Yes --> Contact
    Interest -- Yes --> Case[Read case study]
    Case --> Enough{Enough to decide?}
    Enough -- No --> Work
    Enough -- Yes --> Contact[Use contact link]
    Contact --> Send[Send email]
    Send --> End([Message received])
```

## Why this matters for the layout

- The **hero** must answer "what does this person do, and for whom?" in one glance, because the first branch is where most visitors leave.
- Every case study needs a clear path back to the **contact link**. The decision loop returns to "Work" or "Contact", never to a dead end.
- The contact link appears in the header navigation, at the end of each case study, and in the footer.
