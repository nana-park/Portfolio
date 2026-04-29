import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    # Google Translate sometimes hallucinates " | " or "<i> | </i>"
    a['body_en'] = a['body_en'].replace('<i> | </i>', '')
    a['body_en'] = re.sub(r'<p>\s*\|\s*</p>', '', a['body_en'])
    # also replace standalone | on its own line
    lines = a['body_en'].split('\n')
    new_lines = []
    for line in lines:
        if line.strip() == '|' or line.strip() == '<i> | </i>' or line.strip() == '<p>|</p>':
            continue
        new_lines.append(line)
    a['body_en'] = '\n'.join(new_lines)

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"

with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Pipe characters removed.")
