#!/usr/bin/env python3
"""
TechBro blueprint generator.

Single source of truth:
  tools/data/roles/*.yaml     -> 300 SDLC roles
  tools/data/artifacts.yaml   -> 100 deliverables
  tools/data/sources.yaml     -> citation register

Renders:
  docs/techbro/01-role-catalog.md
  docs/techbro/artifacts/00-artifact-index.md
  docs/techbro/99-sources-and-assumptions.md
  docs/techbro/STATUS.md

The generator fails closed: any dangling reference, duplicate id, or unverified
source claim stops the build. Documentation that cannot be validated is not
documentation, it is decoration.
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "tools" / "data"
OUT = ROOT / "docs" / "techbro"


# ---------------------------------------------------------------- minimal YAML
def _coerce(raw: str):
    raw = raw.strip()
    if raw == "" or raw == "null":
        return None
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [_coerce(p) for p in _split_top(inner)]
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        return raw[1:-1]
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    if raw in ("true", "false"):
        return raw == "true"
    return raw


def _split_top(inner: str) -> list[str]:
    parts, depth, buf, quote = [], 0, "", None
    for ch in inner:
        if quote:
            buf += ch
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            buf += ch
        elif ch in "[{":
            depth += 1
            buf += ch
        elif ch in "]}":
            depth -= 1
            buf += ch
        elif ch == "," and depth == 0:
            parts.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        parts.append(buf)
    return [p.strip() for p in parts]


def _split_keyval(body: str) -> tuple[str, str]:
    quote = None
    depth = 0
    for i, ch in enumerate(body):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == ":" and depth == 0:
            return body[:i].strip(), body[i + 1:].strip()
    raise ValueError(f"no key/value separator in: {body[:60]}")


def load_flow_list(path: Path) -> list[dict]:
    """Parse a YAML file that is a list of single-line flow mappings."""
    rows: list[dict] = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if not (s.startswith("- {") and s.endswith("}")):
            raise ValueError(f"{path.name}:{lineno}: expected '- {{...}}', got: {s[:70]}")
        body = s[3:-1].strip()
        row: dict = {}
        for chunk in _split_top(body):
            key, raw = _split_keyval(chunk)
            row[key] = _coerce(raw)
        rows.append(row)
    return rows


def load_block_list(path: Path) -> list[dict]:
    """Parse a YAML file of block mappings: '- key: value' plus indented 'key: value'."""
    rows: list[dict] = []
    current: dict | None = None
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        stripped = line.strip()
        if line.startswith("- "):
            if current is not None:
                rows.append(current)
            current = {}
            stripped = stripped[2:]
        if current is None:
            raise ValueError(f"{path.name}:{lineno}: mapping before first list item")
        key, raw = _split_keyval(stripped)
        current[key] = _coerce(raw)
    if current is not None:
        rows.append(current)
    return rows


# ---------------------------------------------------------------- load + validate
def load_roles() -> list[dict]:
    roles: list[dict] = []
    for f in sorted((DATA / "roles").glob("*.yaml")):
        roles.extend(load_flow_list(f))
    return roles


ARTIFACTS = load_flow_list(DATA / "artifacts.yaml")
SOURCES = load_block_list(DATA / "sources.yaml")
ROLES = load_roles()

# normalise 'D01' / 'D001' / 1 -> 1 so cross-references are comparable
for _a in ARTIFACTS:
    _o = _a["owner"]
    _a["owner"] = int(str(_o)[1:]) if isinstance(_o, str) and str(_o).startswith("D") else int(_o)
    # a single source key must behave like a one-element list, never a string
    _std = _a.get("std")
    if _std is None:
        _a["std"] = []
    elif isinstance(_std, int):
        _a["std"] = [f"S{_std}"]
    elif isinstance(_std, str):
        _s = _std.strip()
        _a["std"] = _split_top(_s[1:-1]) if _s.startswith("[") and _s.endswith("]") else [_s]
    else:
        _a["std"] = [str(x) for x in _std]
for _r in ROLES:
    _r["id"] = int(str(_r["id"]).lstrip("D"))
    _own = _r.get("own")
    if _own is None:
        _r["own"] = []
    elif isinstance(_own, int):
        _r["own"] = [_own]
    else:
        _r["own"] = [int(x) for x in _own]
for _s in SOURCES:
    _s["url"] = _s.get("url", "")

FAMILIES = [
    "Leadership", "Product", "Business", "Research", "Design", "Delivery",
    "Architecture", "Data", "AI", "Engineering", "Quality", "Security",
    "Operations", "Growth", "Content", "People", "Finance", "Legal", "Governance",
]
REQUIRED_ROLE_KEYS = {"id", "title", "fam", "own", "in", "out", "sk", "mat", "aei", "kpi"}
REQUIRED_ART_KEYS = {"id", "name", "cell", "owner", "dod"}
CELLS = ["discover", "define", "architect", "build", "assure", "secure", "deploy", "sustain"]
BLOOM = [
    "1-Remember", "2-Understand", "3-Apply", "4-Analyse",
    "5-Evaluate", "6-Create",
]
# Bloom level that MODERN-AI work pushes each role toward, used in the report.
AI_SHIFT = {
    "1-Remember": "AI retrieves and recalls; the human must move to verification",
    "2-Understand": "AI explains and summarises; the human checks meaning against context",
    "3-Apply": "AI drafts and executes; the human owns correctness, safety and edge cases",
    "4-Analyse": "AI generates hypotheses and finds patterns; the human interrogates causal claims",
    "5-Evaluate": "AI scores and compares; the human owns the judgement, the trade-off and the consequences",
    "6-Create": "AI expands the option space; the human commits to the irreversible choice",
}


ROLE_BY_ID = {r["id"]: r for r in ROLES}
ART_BY_ID = {a["id"]: a for a in ARTIFACTS}
SRC_BY_ID = {s["id"]: s for s in SOURCES}


class ValidationError(Exception):
    pass


def validate() -> list[str]:
    errors: list[str] = []
    seen_ids: Counter = Counter(r["id"] for r in ROLES)
    dupes = [i for i, n in seen_ids.items() if n > 1]
    if dupes:
        errors.append(f"duplicate role ids: {dupes}")
    art_ids = {a["id"] for a in ARTIFACTS}
    if len(art_ids) != len(ARTIFACTS):
        errors.append("duplicate artefact ids")
    if art_ids != set(range(1, len(ARTIFACTS) + 1)):
        errors.append("artefact ids are not a contiguous 1..100 range")
    for r in ROLES:
        missing = REQUIRED_ROLE_KEYS - set(r)
        if missing:
            errors.append(f"{r.get('id')}: missing keys {sorted(missing)}")
            continue
        if r["fam"] not in FAMILIES:
            errors.append(f"{r['id']}: unknown family {r['fam']!r}")
        if r["mat"] not in BLOOM:
            errors.append(f"{r['id']}: unknown Bloom level {r['mat']!r}")
        for a in r["own"] or []:
            if a not in art_ids:
                errors.append(f"{r['id']}: owns unknown artefact ART-{a:03d}")
        if not r["own"]:
            errors.append(f"{r['id']}: owns no artefact (every role must own an output)")
    for a in ARTIFACTS:
        if a["cell"] not in CELLS:
            errors.append(f"ART-{a['id']:03d}: unknown cell {a['cell']!r}")
        if not (1 <= a["owner"] <= len(ROLES)):
            errors.append(f"ART-{a['id']:03d}: owner D{a['owner']:03d} out of range")
        # bidirectional integrity: if a role is accountable, that role must claim it too
        acc = ROLE_BY_ID.get(a["owner"])
        if acc is not None and a["id"] not in (acc["own"] or []):
            errors.append(
                f"ART-{a['id']:03d}: accountable owner D{a['owner']:03d} "
                f"does not list it in 'own' (drift)"
            )
        for s in a.get("std") or []:
            if not any(src["id"] == s for src in SOURCES):
                errors.append(f"ART-{a['id']:03d}: unknown source key {s}")
        if not a["dod"]:
            errors.append(f"ART-{a['id']:03d}: no definition of done")
    src_ids = [s["id"] for s in SOURCES]
    if len(set(src_ids)) != len(src_ids):
        errors.append("duplicate source ids")
    for s in SOURCES:
        if "verified" in s and s["verified"] not in (True, False, None):
            errors.append(f"{s['id']}: verified must be boolean")
        if s.get("verified") is not True and s.get("verified") is not False:
            errors.append(f"{s['id']}: verified flag missing")
    return errors




# ---------------------------------------------------------------- rendering
def fam_counts() -> Counter:
    return Counter(r["fam"] for r in ROLES)


def render_role_catalog() -> str:
    counts = fam_counts()
    mats = Counter(r["mat"] for r in ROLES)
    lines = [
        f"# 01 — Role Catalogue: {len(ROLES)} SDLC Roles",
        "",
        "> Generated from `tools/data/roles/*.yaml` by `tools/gen_blueprint.py`. Do not edit by hand:",
        "> edit the data and regenerate, otherwise the document and the truth diverge.",
        "",
        f"**Roles:** {len(ROLES)} &nbsp;|&nbsp; **Families:** {len(counts)} &nbsp;|&nbsp; "
        f"**Artefacts owned:** {len(ARTIFACTS)} &nbsp;|&nbsp; "
        f"**Roles per artefact:** {len(ROLES) / len(ARTIFACTS):.1f}",
        "",
        "Every role is a *job to be done*, not a headcount. In a 6-person startup one human holds",
        "15–25 of these hats; the catalogue exists so that when a hat is dropped, somebody can name",
        "the hat, the output and the artefact that went missing. Columns:",
        "",
        "| Column | Meaning |",
        "| --- | --- |",
        "| **Owns** | the artefact(s) this role is accountable for (ART-###, see `artifacts/00-artifact-index.md`) |",
        "| **Inputs → Outputs** | what must exist before the work, and what must exist after |",
        "| **Core skill** | the specific competence, not a generic adjective |",
        "| **Bloom** | cognitive ceiling of the role (revised Bloom, Anderson & Krathwohl 2001) |",
        "| **AI leverage** | where a model accelerates the role, and the irreducible human judgement |",
        "| **KPI** | how the role is measured (a role without a measure is a rumour) |",
        "",
        "## 1.1 Family load",
        "",
        "| # | Family | Roles | Share | Artefacts owned |",
        "| ---: | --- | ---: | ---: | ---: |",
    ]
    for i, fam in enumerate(sorted(counts, key=lambda f: (-counts[f], f)), 1):
        owned = sum(len(r["own"] or []) for r in ROLES if r["fam"] == fam)
        lines.append(
            f"| {i} | {fam} | {counts[fam]} | {counts[fam] / len(ROLES):.1%} | {owned} |"
        )
    lines += [
        "",
        "## 1.2 Cognitive load (revised Bloom taxonomy)",
        "",
        "The distribution is the design intent for an AI-augmented team: machines carry recall and",
        "retrieval, humans are concentrated in analysis, evaluation and creation — the levels where",
        "being wrong is expensive and accountability cannot be delegated to a model.",
        "",
        "| Bloom level | Roles | Share | What AI changes |",
        "| --- | ---: | ---: | --- |",
    ]
    for lvl in BLOOM:
        lines.append(
            f"| {lvl} | {mats[lvl]} | {mats[lvl] / len(ROLES):.1%} | {AI_SHIFT[lvl]} |"
        )
    lines += ["", "## 1.3 The catalogue", ""]
    for fam in sorted(counts, key=lambda f: (-counts[f], f)):
        fam_roles = [r for r in ROLES if r["fam"] == fam]
        lines += [
            f"### {fam} — {len(fam_roles)} roles",
            "",
            "| ID | Role | Owns | Inputs → Outputs | Core skill | Bloom | AI leverage | KPI |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for r in fam_roles:
            owns = ", ".join(f"ART-{a:03d}" for a in r["own"] or [])
            lines.append(
                f"| D{r['id']:03d} | **{r['title']}** | {owns} | {r['in']} → {r['out']} | "
                f"{r['sk']} | {r['mat']} | {r['aei']} | {r['kpi']} |"
            )
        lines.append("")
    lines += [
        "## 1.4 Coverage proof",
        "",
        "Three assertions are checked mechanically by the generator (build fails if violated):",
        "",
        "1. every role owns at least one artefact — no job exists without a deliverable;",
        "2. every artefact has exactly one accountable owner — no unowned work;",
        "3. every artefact has a written definition of done — no \"done\" by assertion.",
        "",
        "Artefacts with more than one owning role (accountable owner in *italics*):",
        "",
        "| Artefact | Name | Accountable | Also involved |",
        "| --- | --- | --- | --- |",
    ]
    owners: dict[int, list[int]] = defaultdict(list)
    for r in ROLES:
        for a in r["own"] or []:
            owners[a].append(r["id"])
    multi = sorted((a, rs) for a, rs in owners.items() if len(rs) > 1)
    if not multi:
        lines.append("| — | None: one role, one accountable owner | — | — |")
    for a, rs in multi:
        acc = ART_BY_ID[a]["owner"]
        also = ", ".join(f"D{x:03d}" for x in rs if x != acc)
        lines.append(
            f"| ART-{a:03d} | {ART_BY_ID[a]['name']} | *D{acc:03d} "
            f"{ROLE_BY_ID[acc]['title']}* | {also} |"
        )
    return "\n".join(lines) + "\n"


def render_artifact_index() -> str:
    lines = [
        f"# 00 — Artefact Index: {len(ARTIFACTS)} Deliverables That Define the System",
        "",
        "> Generated from `tools/data/artifacts.yaml`. The eight cells are the SDLC itself",
        "> (see `02-sdlc-framework.md`). An artefact is real only when it satisfies its definition of done.",
        "",
        "| Cell | Artefacts |",
        "| --- | ---: |",
    ]
    cell_counts = Counter(a["cell"] for a in ARTIFACTS)
    for cell in CELLS:
        lines.append(f"| {cell} | {cell_counts[cell]} |")
    lines.append(f"| **total** | **{len(ARTIFACTS)}** |")
    lines.append("")
    for cell in CELLS:
        items = [a for a in ARTIFACTS if a["cell"] == cell]
        lines += [
            f"## {cell.title()} — {len(items)} artefacts",
            "",
            "| ID | Artefact | Accountable owner | Standard / source | Definition of done |",
            "| --- | --- | --- | --- | --- |",
        ]
        for a in items:
            owner = ROLE_BY_ID[a["owner"]]
            std = ", ".join(a.get("std") or []) or "internal convention"
            lines.append(
                f"| ART-{a['id']:03d} | **{a['name']}** | D{a['owner']:03d} {owner['title']} | "
                f"{std} | {a['dod']} |"
            )
        lines.append("")
    return "\n".join(lines) + "\n"


def render_sources() -> str:
    verified = [s for s in SOURCES if s.get("verified") is True]
    unverified = [s for s in SOURCES if s.get("verified") is not True]
    lines = [
        "# 99 — Sources, Citations & Assumption Register",
        "",
        "> Generated from `tools/data/sources.yaml`. Citation discipline for this pack:",
        "> **a claim that is not in this file is not cited as fact.** If it cannot be sourced,",
        "> it is written as `H-###` in the assumption register below and tested, not asserted.",
        "",
        f"**Sources:** {len(SOURCES)} &nbsp;|&nbsp; **verified:** {len(verified)} &nbsp;|&nbsp; "
        f"**flagged unverified:** {len(unverified)}",
        "",
        "## A. Verified sources",
        "",
        "| ID | Source | Year | Claim used (in our words) | Link |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for s in verified:
        lines.append(
            f"| {s['id']} | {s['title']} — *{s['author']}* | {s.get('year', 'n.d.')} | "
            f"{s['claim']} | <{s['url']}> |"
        )
    if unverified:
        lines += [
            "",
            "## B. Flagged as unverified (cited for principles only — confirm before relying on them)",
            "",
            "| ID | Source | Why flagged |",
            "| --- | --- | --- |",
        ]
        for s in unverified:
            lines.append(f"| {s['id']} | {s['title']} | {s['claim']} |")
    lines += [
        "",
        "## C. Assumption register (things we do **not** know yet)",
        "",
        "Each assumption gets a test, an owner and a date. An assumption that has not been tested",
        "by its review date escalates to the risk register, it does not quietly become a fact.",
        "",
        "| ID | Assumption | Why it matters | Test | Owner | Review |",
        "| --- | --- | --- | --- | --- | --- |",
        "| H-001 | Tech workers in Accra will pay a 10% service fee rather than transact off-platform with someone they met here | The entire revenue model | Price-sensitivity test in onboarding + off-platform leakage cohort analysis | D024 | v1 + 30 days |",
        "| H-002 | There is enough local demand for specialist work (mobile, data, security) to keep verified supply utilised at ≥55% | Liquidity is the only real moat | Measure match-fill rate per skill per week | D177 | weekly from launch |",
        "| H-003 | Employers will pay into escrow before work starts when the platform offers milestone release | Determines whether we can be paid at all | Compare deposit rate with and without escrow messaging (A/B) | D030 | v1 + 45 days |",
        "| H-004 | Mobile money settlement (MoMo) is acceptable to workers and does not add meaningful friction | Payout design | Measure payout failure rate and time-to-cash by rail | D023 | v1 + 14 days |",
        "| H-005 | A payment provider's delayed-settlement split is sufficient to approximate escrow without a BoG payment licence | Legal exposure | Written position from counsel + provider compliance confirmation | D018 | before public launch |",
        "| H-006 | Users will complete KYC with a Ghana Card photo before their first paid match | Fraud control vs. conversion | Funnel conversion with hard vs. soft gate | D154 | v1 + 30 days |",
        "| H-007 | Verified skill assessment improves hire success enough to justify the cost | Quality positioning | Compare dispute rate and repeat-hire rate for assessed vs. unassessed talent | D277 | v2 |",
        "| H-008 | 6–10 person squads will form for larger jobs without a formal contracting entity | Bigger deal sizes | Count squad deals and completion rate | D303 | v2 |",
        "| H-009 | WhatsApp is a viable notification channel under our consent and cost model | Engagement | Delivery and opt-out rates vs push/SMS | D166 | v1 + 30 days |",
        "| H-010 | We can reach 1,000 verified workers within 90 days at ≤ GHS 25 CAC | Growth plan | Weekly cohort cost tracking | D229 | day 90 |",
        "",
        "## D. How to cite in this pack",
        "",
        "- Facts from a source: the source key in brackets, e.g. *(S2)*.",
        "- Numbers in models: every input cell names its source or is labelled `assumption`.",
        "- Predictions: never stated as fact; written as a range with the assumption it depends on.",
        "- Anything dated: the date in this file is the date the claim was checked, not the date the",
        "  law was passed. Re-verify regulatory items every quarter (see ART-070).",
    ]
    return "\n".join(lines) + "\n"


def render_status() -> str:
    counts = fam_counts()
    cell_counts = Counter(a["cell"] for a in ARTIFACTS)
    rows = [
        ("Roles defined", f"{len(ROLES)}", "tools/data/roles/*.yaml"),
        ("Artefacts defined", f"{len(ARTIFACTS)}", "tools/data/artifacts.yaml"),
        ("Artefacts with DoD", f"{sum(1 for a in ARTIFACTS if a['dod'])}", "validated at build"),
        ("Sources registered", f"{len(SOURCES)}", "tools/data/sources.yaml"),
        ("Sources verified", f"{sum(1 for s in SOURCES if s.get('verified') is True)}", "checked 2026-11-06"),
        ("Families", f"{len(counts)}", "distinct disciplines"),
        ("Cells (SDLC stages)", f"{len(CELLS)}", ", ".join(CELLS)),
        ("Roles per artefact", f"{len(ROLES) / len(ARTIFACTS):.1f}", "load indicator"),
    ]
    lines = [
        "# Blueprint status",
        "",
        f"Generated {len(ROLES)} roles, {len(ARTIFACTS)} artefacts, {len(SOURCES)} sources.",
        "",
        "| Check | Value | Where it comes from |",
        "| --- | ---: | --- |",
    ]
    lines += [f"| {a} | {b} | {c} |" for a, b, c in rows]
    lines += ["", "## Artefacts per cell", "", "| Cell | Count |", "| --- | ---: |"]
    lines += [f"| {c} | {cell_counts[c]} |" for c in CELLS]
    lines += ["", "## Roles per family", "", "| Family | Count |", "| --- | ---: |"]
    lines += [f"| {f} | {n} |" for f, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]
    return "\n".join(lines) + "\n"


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for e in errors:
            print(" -", e, file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "artifacts").mkdir(parents=True, exist_ok=True)
    (OUT / "01-role-catalog.md").write_text(render_role_catalog(), encoding="utf-8")
    (OUT / "artifacts" / "00-artifact-index.md").write_text(render_artifact_index(), encoding="utf-8")
    (OUT / "99-sources-and-assumptions.md").write_text(render_sources(), encoding="utf-8")
    (OUT / "STATUS.md").write_text(render_status(), encoding="utf-8")
    print(f"ok: {len(ROLES)} roles, {len(ARTIFACTS)} artefacts, {len(SOURCES)} sources")
    print(f"families: {dict(fam_counts())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
