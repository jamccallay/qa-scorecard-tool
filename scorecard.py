import os
import json
from datetime import datetime
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

RUBRIC = """
You are a QA evaluator for a customer support contact center. Evaluate the following support transcript against this rubric and return ONLY a JSON object with no additional text.

RUBRIC CATEGORIES (each scored 0-10):

1. greeting_and_opening (0-10)
   - Agent introduced themselves professionally
   - Acknowledged the customer warmly
   - Set a helpful tone from the start

2. understanding_the_issue (0-10)
   - Asked clarifying questions when needed
   - Demonstrated they understood the customer's problem
   - Did not make the customer repeat themselves unnecessarily

3. resolution_quality (0-10)
   - Provided a clear, accurate resolution or next step
   - Stayed on topic and did not give irrelevant information
   - If unresolved, explained why and set clear expectations

4. empathy_and_tone (0-10)
   - Acknowledged customer frustration or urgency when present
   - Maintained a calm, professional, and human tone throughout
   - Avoided robotic or dismissive language

5. compliance_and_process (0-10)
   - Followed proper verification or escalation steps if applicable
   - Did not promise things outside their authority
   - Closed the interaction properly

RETURN THIS EXACT JSON STRUCTURE:
{
  "scores": {
    "greeting_and_opening": <score>,
    "understanding_the_issue": <score>,
    "resolution_quality": <score>,
    "empathy_and_tone": <score>,
    "compliance_and_process": <score>
  },
  "overall_score": <average of all scores, rounded to one decimal>,
  "pass_fail": "<PASS if overall >= 7.0, FAIL if below>",
  "highlights": ["<one thing the agent did well>", "<another strength if present>"],
  "flags": ["<one specific thing to coach on>", "<another flag if present>"],
  "summary": "<2-3 sentence plain English summary of the interaction quality>"
}
"""

def score_transcript(transcript_text):
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"{RUBRIC}\n\nTRANSCRIPT:\n{transcript_text}"
            }
        ]
    )
    
    raw = message.content[0].text
    clean = raw.strip()
    if clean.startswith("```"):
        clean = clean.split("\n", 1)[1]
    if clean.endswith("```"):
        clean = clean.rsplit("```", 1)[0]
    clean = clean.strip()
    result = json.loads(clean)
    return result

def format_report(result, transcript_name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = []
    lines.append("=" * 55)
    lines.append("  BPO QA SCORECARD")
    lines.append(f"  Transcript: {transcript_name}")
    lines.append(f"  Evaluated:  {now}")
    lines.append("=" * 55)
    lines.append("")
    
    lines.append("SCORES")
    lines.append("-" * 35)
    for category, score in result["scores"].items():
        label = category.replace("_", " ").title()
        bar = "█" * score + "░" * (10 - score)
        lines.append(f"  {label:<28} {bar} {score}/10")
    
    lines.append("")
    lines.append(f"  OVERALL SCORE:  {result['overall_score']}/10")
    lines.append(f"  RESULT:         {result['pass_fail']}")
    lines.append("")
    
    lines.append("HIGHLIGHTS")
    lines.append("-" * 35)
    for h in result["highlights"]:
        lines.append(f"  + {h}")
    lines.append("")
    
    lines.append("COACHING FLAGS")
    lines.append("-" * 35)
    for f in result["flags"]:
        lines.append(f"  ! {f}")
    lines.append("")
    
    lines.append("SUMMARY")
    lines.append("-" * 35)
    lines.append(f"  {result['summary']}")
    lines.append("")
    lines.append("=" * 55)
    
    return "\n".join(lines)

def main():
    print("\nBPO QA Scorecard Tool")
    print("---------------------")
    print("Paste your transcript below.")
    print("When finished, type END on a new line and press Enter.\n")
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    
    transcript = "\n".join(lines)
    
    if not transcript.strip():
        print("No transcript entered. Exiting.")
        return
    
    transcript_name = input("\nEnter a name for this transcript (e.g. ticket-1042): ").strip()
    if not transcript_name:
        transcript_name = "unnamed"
    
    print("\nScoring transcript...")
    
    result = score_transcript(transcript)
    report = format_report(result, transcript_name)
    
    print("\n" + report)
    
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_filename = f"{output_dir}/{transcript_name}_{timestamp}"
    
    with open(f"{base_filename}.txt", "w", encoding="utf-8") as f:
        f.write(report)
    
    with open(f"{base_filename}.json", "w") as f:
        json.dump(result, f, indent=2)
    
    print(f"\nFiles saved:")
    print(f"  {base_filename}.txt")
    print(f"  {base_filename}.json")

if __name__ == "__main__":
    main()
    