# AI Slop Detector
AI Slop Detector is a Flask-based web application that analyzes text and estimates whether it contains AI-generated, repetitive, or low-quality content ("AI slop").

## Features
- Analyze text pasted directly into the application.
- Analyze content from a webpage URL.
- Uses Hugging Face's BART Large MNLI model for zero-shot classification.
- Uses Groq's Llama model for AI-powered content evaluation.
- Generates a slop score from 0 to 100.
- Provides a verdict and reasons for the score.

## Tech Stack
- Python
- Flask
- Hugging Face Transformers
- Groq API
- BeautifulSoup
- HTML/CSS

## Project Structure
project/
│
├── app.py
├── analyzer.py
├── scorer.py
├── scraper.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
└── static/

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ai-slop-detector
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```
http://127.0.0.1:5000
```

## How It Works

1. User enters text or a URL.
2. The application extracts and processes the content.
3. Hugging Face and Groq models analyze the text.
4. Scores are combined to generate a final slop score.
5. The user receives a verdict and explanation.

## Future Improvements

- User authentication
- Analysis history
- PDF and document uploads
- Advanced content quality metrics


Aakriti Chandan
B.Tech CSE (AI & ML)
Amity University
