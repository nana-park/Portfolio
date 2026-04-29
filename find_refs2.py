import json

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

out = []
for a in articles:
    lines = a['body_en'].split('\n')
    for line in lines:
        if 'Freepik' in line or 'EBS' in line or 'Literacy' in line:
            out.append(f"[{a['id']}]: {line}")

with open('refs_utf8.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
