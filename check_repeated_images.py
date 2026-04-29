import json
import re
import urllib.request
import os
from collections import defaultdict

os.makedirs('temp_imgs', exist_ok=True)

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

size_map = defaultdict(list)

for a in articles:
    found = re.findall(r'<img[^>]+src=[\"\'](.*?)[\"\']', a['body_ko'])
    for url in found:
        try:
            filename = f"temp_imgs/{url.split('/')[-1]}"
            if not os.path.exists(filename):
                urllib.request.urlretrieve(url, filename)
            size = os.path.getsize(filename)
            size_map[size].append(url)
        except Exception as e:
            pass

for size, urls in size_map.items():
    if len(urls) > 1:
        print(f"Size {size} bytes appears {len(urls)} times.")
        print(f"  Example: {urls[0]}")
