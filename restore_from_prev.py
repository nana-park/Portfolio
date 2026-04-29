import json
import re

# Load previous good version
with open('articles_data_prev_utf8.js', 'r', encoding='utf-8-sig') as f:
    prev_content = f.read()
prev_json = prev_content[prev_content.find('['): prev_content.rfind(']')+1]
prev_articles = json.loads(prev_json, strict=False)
prev_map = {a['id']: a for a in prev_articles}

# Load current version  
with open('articles_data.js', 'r', encoding='utf-8') as f:
    curr_content = f.read()
curr_json = curr_content[curr_content.find('['): curr_content.rfind(']')+1]
curr_articles = json.loads(curr_json)

DAMAGED_IDS = ['51061', '47268']

# Restore damaged articles from previous version
for a in curr_articles:
    if a['id'] in DAMAGED_IDS:
        prev = prev_map.get(a['id'])
        if prev:
            print(f"Restoring [{a['id']}]: en {len(a['body_en'])} -> {len(prev['body_en'])}, ko {len(a['body_ko'])} -> {len(prev['body_ko'])}")
            a['body_en'] = prev['body_en']
            a['body_ko'] = prev['body_ko']

new_content = "const articlesData = " + json.dumps(curr_articles, ensure_ascii=False, indent=2) + ";\n"
with open('articles_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done.")
