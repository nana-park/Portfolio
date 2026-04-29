import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

print("=== BEGINNING OF ARTICLES (to check top spacing) ===")
for a in articles[:3]:
    print(f"[{a['id']}]: {repr(a['body_en'][:100])}")

print("\n=== BLOCKQUOTES ===")
# Blockquotes might be tables, divs with background color, or <blockquote>
for a in articles:
    matches = re.findall(r'<table[^>]*>.*?</table>|<blockquote[^>]*>.*?</blockquote>', a['body_en'], re.DOTALL | re.IGNORECASE)
    if matches:
        for m in matches:
            if 'burst into blossom' in m or 'David Hockney' in m:
                print(f"[{a['id']}]: {m[:300]}...")

print("\n=== HEADINGS WITH HR OR BORDER-BOTTOM ===")
for a in articles:
    matches = re.findall(r'<p[^>]*>.*?(?:<hr[^>]*>|border-bottom[^>]*>|First, a happy point).*?</p>', a['body_en'], re.IGNORECASE | re.DOTALL)
    if matches:
        for m in matches:
            if 'First, a happy point' in m:
                print(f"[{a['id']}]: {m}")

# Also check for standalone hr
for a in articles:
    if '<hr' in a['body_en']:
        print(f"[{a['id']}] has <hr>")

