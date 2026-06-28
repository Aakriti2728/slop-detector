import os
import json
from transformers import pipeline
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key="YOUR API KEY")

# Loads on startup — takes ~60 seconds first time (downloads 1.6GB model)
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

SLOP_LABELS = [
    "AI-generated generic filler content",
    "repetitive and hollow writing",
    "authentic human writing",
    "insightful and original content"
]

def hf_analyze(text: str) -> dict:
    result = classifier(text[:1000], candidate_labels=SLOP_LABELS)
    scores = dict(zip(result["labels"], result["scores"]))
    slop_score = (
        scores.get("AI-generated generic filler content", 0) * 0.5 +
        scores.get("repetitive and hollow writing", 0) * 0.5
    )
    return {
        "hf_slop_score": round(slop_score * 100, 1),
        "hf_breakdown": scores
    }

def groq_analyze(text: str) -> dict:
    prompt = f"""You are an AI slop detector. Analyze the following text and return a JSON object with:
- "slop_score": integer 0-100 (0 = genuine human writing, 100 = maximum AI slop)
- "verdict": one of "Slop-Free", "Mild Slop", "Certified Slop", "Pure Slop"
- "reasons": list of 3 short bullet points explaining your score

Text:
{text[:2000]}

Respond ONLY with valid JSON. No preamble. No markdown. No backticks."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown code fences if model adds them anyway
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    return json.loads(raw)