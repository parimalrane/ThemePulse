# TABELA FUTURE ROADMAP

## CORE IDENTITY

TABELA is a proprietary Institutional Capital Rotation Intelligence Engine.

TABELA is NOT:

* Stock scanner
* Trade signal generator
* Automated trading system

Primary objectives:

* Detect institutional capital accumulation
* Detect institutional capital rotation between themes
* Identify strongest themes for LONG opportunities
* Identify weakest themes for SHORT opportunities
* Build proprietary historical market intelligence database
* Learn recurring institutional behavior before future leaders emerge

Core philosophy:

* Capital Flow Detection First
* Market Structure First
* Stock Selection Second
* Historical Intelligence Compounds Over Time
* Price Action Leads Narrative
* Chart Review Always Mandatory

---

# CURRENT PRODUCTION STABLE MODULES

Core engine (protected):

* ETF ingestion engine
* Stock ingestion engine
* ETF ranking engine
* Theme engine
* Stock mapper engine
* Relative Strength engine
* Long scoring engine
* Short scoring engine
* Rotation engine

Historical layer (stable):

* Stock history engine
* Market snapshot engine
* Unknown emerging leaders engine

Optional intelligence layer:

* TradingView export engine

Protected modules:

* Long engine
* Short engine
* Historical logging architecture
* ETF ranking logic

---

# CURRENT ACTIVE PRIORITIES

## P0 — LIVE OBSERVATION PHASE (ACTIVE)

Run live market observation for 10–20 sessions.

Validate:

* Long output quality
* Short output quality
* Theme rotation stability
* Historical logging consistency
* Unknown emerging leaders quality

Rule:

No major scoring redesign during observation period.

Status:

ACTIVE

---

## P1 — THEME ARCHITECTURE REDESIGN (HIGHEST PRIORITY)

Problem:

Current theme architecture fragmented.

Current weaknesses:

* Hardcoded ticker mapping
* Multiple theme sources of truth
* Excessive theme fragmentation
* High maintenance burden

Goal:

Replace current theme architecture.

Target architecture:

config/

* company_theme_mapping.csv
* theme_rules.csv
* theme_taxonomy.csv

Objectives:

* Remove hardcoded theme dictionaries
* Simplify maintenance
* Weekly CSV updates only
* Eliminate multiple theme authority problem

Priority:

CRITICAL

---

## P2 — UNKNOWN CLASSIFICATION LEARNING LOOP

Current system implemented.

Purpose:

Identify unknown emerging leaders requiring classification.

Weekly workflow:

* Run Friday TABELA
* Review unknown_emerging_leaders.csv
* Update company_theme_mapping.csv

Goal:

Allow TABELA classification database to improve continuously from market behavior.

Priority:

ACTIVE

Status:

IMPLEMENTED

---

## P3 — THEME TAXONOMY RESTRUCTURE

Current issue:

Themes are over fragmented.

Example:

Current:

* AI Accelerators
* AI ASIC
* AI Sensors
* AI Connectivity

Future:

Macro Theme:

Artificial Intelligence

Sub Themes:

* AI Infrastructure
* AI Compute
* AI Networking

Goal:

Track capital rotation at institutional level.

Not micro categories.

Priority:

HIGH

---

## P4 — THEME NORMALIZATION ENGINE

Current issue:

Theme inconsistency exists.

Example:

* Natural Gas
* natural gas

Problem:

Historical intelligence corruption.

Goal:

Single canonical theme naming system.

Priority:

HIGH

---

## P5 — ARCHITECTURE CLEANUP

Current issue:

main.py becoming orchestration bottleneck.

Future architecture:

* main.py
* core_pipeline.py
* logging_pipeline.py
* reporting_pipeline.py

Rule:

Optional modules must never break core engine.

Priority:

HIGH

Status:

DEFERRED

---

## P6 — SCORING ENGINE REVIEW

Current objective:

Audit scoring logic.

Review:

* RS weighting
* Theme weighting
* Sales Growth weighting
* Margin weighting
* Zacks weighting

Question:

Are fundamentals overweighted?

Principle:

Price leads analyst opinion.

Priority:

HIGH

---

## P7 — SHORT ENGINE REVIEW

Current objective:

Review short side logic.

Important principle:

Weakness does NOT automatically imply short opportunity.

Review:

* Institutional distribution behavior
* Structural weakness behavior
* Short score thresholds
* Theme weakness relationships

Priority:

HIGH

---

# HISTORICAL INTELLIGENCE LAYER (FUTURE)

Important rule:

Core system must always function without history.

History improves intelligence.

History never becomes runtime dependency.

---

## P8 — ROTATION INTELLIGENCE ENGINE

Purpose:

Track capital movement over time.

Examples:

* Themes accelerating
* Themes weakening
* Themes entering leadership
* Themes exiting leadership

Example output:

Semiconductors strengthening 5 sessions

Software weakening 3 sessions

Defense entering emerging status

Priority:

VERY HIGH

---

## P9 — THEME BREADTH EXPANSION ENGINE

Goal:

Measure internal participation inside themes.

Metrics:

* Stock count inside theme
* Strong stock count
* Breadth expansion trend
* Breadth deterioration trend

Questions:

* Is leadership broadening?
* Is theme participation shrinking?

Priority:

VERY HIGH

---

## P10 — LEADERSHIP DETERIORATION ENGINE

Goal:

Track strong stocks losing leadership quality.

Signals:

* RS deterioration
* Long score deterioration
* Leadership disappearance
* Theme deterioration

Purpose:

Detect institutional distribution behavior.

Requires history.

Priority:

VERY HIGH

---

## P11 — RELATIVE STRENGTH DECAY ENGINE

Goal:

Track gradual RS weakening.

Example:

96 → 91 → 84 → 73 → 61

Signals:

* Institutional exit
* Distribution
* Momentum deterioration

Requires history.

Priority:

VERY HIGH

---

## P12 — INTERNAL ROTATION ENGINE

Goal:

Detect divergence inside strong themes.

Example:

Semiconductors strong.

NVDA strong.

MU strong.

AMD weak.

Interpretation:

Capital rotating internally.

Priority:

HIGH

---

## P13 — QUIET ACCUMULATION ENGINE

Goal:

Detect silent institutional accumulation before obvious breakout.

Requires:

Historical pattern database.

Priority:

EXTREMELY HIGH

---

## P14 — PRE BREAKOUT FINGERPRINT ENGINE

Study historical winners.

Examples:

* NVDA
* PLTR
* ARM
* APP

Question:

What recurring behavior occurs before explosive moves?

Priority:

MAXIMUM

---

## P15 — MARKET REGIME ENGINE

Classify market environment.

Possible regimes:

* Broad bull market
* Narrow leadership market
* Defensive rotation
* Commodity cycle
* Risk off environment
* AI supercycle

Priority:

HIGH

---

## P16 — HISTORICAL INTELLIGENCE ENGINE

Final intelligence brain.

Learn recurring patterns:

* Institutional accumulation
* Institutional distribution
* Theme persistence
* Leadership deterioration
* Rotation sequences

Ultimate objective:

Understand institutional behavior before market recognizes it.

Priority:

ULTIMATE DESTINATION

---

# REMOVED PERMANENTLY

Deleted future ideas:

* Persistence Engine
* Behavioral Anomaly Engine V1
* Behavioral Anomaly Engine V2
* Composite Velocity Engine
* Historical Intelligence Engine V0

Reason:

Insufficient data support or obsolete architecture.

---

# PERMANENT ENGINEERING RULES

Rule 1

TABELA never generates trade signals.

Rule 2

Chart review always mandatory.

Rule 3

Core engine must work without history.

Rule 4

History improves intelligence but never becomes dependency.

Rule 5

Engine files contain logic.

Config files contain assumptions.

Rule 6

Remove hard coding whenever possible.

Rule 7

Weekly maintenance maximum 30 minutes.

Rule 8

Monthly review includes:

* Theme taxonomy review
* Scoring weight review
* Hard coding audit
* Unknown classification review

Rule 9

Recent market behavior has higher authority than old behavior.

Rule 10

Data capability defines intelligence capability.

Rule 11

Never force advanced intelligence unsupported by available data.

Rule 12

Institutional capital flow detection always has highest priority.
