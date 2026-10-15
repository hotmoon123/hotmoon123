# Research sources and provenance

Reviewed/rechecked during this conversation, including the v0.2 work on 8 October 2026. These references support specific decisions; they are not endorsements of StitchLedger, proof of demand, or certificates of compliance.

## Requirements and lifecycle

**IEEE/ISO/IEC 29148-2018** — official IEEE catalogue description. The public page identifies an active requirements-engineering standard covering requirements processes/products and characteristics. We reviewed the public description, not the complete purchased standard. Used to motivate identifiable requirements, acceptance criteria and traceability. https://standards.ieee.org/ieee/29148/6937/

**NIST SSDF** — official project page describes SP 800-218 / SSDF 1.1 and secure-development practices. Used to structure security requirements, provenance and verification throughout delivery. This is reference-informed practice, not a completed SSDF assessment. [1](https://csrc.nist.gov/projects/ssdf)

## Security and accessibility

**OWASP ASVS** — official project overview describes the basis for verifying web application technical security controls, and references versioned requirement IDs. Used as the planned web/API verification reference; a complete ASVS checklist has not been executed. https://owasp.org/projects/asvs

**OWASP MASVS** — official control groups cover storage, cryptography, authentication, network, platform, code, resilience and privacy. Used to define native-mobile review areas; do not apply obsolete level claims from older uploaded summaries or claim a completed MASVS audit. [1](https://mas.owasp.org/MASVS/)

**W3C WCAG 2.2** — official recommendation, relevant to web content including mobile devices. Used as the intended web accessibility baseline. Only selected overview material was reviewed here; success-criterion-by-success-criterion conformance, native VoiceOver and TalkBack testing remain outstanding. https://www.w3.org/TR/WCAG22/

## University methods

**Stanford d.school, Design Thinking Bootleg** — the official resource describes Empathize, Define, Ideate, Prototype and Test as modes and presents tools/methods, not a guarantee that mechanically following stages yields a successful business. Used to structure the proposed user-research and iteration plan. [1](https://dschool.stanford.edu/tools/design-thinking-bootleg)

**Carnegie Mellon SEI, ATAM collection** — describes architectural evaluation against quality-attribute goals and the trade-offs between them. Used to motivate explicit security, modifiability, availability and simplicity trade-offs. No formal staffed ATAM evaluation was conducted. [1](https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/)

## Platform/build documentation

**Expo EAS Build** — official documentation describes cloud/local builds and Android/Linux versus iOS/macOS workers. Used to explain what can be initiated from Kali and what still requires platform build/signing infrastructure. [1](https://docs.expo.dev/build/introduction/)

**Expo development-build configuration** — official tutorial explains owner authentication, project linking and build configuration. Used in the native setup runbook; no owner account was created or linked. [2](https://docs.expo.dev/tutorial/eas/configure-development-build/)

The actual installed dependency graph was checked using Expo's compatibility check, TypeScript, web export, native JavaScript exports and package audits. The npm advisory report remains unresolved and is included verbatim.

## Market context and competition (initial research, not a field study)

**Ghana Statistical Service, 2024 IBES factsheet** — reports establishment counts and firm characteristics, including a predominance of micro establishments. This is broad context, not an estimate of paying tailoring studios. [5](https://statsghana.gov.gh/gssmain/fileUpload/pressrelease/factsheet.pdf)

**ReFinD/ISSER with GSS, digital-payments research** — describes firm-level digital-payment adoption and findings from IBES. Used only as context, not causal evidence that StitchLedger improves revenue. [2](https://refind-isser.ug.edu.gh/media/5/download)

**Oze official business-app page** — describes an existing competitor's bookkeeping, inventory, invoices and payment-reminder features, with free/paid offerings. It demonstrates existing alternatives, not a tailoring-specific gap or our willingness-to-pay evidence. [2](https://getoze.com/business-app/)

## Ghana privacy obligations

**Ghana Data Protection Commission, registration guidance** — official regulator guidance says entities processing personal data must register and discusses restrictions on unregistered controllers. Confirm the operator's exact circumstances, controller/processor roles, registration and current obligations before collecting real data; this document is not legal advice. [2](https://dataprotection.org.gh/registration/)

The statutory context does not prove all product-specific legal obligations have been identified. Hosting location, customer location, store/payment services and actual data processing can introduce further obligations.

## Internal evidence and boundaries

- User-uploaded library: reusable preferences, analytical structures and draft frameworks; not independent proof of every factual assertion.
- v0.1 research/specification: retained context, superseded where current implementation differs.
- v0.2 source/tests: evidence of the behaviors actually exercised.
- No customer interviews, representative usability study, paid pilot, independent penetration test, legal opinion, signed native build, store review or live AI-provider validation was completed.

Where no evidence exists, the documents explicitly use “hypothesis,” “proposed,” “target,” “not tested,” or “not implemented.”
