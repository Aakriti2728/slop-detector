def aggregate_scores(hf_result: dict, groq_result: dict) -> dict:
    hf_score = hf_result.get("hf_slop_score", 0)
    ai_score = groq_result.get("slop_score", 0)

    final_score = round(hf_score * 0.4 + ai_score * 0.6)

    if final_score < 25:
        label, color = "Slop-Free", "green"
    elif final_score < 50:
        label, color = "Mild Slop", "goldenrod"
    elif final_score < 75:
        label, color = "Certified Slop", "orange"
    else:
        label, color = "Pure Slop", "red"

    return {
        "final_score": final_score,
        "label": label,
        "color": color,
        "reasons": groq_result.get("reasons", []),
        "hf_score": hf_score,
        "ai_score": ai_score
    }