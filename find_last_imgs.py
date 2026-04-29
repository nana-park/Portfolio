import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    found = re.findall(r'<img[^>]+src=[\"\'](.*?)[\"\']', a['body_ko'])
    if found:
        print(f"{a['id']}: {found[-1]}")
    else:
        print(f"{a['id']}: None")
