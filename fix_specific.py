import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()
json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    # ---- Fix 1: Article 65427 ----
    if a['id'] == '65427':
        # 1a. Add period+space before "First of all, AI has several difficult There are"
        a['body_en'] = a['body_en'].replace(
            'difficult There are',
            'difficult. There are'
        )
        # 1b. Remove the trailing ")" in "to change)"
        # The pattern is: "to change)" inside a <b> tag
        a['body_en'] = re.sub(
            r'\bResistance to change to change\)',
            'Resistance to change',
            a['body_en']
        )
        # More general: any "to change)" -> "to change"
        a['body_en'] = a['body_en'].replace('to change)', 'to change')
        print(f"[65427] Fixed spacing and parenthesis")

    # ---- Fix 2: Article 58119 — strip leading empty article-subheading paragraphs ----
    if a['id'] == '58119':
        # Remove leading <p class="article-subheading"> that only contain whitespace
        before = a['body_en']
        a['body_en'] = re.sub(
            r'^(\s*<p[^>]*class="article-subheading"[^>]*>\s*(?:<[^>]*>)*\s*(?:</[^>]*>)*\s*</p>\s*)+',
            '',
            a['body_en'].lstrip(),
            flags=re.IGNORECASE
        )
        # Also remove any leading <hr>
        a['body_en'] = re.sub(r'^\s*<hr[^>]*/?\s*>', '', a['body_en'].lstrip(), flags=re.IGNORECASE)
        if a['body_en'] != before:
            print(f"[58119] Removed leading empty subheadings")
        else:
            print(f"[58119] No change (pattern didn't match) — current start: {repr(a['body_en'][:150])}")

print("Done.")

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"
with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
