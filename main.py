from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() == "true"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],   # IMPORTANT
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_website(data: PromptRequest):
    if DEMO_MODE:
        return {
            "html": """<!DOCTYPE html>
<html>
<head><title>Demo Mode</title></head>
<body>
<h1>Demo Mode</h1>
<p>The full AI generation runs locally using LLaMA-2 via Ollama.</p>
<p>This cloud deployment demonstrates API and frontend integration.</p>
</body>
</html>"""
        }

    # existing LLaMA-2 logic below

    system_prompt = f"""
You are a professional frontend web developer.

TASK:
Generate a COMPLETE and VALID HTML website.

STRICT RULES:
- Output ONLY valid HTML
- No explanations
- Include <html>, <head>, <body>
- Use internal <style> and <script>
- Close ALL tags
IMAGE RULES (MANDATORY):
- DO NOT use local image files (no image1.jpg, no ./images)
- ALL images MUST use online placeholders
- Use this format ONLY:
 https://picsum.photos/400/300
 https://picsum.photos/seed/gallery1/400/300
 https://picsum.photos/seed/gallery2/400/300

Example:
<img src="https://picsum.photos/seed/gallery1/400/300" />
USER REQUIREMENT:
{data.prompt}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": system_prompt,
            "stream": False,
            "options": {"num_predict": 2048}
        }
    )

    raw_output = response.json()["response"]

    # 🔒 SANITIZE OUTPUT
    start = raw_output.lower().find("<!doctype html")
    end = raw_output.lower().rfind("</html>")

    if start != -1 and end != -1:
        clean_html = raw_output[start:end + len("</html>")]
    else:
        clean_html = raw_output
    import re

# 🔧 FIX BROKEN IMAGE SOURCES
    clean_html = re.sub(
    r'<img[^>]*src="(?!https?://)[^"]*"',
    lambda m: '<img src="https://picsum.photos/seed/fallback/400/300"',
    clean_html,
    flags=re.IGNORECASE
)

    return {"html": clean_html}
