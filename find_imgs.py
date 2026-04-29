import json
import re

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

imgs = []
for a in articles:
    found = re.findall(r'<img[^>]+src=[\"\'](.*?)[\"\']', a['body_ko'])
    imgs.extend(found)

# count frequencies to find common signature images
from collections import Counter
counts = Counter(imgs)
for img, count in counts.most_common():
    print(f"{count}x : {img}")
