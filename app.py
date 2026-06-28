import json
from flask import Flask, render_template, request
from scraper import scrape_text
from analyzer import hf_analyze, groq_analyze
from scorer import aggregate_scores

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    url = request.form.get("url", "").strip()
    raw_text = request.form.get("text", "").strip()

    try:
        if url:
            text = scrape_text(url)
            source = url
        elif raw_text:
            text = raw_text[:4000]
            source = "Pasted text"
        else:
            return render_template("index.html", error="Provide a URL or paste some text.")

        hf_result = hf_analyze(text)
        groq_result = groq_analyze(text)
        result = aggregate_scores(hf_result, groq_result)
        result["source"] = source
        result["preview"] = text[:300] + "..."

        return render_template("result.html", result=result)

    except json.JSONDecodeError:
        return render_template("index.html", error="Groq returned invalid JSON. Try again.")
    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)