import requests

PROMPT = """
You are a professional frontend web developer.

TASK:
Generate a COMPLETE and VALID HTML website for a photographer portfolio.

STRICT RULES:
- Output ONLY valid HTML code
- Do NOT explain anything
- Do NOT add comments outside HTML
- Do NOT add text before or after HTML
- Include <html>, <head>, <body>
- Use internal <style> and <script>
- Close ALL tags

SECTIONS REQUIRED:
- Navbar
- Hero
- Gallery
- Contact form
- Footer
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama2",
        "prompt": PROMPT,
        "stream": False,
        "options": {
            "num_predict": 2048
        }
    }
)

html_output = response.json()["response"]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("index.html generated")
