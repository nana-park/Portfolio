import json
import re
import urllib.request
import os

os.makedirs('temp_imgs', exist_ok=True)

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for a in articles:
    found = re.findall(r'<img[^>]+src=[\"\'](.*?)[\"\']', a['body_ko'])
    if found:
        last_img_url = found[-1]
        try:
            filename = f"temp_imgs/{a['id']}.jpg"
            urllib.request.urlretrieve(last_img_url, filename)
            # Check dimensions if PIL is available, or just print sizes
            size = os.path.getsize(filename)
            print(f"{a['id']}: {last_img_url} (Size: {size} bytes)")
        except Exception as e:
            print(f"{a['id']}: Failed to download {last_img_url}")
