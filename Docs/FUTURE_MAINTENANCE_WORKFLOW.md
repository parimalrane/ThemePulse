# TABELA MASTER ROADMAP (UPDATED)

## CORE IDENTITY

TABELA is an Institutional Capital Rotation Intelligence Engine.

TABELA is NOT a stock scanner.

Primary purpose:

* Detect institutional capital flow
* Identify strongest themes for LONG trades
* Identify weakest themes for SHORT trades
* Track capital rotation between themes over time
* Build long-term institutional market intelligence database
* Learn institutional behavior before future leaders become obvious

Core philosophy:

Capital Rotation Detection First
Stock Selection Second
Historical Intelligence Compounds Over Time

---

# CURRENT STABLE ARCHITECTURE

Production stable modules:

* ETF ingestion engine
* Stock ingestion engine
* ETF signal quality filter
* Theme classification engine
* Relative Strength engine
* Composite scoring engine
* Long candidate engine
* Short candidate engine
* TradingView export engine
* Daily snapshot history engine
* Rotation Delta Report
* Stock History Engine

Protected modules:

* Long Engine
* Snapshot Architecture
* Historical Logs

Current phase:

P0 Observation Phase

Rule:

No unnecessary architecture modifications.

---

# TIER 1 PRIORITIES (CORE SYSTEM QUALITY)

## P0 — LIVE OBSERVATION PHASE

Observe 5–10 live market sessions.

Focus:

* Theme persistence
* Long candidate stability
* Short candidate quality
* Rotation behavior consistency
* Unexpected ranking anomalies

Rules:

No architecture redesign.

Status:

ACTIVE

---

## P1 — THEME CLASSIFICATION EXPANSION

Objective:

Reduce Unknown stock classification.

Goals:

* Better ETF mapping
* Reduce unclassified leaders
* Improve theme coverage

Priority:

HIGH

Status:

Pending

---

## P2 — THEME STABILITY VALIDATION ENGINE

Objective:

Measure trustworthiness of theme movement.

Questions:

* Is theme leadership persistent?
* Is weakness structural?
* Is movement temporary noise?

Metrics:

* Days in leadership
* Leadership persistence score
* Theme stability score

Priority:

HIGH

Status:

Pending

---

## P3 — SHORT ENGINE QUALITY REVIEW

Objective:

Improve weakest theme short reliability.

Research:

* Temporary weakness vs structural weakness
* Mean reversion contamination
* False weakness detection

Priority:

HIGH

Status:

Pending

---

# TIER 2 PRIORITIES (DATA INTELLIGENCE LAYER)

## P4 — STOCK EVOLUTION HISTORY ENGINE

Objective:

Store daily full stock universe history.

Purpose:

Track how stocks evolve before becoming leaders.

Store:

* Ticker
* Last Close
* Avg Volume
* 52 Week High
* 52 Week Low
* Price Position in 52 Week Range
* Theme
* Theme Class
* RS Rating
* Composite Score
* Sales Score
* Zacks Score

Rules:

Overwrite same day.

Purpose:

Historical research foundation.

Priority:

VERY HIGH

Status:

Active

---

## P5 — THEME INTERNAL BREADTH ENGINE

Objective:

Measure internal strength of themes.

Example:

Semiconductors

Day 1 → 4 strong stocks
Day 5 → 9 strong stocks
Day 12 → 17 strong stocks

Questions:

* Is theme strengthening internally?
* Is breadth expanding before ETF moves?

Metrics:

* Strong stock count by theme
* Average composite score by theme
* Breadth expansion trend

Purpose:

Detect institutional accumulation inside themes.

Priority:

EXTREMELY HIGH

Status:

Future

---

## P6 — COMPOSITE SCORE VELOCITY ENGINE

Objective:

Measure speed of stock strengthening.

Example:

ARM

58 → 62 → 69 → 78 → 88

Questions:

* Which stocks strengthen fastest?
* Which stocks weaken fastest?

Metrics:

* 5 day score change
* 10 day score change
* Score acceleration

Priority:

VERY HIGH

Status:

Future

---

# TIER 3 PRIORITIES (INSTITUTIONAL BEHAVIOR RESEARCH)

## P7 — QUIET ACCUMULATION ENGINE

Objective:

Detect silent institutional accumulation.

Pattern:

RS steadily improving over multiple sessions without entering top leaders.

Example:

72 → 76 → 81 → 89 → 94

Questions:

* Which stocks strengthen quietly before breakout?

Priority:

EXTREMELY HIGH

Status:

Future

---

## P8 — FIRST APPEARANCE ENGINE

Objective:

Track when stocks first enter institutional leadership.

Example:

Day 1 → Rank 42
Day 4 → Rank 16
Day 7 → Rank 4

Questions:

* Which stocks are fresh leaders?
* Which stocks are entering leadership for first time?

Metrics:

* First appearance date
* Rank progression
* Days since appearance

Priority:

HIGH

Status:

Future

---

## P9 — INSTITUTIONAL DISTRIBUTION ENGINE

Objective:

Detect when institutions begin exiting strong stocks.

Example:

NVDA

98 → 95 → 91 → 84 → 76

Question:

* Is institutional conviction deteriorating while stock still looks strong?

Purpose:

Detect future laggards early.

Priority:

EXTREMELY HIGH

Status:

Future

---

## P10 — FAILED LEADER ENGINE

Objective:

Study how strong leaders fail.

Questions:

* What happens before strong leaders disappear?
* Does theme weaken first?
* Does score collapse gradually or suddenly?

Purpose:

Avoid late entries.

Priority:

HIGH

Status:

Future

---

# TIER 4 PRIORITIES (BREAKOUT DISCOVERY RESEARCH)

## P11 — PRE BREAKOUT FINGERPRINT ENGINE

Objective:

Learn what happens before explosive moves.

Research candidates:

* ARM
* NVDA
* PLTR
* CRDO
* APP

Questions:

What changes happened 10–20 days before breakout?

Possible signals:

* Composite rising continuously
* RS above 90
* Price near 52 week high
* Theme entering leadership
* First appearance in top longs

Goal:

Detect tomorrow’s explosive winners.

Priority:

EXTREMELY HIGH

Status:

Long term research

---

## P12 — EMERGING MONSTER DETECTOR

Objective:

Detect future explosive winners before market recognizes them.

Example:

54 → 61 → 68 → 76 → 84 → 92 → breakout

Focus:

Second derivative.

Not score.

Acceleration of score.

Need:

* Rate of score acceleration
* Persistent acceleration pattern

Purpose:

Find future market leaders early.

Priority:

MAXIMUM

Status:

Long term research

---

## P13 — FALSE BREAKOUT PREDICTOR

Objective:

Distinguish successful breakouts from failed breakouts.

Question:

Why do some leaders become explosive winners while others fail?

Compare:

Successful breakout patterns vs failed breakout patterns.

Purpose:

Avoid weak breakouts.

Priority:

HIGH

Status:

Future

---

# TIER 5 PRIORITIES (MARKET STRUCTURE INTELLIGENCE)

## P14 — ETF LEADERSHIP PREDICTIVE ENGINE

Objective:

Detect ETF leadership before ETF ranking changes.

Theory:

Stocks inside theme strengthen first.

ETF strength follows later.

Questions:

Can stock behavior predict ETF movement before ETF ranks improve?

Priority:

VERY HIGH

Status:

Future

---

## P15 — ROTATION SPEED ENGINE

Objective:

Measure how fast institutional capital rotates.

Example:

AI leadership duration = 41 days
Gold miners = 8 days
Semiconductors = 55 days

Metric:

Theme Half Life

Purpose:

Learn which themes sustain leadership longest.

Priority:

MEDIUM

Status:

Future

---

## P16 — MARKET REGIME PREDICTOR

Objective:

Detect risk-on vs risk-off transitions.

Possible warning signs:

* Leadership narrows
* Weak themes expand
* Composite averages fall
* Fewer strong themes

Purpose:

Detect structural market changes early.

Priority:

HIGH

Status:

Future

---

# FINAL LONG TERM ENGINE

## P17 — HISTORICAL INSTITUTIONAL INTELLIGENCE ENGINE

Objective:

Build long term proprietary market intelligence database.

Questions:

* Which themes repeatedly lead?
* Which sectors repeatedly weaken?
* What patterns repeat before future winners emerge?
* What behavior appears before institutions accumulate aggressively?

Purpose:

Long term institutional pattern recognition.

This becomes the intelligence brain of TABELA.

Priority:

ULTIMATE DESTINATION

Status:

Delayed until enough historical data exists

---

# ENGINEERING RULES

Never redesign architecture casually.

Historical logs are sacred.

Recent behavior always carries more weight than old behavior.

Long Engine is protected.

Snapshot JSON stores raw market state only.

Rotation Delta remains diagnostic only.

Automation first.

No manual logging.

Protect simplicity.

Avoid feature creep.

Observe before optimizing.

Capital rotation detection first.

Stock selection second.

---

# LONG TERM VISION

Current TABELA

Institutional Capital Rotation Engine

Future TABELA

Institutional Market Intelligence Platform

Ultimate capability

Learn what institutions do BEFORE explosive leaders emerge.

Final goal

Detect future market leaders before the crowd notices.
