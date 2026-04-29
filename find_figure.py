import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

match = re.search(r'<div class="cheditor-caption-wrapper".*?</div>', articles[1]['body_en'], re.DOTALL)
if match:
    print(match.group(0))
else:
    for a in articles:
        match = re.search(r'<div class="cheditor-caption-wrapper".*?</div>', a['body_en'], re.DOTALL)
        if match:
            print(match.group(0))
            break
