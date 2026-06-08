# BPO QA Scorecard Tool

A command-line tool that uses the Claude API to evaluate customer support transcripts against a structured QA audit framework. Built by a Senior Operations Manager to automate the manual transcript review process used in BPO and contact center environments.

---

## The Problem

In a typical BPO or contact center operation, a QA team manually reviews 60–70 support transcripts per week. Each review requires an analyst to read the full transcript, score it across multiple audit categories, write coaching notes, and log the results — a process that takes 15–20 minutes per transcript and introduces scoring inconsistency across reviewers.

At scale, this creates three real operational problems:

- **Coverage gaps** — with limited analyst hours, only a fraction of interactions get reviewed
- **Calibration drift** — different analysts score the same behaviors differently over time
- **Delayed feedback** — agents may not receive coaching until days after the interaction occurred

This tool addresses all three by automating the initial scoring pass, giving QA analysts a structured starting point they can review, adjust, and act on immediately.

---

## What It Does

- Accepts any customer support transcript as input (paste directly into the terminal)
- Evaluates the transcript across five QA audit categories
- Returns a scored report with pass/fail status, specific highlights, and coaching flags
- Saves output as both a formatted `.txt` report and a structured `.json` file for logging or downstream use

---

## QA Audit Categories

These categories are modeled on the audit guidelines used in real BPO QA calibration sessions:

| Category | What It Measures |
|---|---|
| **Greeting and Opening** | Professional introduction, warm acknowledgment, tone-setting |
| **Understanding the Issue** | Clarifying questions, demonstrated comprehension, avoiding repeat explanations |
| **Resolution Quality** | Accuracy and clarity of resolution, expectation-setting if unresolved |
| **Empathy and Tone** | Acknowledgment of frustration or urgency, avoidance of robotic language |
| **Compliance and Process** | Verification steps, appropriate escalation, proper close |

Each category is scored 0–10. An overall score of 7.0 or above returns a **PASS**. Below 7.0 returns a **FAIL**.

---

## Sample Output

```
=======================================================
  BPO QA SCORECARD
  Transcript: ticket-0002
  Evaluated:  2026-06-08 14:36
=======================================================
SCORES
-----------------------------------
  Greeting And Opening         █████████░ 9/10
  Understanding The Issue      █████████░ 9/10
  Resolution Quality           ██████████ 10/10
  Empathy And Tone             ██████████ 10/10
  Compliance And Process       █████████░ 9/10

  OVERALL SCORE:  9.4/10
  RESULT:         PASS

HIGHLIGHTS
-----------------------------------
  + Excellent empathy - immediately validated the customer's frustration about the 3-day wait
  + Efficient resolution with real-time verification by having customer test login while on the call

COACHING FLAGS
-----------------------------------
  ! Could have briefly explained what caused the verification flag to help customer understand the issue
  ! Consider offering a callback number or direct escalation path in case future issues arise

SUMMARY
-----------------------------------
  Marcus delivered an exemplary support interaction. He acknowledged the customer's frustration
  genuinely, resolved the account access issue quickly and efficiently, and added proactive value
  by documenting the account history. The call was professional, empathetic, and well-structured
  from start to finish.
=======================================================
```

---

## Setup

**Requirements**
- Python 3.8+
- An Anthropic API key ([get one here](https://console.anthropic.com))

**Installation**

Clone the repository:
```bash
git clone https://github.com/josephmccallister/qa-scorecard-tool.git
cd qa-scorecard-tool
```

Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

Install dependencies:
```bash
pip install anthropic python-dotenv
```

Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your-api-key-here
```

---

## Usage

```bash
python scorecard.py
```

When prompted, paste your transcript and type `END` on a new line when finished. Enter a name for the transcript (e.g. a ticket number) and the tool will score it and save the output to the `/output` folder.

---

## Output Files

Each run saves two files to the `/output` directory:

- `{transcript-name}_{timestamp}.txt` — formatted scorecard for human review
- `{transcript-name}_{timestamp}.json` — structured data for logging, reporting, or integration

The JSON output is designed to support downstream use cases such as loading results into a spreadsheet tracker, aggregating scores by agent or team, or feeding into a QA dashboard.

---

## Why JSON Output Matters

Most QA tools stop at the report. This tool also produces structured JSON so that scoring data can be aggregated over time — tracking agent performance trends, identifying recurring coaching flags across a team, or flagging systemic process gaps that show up repeatedly across transcripts.

---

## Roadmap

Planned enhancements for future versions:

- **Configurable rubric loader** — define custom audit categories via a config file without editing code
- **Batch processing** — score a folder of transcript files in a single run
- **Agent performance tracker** — aggregate scores by agent name across multiple transcripts
- **CSV export** — output a summary row per transcript for easy spreadsheet import

---

## About

Built by **Joseph McCallay**, Senior Operations Manager with experience leading BPO vendor management, contact center operations, and QA program development in SaaS environments.

[LinkedIn](https://www.linkedin.com/in/joseph-mccallay-850369b7/) · [GitHub](https://github.com/jamccallay)