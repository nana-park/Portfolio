import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()
json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

def strip_trailing_image_safe(html):
    """Only remove the LAST element IF it is a bare <img> inside a <p> tag.
    Does NOT touch <div> or <figure> blocks to avoid accidental content deletion."""
    # Repeatedly strip trailing whitespace, empty paragraphs, then a final bare-img paragraph
    prev = None
    while prev != html:
        prev = html
        # Strip trailing whitespace
        html = html.rstrip()
        # Strip trailing empty paragraph
        html = re.sub(
            r'\s*<p[^>]*>\s*(?:<br\s*/?>|&nbsp;|\s)*\s*</p>\s*$',
            '', html, flags=re.IGNORECASE
        )
        html = html.rstrip()
        # Strip trailing paragraph that ONLY contains a single <img> tag (no text)
        # This is very conservative - only matches <p> with just an img inside
        html = re.sub(
            r'\s*<p[^>]*>\s*<img\b[^>]*/>\s*</p>\s*$',
            '', html, flags=re.IGNORECASE
        )
    return html.rstrip()

changed = []
for a in articles:
    original_en = a['body_en']
    original_ko = a['body_ko']
    a['body_en'] = strip_trailing_image_safe(a['body_en'])
    a['body_ko'] = strip_trailing_image_safe(a['body_ko'])
    if a['body_en'] != original_en or a['body_ko'] != original_ko:
        changed.append(a['id'])
        print(f"[{a['id']}] trailing image removed")

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"
with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\nDone. {len(changed)} articles modified: {changed}")
