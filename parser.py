import re

with open("output.txt", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

def extract_between(start_tag, end_tag, fallback_pattern):
    if start_tag in content:
        start_index = content.find(start_tag) + len(start_tag)
        if end_tag in content:
            end_index = content.find(end_tag)
            return content[start_index:end_index].strip()
        else:
            # fallback if closing tag missing
            match = re.search(fallback_pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(0).strip()
            return content[start_index:].strip()
    return ""


html = extract_between("<HTML>", "</HTML>", r"<html.*?>.*")
css = extract_between("<CSS>", "</CSS>", r".*")
js = extract_between("<JS>", "</JS>", r".*")

if not html:
    raise ValueError("No HTML content generated")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Website files generated (with safety fallback)!")
