import json, re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    a['body_en'] = re.sub(r'\.([A-Z])', r'. \1', a['body_en'])
    a['excerpt'] = re.sub(r'\.([A-Z])', r'. \1', a['excerpt'])

new_content = "const articlesData = " + json.dumps(articles, ensure_ascii=False, indent=2) + ";\n"

with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Spacing fixed!")
