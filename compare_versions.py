import json
import re

# Load previous (good) version
with open('articles_data_prev.js', 'r', encoding='utf-16') as f:
    prev_content = f.read()
prev_json = prev_content[prev_content.find('['): prev_content.rfind(']')+1]
prev_articles = json.loads(prev_json, strict=False)
prev_map = {a['id']: a for a in prev_articles}

# Load current (broken) version
with open('articles_data.js', 'r', encoding='utf-8') as f:
    curr_content = f.read()
curr_json = curr_content[curr_content.find('['): curr_content.rfind(']')+1]
curr_articles = json.loads(curr_json)
curr_map = {a['id']: a for a in curr_articles}

# Check which are significantly shorter
for aid, curr in curr_map.items():
    prev = prev_map.get(aid)
    if prev:
        ratio_en = len(curr['body_en']) / max(len(prev['body_en']), 1)
        ratio_ko = len(curr['body_ko']) / max(len(prev['body_ko']), 1)
        if ratio_en < 0.85 or ratio_ko < 0.85:
            print(f"[{aid}] DAMAGED: en {len(prev['body_en'])} -> {len(curr['body_en'])} ({ratio_en:.0%}), ko {len(prev['body_ko'])} -> {len(curr['body_ko'])} ({ratio_ko:.0%})")
