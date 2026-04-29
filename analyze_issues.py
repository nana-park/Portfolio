import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

# Patterns to analyze
for a in articles:
    body = a['body_en']
    stripped = body.lstrip()
    first_300 = stripped[:300]
    # check if starts with an image or empty-looking content
    if re.match(r'\s*<p[^>]*>\s*[·ㆍ.\-—_]+\s*</p>', stripped, re.IGNORECASE):
        print(f"[{a['id']}] Starts with DOT paragraph: {repr(stripped[:100])}")
    elif re.match(r'\s*<hr', stripped, re.IGNORECASE):
        print(f"[{a['id']}] Starts with HR: {repr(stripped[:100])}")
    elif re.match(r'\s*<p[^>]*>\s*(?:<br\s*/?>|\s)+\s*</p>', stripped, re.IGNORECASE):
        print(f"[{a['id']}] Starts with EMPTY paragraph: {repr(stripped[:100])}")

print("\n=== LAST ELEMENT CHECK ===")
for a in articles:
    body = a['body_en'].rstrip()
    # Check if ends with image
    if re.search(r'<img[^>]+>\s*</p>\s*$|<img[^>]+/>\s*</p>\s*$|</figure>\s*</div>\s*$', body, re.IGNORECASE):
        print(f"[{a['id']}] Ends with image: {repr(body[-200:])}")
