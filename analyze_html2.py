import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

out = []
out.append("=== BEGINNING OF ARTICLES (to check top spacing) ===")
for a in articles[:3]:
    out.append(f"[{a['id']}]: {repr(a['body_en'][:100])}")

out.append("\n=== BLOCKQUOTES ===")
for a in articles:
    matches = re.findall(r'<table[^>]*>.*?</table>|<blockquote[^>]*>.*?</blockquote>|<div[^>]*style="[^"]*background[^"]*".*?</div>', a['body_en'], re.DOTALL | re.IGNORECASE)
    if matches:
        for m in matches:
            if 'burst into blossom' in m or 'David Hockney' in m:
                out.append(f"[{a['id']}]: {m[:300]}...")

out.append("\n=== HEADINGS WITH HR OR BORDER-BOTTOM ===")
for a in articles:
    matches = re.findall(r'<p[^>]*>.*?(?:<hr[^>]*>|border-bottom[^>]*>|First, a happy point).*?</p>', a['body_en'], re.IGNORECASE | re.DOTALL)
    if matches:
        for m in matches:
            if 'First, a happy point' in m:
                out.append(f"[{a['id']}]: {m}")

with open('analysis_utf8.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
