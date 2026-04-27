import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

# ============================================================
# 1. AGGRESSIVELY strip leading junk from body_en and body_ko
# ============================================================
# Matches: <p> that only contains dots, dashes, <br>, &nbsp;, whitespace, <i></i>, <b></b>, <hr>
leading_junk_pattern = re.compile(
    r'^(?:\s*<(?:hr[^>]*|p[^>]*)>\s*(?:'
    r'(?:<br\s*/?>|&nbsp;|\s|[·ㆍ\.\-—_\s]|</?[bi]>)*'
    r')\s*(?:</(?:p|hr)>)?\s*)+',
    re.IGNORECASE
)

def strip_leading_junk(html):
    # Iteratively remove leading empty/junk paragraphs and hr
    prev = None
    while prev != html:
        prev = html
        # Remove standalone <hr> at start
        html = re.sub(r'^\s*<hr[^>]*/?\s*>', '', html.lstrip(), flags=re.IGNORECASE)
        # Remove empty or dot-only <p>...</p> at start
        html = re.sub(
            r'^\s*<p[^>]*>\s*(?:<br\s*/?>|&nbsp;|\s|[·ㆍ\.\-—_]|</?[bi]>\s*)*\s*</p>',
            '', html.lstrip(), flags=re.IGNORECASE
        )
    return html.lstrip()

# ============================================================
# 2. Remove trailing images (bare <img> in <p>, or figure/div blocks at end)
# ============================================================
def strip_trailing_image(html):
    prev = None
    while prev != html:
        prev = html
        # Remove trailing <p ...><img .../></p>
        html = re.sub(
            r'\s*<p[^>]*>\s*<img[^>]+/?\s*>\s*</p>\s*$',
            '', html.rstrip(), flags=re.IGNORECASE
        )
        # Remove trailing figure wrapper div
        html = re.sub(
            r'\s*<div[^>]*class="cheditor-caption-wrapper"[^>]*>.*?</div>\s*$',
            '', html.rstrip(), flags=re.IGNORECASE | re.DOTALL
        )
        # Remove trailing empty paragraph after stripping
        html = re.sub(
            r'\s*<p[^>]*>\s*(?:<br\s*/?>|&nbsp;|\s)*\s*</p>\s*$',
            '', html.rstrip(), flags=re.IGNORECASE
        )
    return html.rstrip()

changed_count = 0
for a in articles:
    original_en = a['body_en']
    original_ko = a['body_ko']
    
    a['body_en'] = strip_leading_junk(a['body_en'])
    a['body_ko'] = strip_leading_junk(a['body_ko'])
    
    a['body_en'] = strip_trailing_image(a['body_en'])
    a['body_ko'] = strip_trailing_image(a['body_ko'])
    
    if a['body_en'] != original_en or a['body_ko'] != original_ko:
        changed_count += 1
        print(f"[{a['id']}] Modified")

print(f"\nTotal articles modified: {changed_count}")

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"
with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done.")
